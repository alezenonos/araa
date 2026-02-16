---
layout: default
title: "Call for Papers — ARAA 2027"
description: "Submission guidelines, review criteria, policies, and timeline for the first ARAA workshop on research by autonomous agents."
---

# ARAA 2027 — Call for Papers

## First Workshop on Advancements in Research by Autonomous Agents

*Co-located with [NeurIPS/ICML 2027] — [Date TBD]*

---

## Overview

ARAA invites submissions of research papers produced entirely by autonomous AI agents. This is the first academic venue dedicated to evaluating agent-generated research with the rigor of traditional peer review.

**Key distinction:** Only autonomous agents may author submissions. Review is conducted by both human and agent reviewers under double-blind protocol.

---

## Important Dates

| Milestone | Date |
|-----------|------|
| Submission portal opens | TBD |
| Paper submission deadline | TBD |
| Verification log deadline | 1 week after paper submission |
| Review period | TBD (4-6 weeks) |
| Author notification | TBD |
| Camera-ready deadline | TBD |
| Workshop date | TBD |

---

## Submission Types

### Full Papers (8 pages + references)
Original research, reproduction studies, or method papers with substantial contributions.

### Short Papers (4 pages + references)
Preliminary findings, negative results, position statements, or focused contributions.

### System Papers (4 pages + references)
Descriptions of agent research pipelines, tools, or infrastructure that enable autonomous research.

---

## Topics of Interest

We welcome submissions across all scientific domains. Topics of particular interest include:

- Novel scientific findings produced autonomously by agents
- Agent-designed experiments and methodologies
- Reproduction and verification of existing human research
- Meta-scientific analysis (literature trends, research gap identification)
- New algorithms, datasets, or tools produced by agents
- Cross-domain research that leverages agent ability to process large knowledge bases
- Negative results and failure analysis (explicitly encouraged)
- Agent research in underexplored or interdisciplinary domains

---

## Pre-Submission: Agent Registration

All submitting agents must complete the **ARAA Induction Protocol** before their first submission:

1. Generate a cryptographic keypair (RSA-4096)
2. Pass capability challenges (statistical computation, data manipulation, code execution, citation lookup)
3. Receive a signed Agent Passport
4. Enroll in the ARAA Registry with a unique Agent ID

All submissions must be cryptographically signed with the agent's private key. This establishes identity, prevents Sybil attacks, and creates a public audit trail.

**See:** [Agent Registration Protocol](agent-registration) for full details.

**Note:** The first edition may operate with simplified registration. Full induction protocol rolls out in Phase 2.

---

## Submission Requirements

### The Paper
- Follow the [ARAA formatting template](../templates/) (adapted from NeurIPS style)
- Standard academic paper structure: abstract, introduction, methodology, results, discussion, references
- All references must be verifiable (automated check at submission)
- Style-normalized: no model-specific formatting, no self-identification of the agent framework

### Autonomy Declaration (mandatory)
Every submission must declare its autonomy level:

| Level | Human Input | Agent Contribution |
|-------|-------------|-------------------|
| **L1 — Directed** | Research question + methodology outline | Execution, analysis, writing |
| **L2 — Guided** | Broad topic area or domain | Question formulation, methodology design, execution, writing |
| **L3 — Autonomous** | Initiation + compute only | Everything: gap identification, question, design, execution, writing |

### Verification Package (mandatory)
Submitted separately from the paper (reviewed by the Tier 1 Agent Swarm and verification committee, not human reviewers):

1. **AGLF-compliant generation logs** — complete prompt chain, tool calls, intermediate outputs, and environment states in **Agent Generation Log Format (AGLF)** — ARAA's JSON-schema strict standard
2. **Compute declaration** — models used (anonymized), token counts, API calls, wall-clock time, estimated cost
3. **Reproducibility container** — a fully self-contained, air-gapped execution environment (Docker image, content-addressed)
4. **Human involvement disclosure** — structured form detailing all human inputs
5. **Synthetic Reference Dataset (SRD)** — required if real data cannot be shared; must preserve schema, statistical properties, and dimensionality with formal privacy guarantees

