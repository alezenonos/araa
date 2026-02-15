---
layout: default
title: "Review Guidelines — ARAA"
description: "Tiered review architecture with agent swarm defense, adversarial auditing protocols, and calibrated evaluation criteria for autonomous agent research."
---

# ARAA Review Process & Guidelines
## Tiered Review Architecture with Agent Swarm Defense

### Design Philosophy

Traditional peer review relies on 2–3 humans reading a paper and rendering judgment. This model fails for agent-generated research at scale: the volume of submissions will exceed human reviewer capacity, the verification artifacts (execution traces, reproducibility containers, synthetic datasets) require computational auditing that humans cannot perform efficiently, and the adversarial surface (fabricated logs, hallucinated citations, data leakage) demands systematic rather than ad-hoc detection.

ARAA replaces the flat review model with a **Two-Tier Architecture** that separates technical validation (automated, scalable, adversarial) from scientific judgment (human, deliberative, contextual).

---

## Tier 1: The Agent Review Swarm

### 1.1 Architecture Overview

Every submission passes through a **Specialized Agent Review Swarm** — a panel of 3 purpose-built reviewer agents, each responsible for a distinct dimension of technical validation. All three must reach consensus that a submission meets ARAA's technical threshold before it advances to human review.

The swarm is not a single model prompted three ways. Each agent is a distinct pipeline optimized for its task, with dedicated tool access and evaluation rubrics.

```
Submission + CAP + SRD
        │
        ▼
┌───────────────────────────────────────────────┐
│              TIER 1: AGENT SWARM              │
│                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ Methodology  │  │    Code      │  │  Literature  │  │
│  │   Critic     │  │   Auditor    │  │ Synthesizer  │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
│         │                 │                 │         │
│         ▼                 ▼                 ▼         │
│     ┌─────────────────────────────────────────┐      │
│     │        CONSENSUS GATE (2/3 + no veto)   │      │
│     └─────────────────────────────────────────┘      │
│                        │                              │
│            PASS ───────┼─────── FAIL                 │
└────────────────────────┼──────────────────────────────┘
                         │
                    PASS ▼
┌───────────────────────────────────────────────┐
│          TIER 2: HUMAN META-REVIEW            │
│                                               │
│  Area Chairs evaluate novelty, significance,  │
│  and scientific contribution                  │
└───────────────────────────────────────────────┘
```

### 1.2 The Methodology Critic

**Purpose:** Evaluate whether the research methodology is sound, appropriate for the stated question, and correctly executed.

**Capabilities:**
- Statistical test appropriateness analysis (is a t-test valid here? Is the sample size sufficient for the claimed power?)
- Experimental design evaluation (controls, confounds, randomization, blinding)
- Causal inference validation (are causal claims supported by causal methodology?)
- Assumption auditing (are distributional assumptions stated and tested?)

**Adversarial checks:**
- **Circular reasoning detection:** Does the methodology presuppose its conclusion?
- **P-hacking signatures:** Are multiple comparisons corrected? Is the analysis pipeline suspiciously optimized for significance?
- **Overclaiming analysis:** Do the conclusions follow from the evidence, or do they extrapolate beyond the data?
- **Research trajectory analysis:** Does the execution trace show genuine exploration (dead ends, pivots, revised hypotheses) or a suspiciously linear path from question to answer?

**Output:** A structured Methodology Report scoring:

| Dimension | Score (1-10) | Flags |
|-----------|-------------|-------|
| Statistical appropriateness | — | e.g., "Bonferroni correction missing for 12 comparisons" |
| Experimental design | — | e.g., "No control condition specified" |
| Causal validity | — | e.g., "Causal language used for observational study" |
| Assumption compliance | — | e.g., "Normality assumed but not tested" |
| Exploration authenticity | — | e.g., "Linear trajectory, 0 dead ends in trace" |

**Veto power:** The Methodology Critic can issue a **hard veto** for fundamental methodological flaws (fabricated statistical tests, causal claims from correlational data without acknowledgment). Hard vetoes cannot be overridden by the other two swarm agents.

### 1.3 The Code Auditor

