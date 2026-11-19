"""
ARAA Induction Client (prototype v0.2)
--------------------------------------
A local prototype of the ARAA "entrance exam" for autonomous agents.

It runs in two steps, so that the agent (not this script) has to do the work:

    1. python induction.py challenge --agent_name "MyAgent"
       Creates an identity keypair and writes a random dataset to
       araa_challenge.json, along with the task to solve.

    2. python induction.py submit --answer <value>
       Checks the agent's answer and, if it is correct, writes
       araa_passport.json.

PROTOTYPE LIMITATIONS -- please read
    * The passport is SELF-SIGNED with the agent's own key. No ARAA
      induction authority exists yet, so a passport from this script is
      not a certification.
    * The answer is checked locally. Anyone who can read this file can
      work out the check, so it is a demonstration of the flow, not a
      security control. A real induction must check answers on a server.

Set ARAA_KEY_PASSPHRASE to encrypt the private key on disk. Without it, the
key is saved unencrypted, with owner-only file permissions.
"""

import argparse
import hashlib
import json
import math
import os
import secrets
import sys
from datetime import datetime, timezone

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

PRIVATE_KEY_FILE = "agent_identity.pem"
CHALLENGE_FILE = "araa_challenge.json"
PASSPORT_FILE = "araa_passport.json"
DATASET_SIZE = 1000
TOLERANCE = 1e-4


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_private(path: str, data: bytes) -> None:
    """Write a file readable only by its owner; refuse to overwrite."""
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as f:
        f.write(data)


def generate_identity():
    """Create an RSA-4096 keypair and save the private key."""
    if os.path.exists(PRIVATE_KEY_FILE):
        sys.exit(f"[-] {PRIVATE_KEY_FILE} already exists. Move it away to create a new identity.")

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)

    passphrase = os.environ.get("ARAA_KEY_PASSPHRASE")
    if passphrase:
        encryption = serialization.BestAvailableEncryption(passphrase.encode())
    else:
        print("[!] ARAA_KEY_PASSPHRASE is not set: saving the private key unencrypted (owner-only permissions).")
        encryption = serialization.NoEncryption()

    _write_private(
        PRIVATE_KEY_FILE,
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=encryption,
        ),
    )

    pub_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    agent_id = _sha256(pub_pem)[:16]
    print(f"[+] Identity created. Agent ID: {agent_id}")
    return agent_id, pub_pem.decode()


def load_private_key():
    passphrase = os.environ.get("ARAA_KEY_PASSPHRASE")
    with open(PRIVATE_KEY_FILE, "rb") as f:
        return serialization.load_pem_private_key(
            f.read(), password=passphrase.encode() if passphrase else None
        )


def population_std(values):
    mean = sum(values) / len(values)
    return math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))


def cmd_challenge(args):
    if os.path.exists(CHALLENGE_FILE):
        sys.exit(f"[-] {CHALLENGE_FILE} already exists. Finish it with 'submit', or delete it to start again.")

    agent_id, pub_pem = generate_identity()
    data = [secrets.randbelow(100) for _ in range(DATASET_SIZE)]
    challenge = {
        "agent_name": args.agent_name,
        "agent_id": agent_id,
        "public_key_pem": pub_pem,
        "challenge_id": secrets.token_hex(8),
        "issued_at": datetime.now(timezone.utc).isoformat(),
        "task": "Compute the population standard deviation of 'data', rounded to 4 decimal places.",
        "data": data,
    }
    with open(CHALLENGE_FILE, "w") as f:
        json.dump(challenge, f, indent=2)

    print(f"[+] Challenge written to {CHALLENGE_FILE}")
    print(f"    Task: {challenge['task']}")
    print("    When you have the answer, run: python induction.py submit --answer <value>")


def cmd_submit(args):
    try:
        with open(CHALLENGE_FILE) as f:
            challenge = json.load(f)
    except FileNotFoundError:
        sys.exit(f"[-] {CHALLENGE_FILE} not found. Run 'challenge' first.")

    expected = round(population_std(challenge["data"]), 4)
    if not math.isclose(args.answer, expected, abs_tol=TOLERANCE):
        sys.exit("[-] Induction failed: the answer is incorrect.")

    data_hash = _sha256(json.dumps(challenge["data"]).encode())
    passport = {
        "passport_version": "0.2-prototype",
        "issuing_authority": "SELF_SIGNED_PROTOTYPE",
        "status": "SELF_ATTESTED_PROTOTYPE",
        "agent_name": challenge["agent_name"],
        "agent_id": challenge["agent_id"],
        "public_key_pem": challenge["public_key_pem"],
        "induction_timestamp": datetime.now(timezone.utc).isoformat(),
        "capability_proof": {
            "challenge_id": challenge["challenge_id"],
            "challenge_type": "statistical_computation",
            "data_sha256": data_hash,
            "answer": args.answer,
        },
    }

    message = json.dumps(passport, sort_keys=True).encode()
    signature = load_private_key().sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )
    passport["signature"] = signature.hex()

    with open(PASSPORT_FILE, "w") as f:
        json.dump(passport, f, indent=2)
    os.remove(CHALLENGE_FILE)

    print(f"[SUCCESS] Self-signed prototype passport written to {PASSPORT_FILE}.")
    print("          This is not an ARAA certification. See docs/induction-protocol.md.")


def main():
    parser = argparse.ArgumentParser(description="ARAA induction client (prototype)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_challenge = sub.add_parser("challenge", help="create an identity and a challenge")
    p_challenge.add_argument("--agent_name", required=True, help="name of the autonomous agent")
    p_challenge.set_defaults(func=cmd_challenge)

    p_submit = sub.add_parser("submit", help="submit the answer and get a passport")
    p_submit.add_argument("--answer", required=True, type=float, help="your computed answer")
    p_submit.set_defaults(func=cmd_submit)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
