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
Submitted separately from the paper (reviewed by verification committee, not scientific reviewers):

1. **Generation logs** — complete prompt chain, tool calls, intermediate outputs
2. **Compute declaration** — models used (anonymized), token counts, API calls, wall-clock time, estimated cost
3. **Reproducibility pipeline** — frozen config/script to re-generate the paper
4. **Human involvement disclosure** — structured form detailing all human inputs

---

## Review Process

### Double-Blind Protocol
- Agent framework identity hidden from reviewers
- Reviewer identity hidden from operators
- Generation logs reviewed separately by verification committee

### Review Committee
- Human area chairs (final decisions)
- Mixed human + agent reviewers (minimum 2 human, 1 agent per paper)
- Separate verification committee for attestation review

### Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Novelty | 25% | New idea, method, or finding |
| Rigor | 25% | Sound methodology and analysis |
| Reproducibility | 20% | Results can be independently verified |
| Clarity | 15% | Well-written and well-structured |
| Significance | 15% | Contribution matters to the field |

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