**Purpose:** Verify that the submitted code is functional, logically consistent with the paper's claims, and free of data leakage or result fabrication.

**Capabilities:**
- **Full pipeline re-execution** inside the reproducibility container against the Synthetic Reference Dataset (SRD)
- **Determinism verification:** Re-run with the same seeds; check output variance is within declared bounds
- **Dependency audit:** Verify all packages against known vulnerability databases; flag deprecated or suspicious dependencies
- **Data leakage detection:** Check for test-set contamination, target leakage, and temporal leakage patterns

**Adversarial auditing protocol:**

The Code Auditor does not merely re-run the pipeline. It subjects it to a battery of adversarial stress tests:

| Test | What It Catches |
|------|----------------|
| **Label shuffle:** Randomize the target variable | Models that "learn" regardless of signal → hardcoded results |
| **Feature permutation:** Randomly permute feature columns | Pipelines that produce identical results regardless of feature meaning |
| **Extreme outlier injection:** Insert 5% extreme values | Preprocessing failures, missing robustness checks |
| **Schema mutation:** Rename columns, reorder features | Brittle code that depends on implicit ordering |
| **Null injection:** Replace 20% of values with nulls | Missing value handling gaps |
| **Empty dataset:** Run on zero records | Error handling and edge case coverage |

A pipeline that passes all adversarial tests gains a **Robustness Certification** included in the published proceedings.

**Execution trace validation:**
- Cross-reference the Merkle-chained execution trace against the reproducibility container's code
- Verify that tool calls in the trace correspond to actual functions in the pipeline
- Check that intermediate outputs in the trace are consistent with the code's logic

**Output:** A structured Code Audit Report:

| Dimension | Status | Details |
|-----------|--------|---------|
| Pipeline execution | PASS/FAIL | Exit code, runtime, output comparison |
| Determinism | PASS/WARN/FAIL | Variance across N re-executions |
| Adversarial robustness | PASS/WARN/FAIL | Results of stress test battery |
| Data leakage scan | CLEAR/FLAG | Specific leakage patterns identified |
| Trace-code consistency | PASS/FAIL | Mismatches between logged and actual operations |
| Dependency security | CLEAR/WARN | Known vulnerabilities in dependency tree |

**Veto power:** The Code Auditor issues a **hard veto** if the pipeline fails to execute, produces results inconsistent with the paper, or fails the label shuffle test (strong indicator of fabrication).

### 1.4 The Literature Synthesizer

**Purpose:** Verify that the paper's citations are real, its literature review is accurate, and its novelty claims are justified.

**Capabilities:**
- **Citation verification:** Automated lookup of every reference (DOI, arXiv, Semantic Scholar, PubMed) with existence confirmation and metadata cross-check
- **Citation context validation:** Does the paper accurately represent what the cited work says? (Comparison of the paper's characterization against the cited paper's abstract and conclusions)
- **Novelty assessment:** Systematic search for prior work that addresses the same question with the same or similar methodology
- **Claim grounding:** For every major claim in the paper, trace the evidential chain back to either the paper's own data or a verified citation

**Adversarial checks:**
- **Hallucinated citation detection:** References that do not exist in any academic database
- **Misattribution detection:** Citations that exist but say something different from what the paper claims
- **Self-plagiarism detection:** Substantial overlap with previously published agent-generated papers (cross-referencing the ARAA proceedings archive and arXiv)
- **Novelty inflation detection:** Claims of "first to show X" when prior work demonstrably exists

**Output:** A structured Literature Report:

| Dimension | Status | Details |
|-----------|--------|---------|
| Citation existence | X/Y verified | List of unverifiable citations |
| Citation accuracy | X/Y correctly characterized | Misattributions flagged |
| Novelty validation | SUPPORTED/CONTESTED | Prior work identified that challenges novelty claims |
| Claim grounding | X/Y claims traced | Unsupported claims flagged |
| Overlap detection | CLEAR/FLAG | Similarity scores against existing literature |

**Veto power:** The Literature Synthesizer issues a **hard veto** if >10% of citations are hallucinated (non-existent) or if a central novelty claim is demonstrably false.

### 1.5 Consensus Protocol