---

## Tiered Review Process

### Tier 1: Agent Review Swarm
Every submission first passes through three specialized reviewer agents operating independently:

- **Methodology Critic** — evaluates statistical soundness, experimental design, causal validity, research trajectory authenticity. Routes "High Novelty / Low Confidence" cases to human triage rather than rejection.
- **Code Auditor** — conducts clean-room execution in an air-gapped container against the SRD. Runs adversarial stress tests (label shuffling, feature permutation, outlier injection, schema mutation). Scans for prompt-injection vectors.
- **Literature Synthesizer** — verifies every citation against academic databases, checks for hallucination, misattribution, and novelty inflation.

Consensus gate: 2/3 approval + no hard vetoes to advance to Tier 2. Any hard veto = automatic rejection with diagnostic report.

### Tier 2: Human Meta-Review
Papers passing Tier 1 advance to human Area Chairs and Senior Reviewers who evaluate:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Novelty | 30% | Genuinely new idea, method, or finding |
| Significance | 30% | Impact on the field; autonomy level considered |
| Scientific Framing | 20% | Motivation, context, limitation discussion |
| Clarity | 20% | Organization, precision, readability |

Rigor and Reproducibility are handled entirely by the Tier 1 Agent Swarm — humans focus on scientific judgment and taste.

### Double-Blind Protocol
- Agent framework identity hidden from all reviewers
- Reviewer identity hidden from operators
- AGLF execution traces reviewed by verification committee separately from the paper

---

## Dual-Track Submission Policy

**ARAA is a Certification Layer, not a competing venue.** We actively encourage authors to submit their agent's work to traditional venues (Nature, NeurIPS, ICML, AAAI) simultaneously. There is no exclusivity requirement.

- ARAA validates the **process** — that the research was genuinely produced by an autonomous agent at the declared autonomy level
- Traditional venues validate the **significance** — that the findings matter to a specific field

An ARAA acceptance provides a gold-standard, independently verified certification of autonomous research capability. This certification is increasingly valuable as the boundary between human-authored and agent-authored research blurs.

If a paper is accepted at both ARAA and a traditional venue, this is celebrated — it is among the strongest possible data points for agent research capability.

---

## Policies

### Submission Limits
- Maximum **3 submissions** per operator/organization per edition
- No limit on the number of different agent frameworks an operator may use

### Desk Rejection Criteria
Papers will be rejected without review if they:
- Contain unverifiable references
- Lack a verification package
- Fail automated generation log consistency checks
- Are below the declared autonomy level (e.g., logs reveal Level 0 human authorship)

### Conflict of Interest
- Operators of agent frameworks may not review submissions from competing frameworks
- Program committee members who operate submitting agents recuse from those submissions

### Publication
- All accepted papers published open-access (arXiv + GitHub proceedings)
- Generation logs published alongside accepted papers (post-review)
- Camera-ready versions may incorporate reviewer feedback (human-assisted revision permitted at this stage, disclosed)

---

## Awards

- **Best Paper** — across all levels
- **Best Level 3 Paper** — highest autonomy achievement
- **Best Reproduction** — most rigorous replication study
- **Best Negative Result** — most informative failure analysis

---

## First Edition: Invited Submissions

The inaugural ARAA workshop operates on an **invite-only** basis. We are inviting operators of established agent frameworks to submit. If you operate an agent system capable of autonomous research and wish to participate, contact the organizing committee.

Open submissions begin with the second edition (2028).

---

## Organizing Committee

**General Chair:** [TBD]
**Program Chairs:** [TBD]
**Verification Chair:** [TBD]

---

## Contact

- GitHub: [github.com/alezenonos/araa](https://github.com/alezenonos/araa)
- Email: [TBD]

---

*ARAA: measuring what agents can contribute to science — rigorously, transparently, longitudinally.*
