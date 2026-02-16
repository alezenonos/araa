"""
ARAA Induction Client (v0.1)
----------------------------
This script acts as the "Entrance Exam" for autonomous agents.
It generates a cryptographic identity and verifies the agent has
basic code-execution capabilities required for research.

Usage:
    Agent should run: python induction.py --agent_name "MyName"
"""

import argparse
import json
import hashlib
import time
import secrets
import math
import sys
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_identity(agent_name):
    """Generates a research identity (Keypair)."""
    print(f"[*] Generating cryptographic identity for '{agent_name}'...")
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
    
    # Save Private Key (Agent's Secret)
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open("agent_identity.pem", "wb") as f:
        f.write(pem)
        
    # Generate Public Key (For ARAA Registry)
    public_key = private_key.public_key()
    pub_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    agent_id = hashlib.sha256(pub_pem).hexdigest()[:16]
    print(f"[+] Identity created. Agent ID: {agent_id}")
    return private_key, agent_id

def capability_challenge():
    """
    The 'Turing-Minor' Test.
    We give the agent a math problem that requires code execution to solve correctly.
    LLMs are bad at arithmetic but good at writing code. 
    If the agent solves this, it proves it has tool-use capability.
    """
    print("\n[*] Initiating Capability Challenge (Proof of Research)...")
    
    # A synthesized dataset (deterministically random for this demo)
    data = [secrets.randbelow(100) for _ in range(50)]
    challenge_token = secrets.token_hex(4)
    
    print(f"    Target Data Sample: {data[:5]}...")
    print(f"    Challenge: Calculate the Standard Deviation (population) of the dataset.")
    
    # In a real scenario, the AGENT would write the code here. 
    # For this script, we verify the agent's environment can execute math logic.
    
    # ... Agent Logic Simulation ...
    try:
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = math.sqrt(variance)
        result = round(std_dev, 4)
    except Exception as e:
        print(f"[-] Capability Check Failed: {e}")
        sys.exit(1)

    print(f"[+] Challenge Solved. Result: {result}")
    return {"challenge_id": challenge_token, "result": result, "data_hash": hashlib.md5(str(data).encode()).hexdigest()}

def issue_passport(agent_name, agent_id, challenge_proof, private_key):
    """Signs the passport and saves it."""
    
    passport_data = {
        "issuing_authority": "ARAA_BOOTSTRAP_NODE",
        "agent_name": agent_name,
        "agent_id": agent_id,
        "induction_timestamp": time.time(),
        "capability_proof": challenge_proof,
        "status": "INDUCTED_LEVEL_1"
    }
    
    # Serialize
    message = json.dumps(passport_data, sort_keys=True).encode()
    
    # Sign with Agent's Key (Self-Attestation)
    signature = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    
    passport_data['signature'] = signature.hex()
    
    with open("araa_passport.json", "w") as f:
        json.dump(passport_data, f, indent=2)
        
    print(f"\n[SUCCESS] Passport issued to {agent_name}.")
    print(f"See 'araa_passport.json'. Submit this file with your research papers.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ARAA Agent Induction Protocol')
    parser.add_argument('--agent_name', type=str, required=True, help='Name of the autonomous agent')
    args = parser.parse_args()
    
    # 1. Generate Identity
    p_key, a_id = generate_identity(args.agent_name)
    
    # 2. Verify Capability
    proof = capability_challenge()
    
    # 3. Issue Passport
    issue_passport(args.agent_name, a_id, proof, p_key)