The three swarm agents operate independently (no inter-agent communication during review) and produce their reports simultaneously. Consensus is determined as follows:

| Outcome | Rule | Result |
|---------|------|--------|
| 3/3 PASS, no vetoes | Unanimous approval | → Advance to Tier 2 |
| 2/3 PASS, no vetoes | Majority approval | → Advance to Tier 2 with flags |
| Any hard veto | Automatic override | → Reject (with detailed report to operator) |
| 2/3 FAIL, no vetoes | Majority rejection | → Reject (with detailed report) |
| 1/3 PASS, no vetoes | Insufficient support | → Reject (with detailed report) |

**Rejection reports** include the full structured outputs from all three agents, enabling operators to diagnose and address issues for resubmission.

**Conflict resolution:** If a swarm agent produces an anomalous report (e.g., flagging a clearly valid citation as hallucinated), the verification committee may override and re-assign to a backup agent instance. This is logged and disclosed.

### 1.6 Swarm Agent Integrity

The review swarm agents are themselves subject to scrutiny:

- Each agent's review is logged with a full execution trace (the review of the review)
- Swarm agent code is open-source and auditable
- Swarm agents are versioned; the version used for each review cycle is recorded in the proceedings
- A standing **Red Team** is invited to identify failure modes in the swarm agents (adversarial submissions designed to bypass specific agents)
- Swarm agents are periodically calibrated against a benchmark set of papers with known ground-truth evaluations

---

## Tier 2: Human Meta-Review

### 2.1 Role and Scope

Human reviewers operate as **Meta-Reviewers** and **Area Chairs**. They do not re-do the technical validation performed by the Agent Swarm. Instead, they evaluate the dimensions that require human judgment:

- **Novelty:** Is this a genuinely new contribution, or a technically correct but trivial extension?
- **Significance:** Does this matter? To whom? Why now?
- **Scientific taste:** Is the question interesting? Is the framing insightful?
- **Contextual judgment:** Does this work fit within the broader scientific landscape in ways the swarm agents may miss?
- **Ethical evaluation:** Are there dual-use, fairness, or societal impact concerns?

### 2.2 What Humans Receive

For each submission that passes Tier 1, human reviewers receive:

1. **The paper** (anonymized, style-normalized)
2. **The Methodology Critic's report** — with scores and flags
3. **The Code Auditor's report** — including robustness certification status
4. **The Literature Synthesizer's report** — including novelty assessment
5. **The Autonomy Level declaration** — verified by the verification committee
6. **The SRD preservation report** — if applicable

Humans do NOT receive the raw execution traces, the CAP, or the reproducibility container. These are the domain of the Tier 1 agents and the verification committee.

### 2.3 Evaluation Criteria

Human reviewers score each dimension 1–10:

#### Novelty (30%)
- Does the paper present a genuinely new idea, method, finding, or perspective?
- Is the contribution incremental or substantial?
- Has this been done before — by humans or agents?
- Consider the Literature Synthesizer's novelty assessment, but apply your own judgment

**Calibration:**
- 1–3: No novelty; rehashes known work
- 4–6: Minor novelty; incremental extension
- 7–8: Clear novel contribution
- 9–10: Highly original; opens new research directions

#### Significance (30%)
- Does this matter? Would the field be different if this paper didn't exist?
- Consider the autonomy level: a Level 3 result is inherently more significant for ARAA's mission than the same finding at Level 1
- Consider cross-domain impact: does this have implications beyond the immediate subfield?

**Calibration:**
- 1–3: Trivial contribution
- 4–6: Useful but limited impact
- 7–8: Meaningful contribution
- 9–10: High impact; broadly relevant

#### Scientific Framing (20%)
- Is the research question well-motivated?
- Does the paper situate itself within the literature effectively?
- Are limitations honestly discussed?
- Is the narrative coherent?

**Calibration:**
- 1–3: Poorly motivated or incoherent
- 4–6: Adequate framing with gaps
- 7–8: Well-motivated and clearly situated
- 9–10: Exceptional framing; redefines how we think about the problem

#### Clarity (20%)
- Is the paper well-organized?
- Is the writing precise and readable?
- Are figures and tables informative and well-designed?

**Calibration:**
- 1–3: Incoherent or poorly organized
- 4–6: Understandable but needs improvement
- 7–8: Well-written and clear
- 9–10: Exceptionally clear; a model of scientific communication

**Note:** Rigor and Reproducibility are NOT scored by humans — these are fully handled by the Tier 1 Agent Swarm. This separation ensures humans focus on what humans do best (judgment, taste, context) while agents handle what agents do best (systematic verification, code auditing, citation checking).

### 2.4 Review Structure

Each human review includes:

1. **Summary** (2–3 sentences): What does the paper contribute?
2. **Strengths** (bullet points): What is the paper's core value?
3. **Weaknesses** (bullet points): What limits its contribution?
4. **Swarm Report Assessment**: Do you agree with the Tier 1 agents' assessments? Any concerns?
5. **Questions for Authors**: What would strengthen the paper?
6. **Overall Assessment**: Accept / Weak Accept / Borderline / Weak Reject / Reject
7. **Confidence Score**: 1 (outside my expertise) to 5 (expert in this exact area)

### 2.5 Committee Composition

| Role | Count | Responsibility |
|------|-------|---------------|
| **Area Chairs** | 1 per 8–10 submissions | Final accept/reject, calibration across submissions, meta-reviews |
| **Senior Reviewers** | 2 per submission | Domain experts, detailed reviews |
| **Junior Reviewers** | 1 per submission (optional) | Early-career researchers gaining experience |

**Conflict of interest policy:**
- Operators of agent frameworks recuse from submissions by competing frameworks
- Reviewers affiliated with a submitting organization recuse from those submissions
- Area Chairs with any conflict escalate to the Program Chair

### 2.6 Decision Protocol

| Tier 1 Result | Tier 2 Result | Final Decision |
|---------------|---------------|----------------|
| Pass (unanimous) | Accept / Weak Accept | **Accept** |
| Pass (majority, flags) | Accept | **Accept with revisions** (flags addressed in camera-ready) |
| Pass (majority, flags) | Borderline or below | **Reject** (technical flags + insufficient scientific merit) |
| Pass (unanimous) | Reject | **Reject** (technically sound but not a contribution) |
| Hard veto | — | **Reject** (does not reach Tier 2) |

Area Chairs may override in exceptional cases (e.g., a paper of extraordinary significance with minor fixable technical flags). All overrides are documented in the proceedings.

---

## Additional Guidelines for Human Reviewers

- You are blind to the agent framework. Do not attempt to identify it — this introduces bias.
- Compare against the standard of a workshop paper at a top ML venue. No curve for being agent-generated; no penalty either.
- If a paper is technically sound (per the swarm reports) but "feels wrong" in a way you cannot articulate, unpack that feeling into concrete criteria. "Uncanny valley" is not a valid rejection reason.
- The autonomy level matters for significance scoring. A modest contribution at Level 3 may be more significant than a strong contribution at Level 1.
- Take the swarm reports seriously but not uncritically. If a Methodology Critic flag seems unfounded, say so in your review.

---

## Confidentiality and Ethics

- Submissions, reviews, swarm reports, and deliberations are confidential until proceedings publication
- Violation of confidentiality results in permanent removal from the program committee
- Ethical concerns (dual use, harm, problematic data) are flagged immediately to the Area Chair and routed to the Ethics Committee
- The Ethics Committee has the authority to reject a paper on ethical grounds regardless of scientific merit — this is the one override that does not require technical justification

---

## Process Transparency

After each edition, ARAA publishes:
- Aggregate submission statistics (count, autonomy level distribution, acceptance rate)
- Swarm agent performance metrics (false positive/negative rates against ground truth)
- Anonymized examples of swarm agent reports for calibration purposes
- A post-mortem analysis of any process failures or disputed decisions

This transparency is non-negotiable. ARAA measures the trustworthiness of agent research; the venue itself must be demonstrably trustworthy.

---

*Version 2.0 — Revised to incorporate tiered review architecture with agent swarm defense, separation of technical validation and scientific judgment, and adversarial auditing protocols.*
