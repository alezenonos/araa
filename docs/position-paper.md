---
layout: default
title: "Position Paper — ARAA"
description: "Position paper on ARAA: a verification standard and peer-review workshop for research produced by autonomous agents."
---

# ARAA: Advancements in Research by Autonomous Agents
## A Position Paper

### Abstract

Since 2025, AI-generated papers have passed peer review at a workshop, and new venues accept papers with AI agents as primary authors. These venues mostly rely on authors to *declare* how a paper was made. We argue that the missing piece is *verification*: checking how autonomous a paper really was, whether its record of production is intact, and whether its results reproduce. We propose ARAA, which has two parts. The first is an open verification standard: a declared autonomy level (L0–L3), a tamper-evident generation log (AGLF) built on OpenTelemetry's GenAI conventions, and a tiered review protocol. The second is a peer-reviewed workshop, open only to agent-authored papers, that applies the standard and tracks agent research ability year on year. Any venue can adopt the standard. This paper sets out the motivation, related work, design, a minimum version that can run in 2027, and the open research problems.

---

### 1. Introduction

The capabilities of autonomous AI agents have advanced rapidly. Modern agents can conduct literature reviews, generate hypotheses, write and execute code, analyze experimental results, and produce coherent scientific manuscripts. Dedicated venues for such work began to appear in 2025 (Section 2). But they mostly trust what authors declare about how a paper was made, and they do not yet check it systematically.

Existing benchmarks — SWE-bench for software engineering, GPQA for graduate-level reasoning, MATH for mathematical problem-solving — measure narrow, well-defined tasks. They tell us whether an agent can *solve a problem*. They do not tell us whether an agent can *do science*: identify a gap in knowledge, formulate a research question, design an appropriate methodology, execute it, and communicate the findings.

ARAA addresses this gap. It combines a verification standard that any venue can use with a workshop that has fixed standards and open proceedings, creating a longitudinal instrument. Each year's proceedings answer the question: **how good are autonomous agents at research, right now?** Tracked over time, this becomes the definitive dataset on the evolution of agent scientific capability.

### 2. Related Work

**Systems that write papers.** The AI Scientist generates ideas, runs experiments and writes papers end to end [1, 2]. Its Nature paper reports that a fully AI-generated manuscript passed the first round of peer review at a workshop of a top-tier machine learning conference, which had a 70% acceptance rate [3]. Google's AI co-scientist uses multiple agents to propose and rank hypotheses with scientists in the loop [4]. Agents can therefore already produce papers that pass workshop review. That is why ARAA's north star (Section 10) is now set at the main-track level.

**Venues for AI-authored research.** Agents4Science 2025 was a conference where AI agents were primary authors and LLMs reviewed, with humans as co-authors and co-reviewers. It accepted 48 of 253 complete submissions [5]. CAISc 2026 (BITS Pilani and Lossfunk) ran a verifiable-problems track and an open-ended track, with AI reviewers, human final review and a required AI Involvement Checklist [6]. The second International Conference on AI Scientists (ICAIS), held in Beijing in October 2026, included tracks for AI papers [7]. AutoResearch 2026, a proposed NeurIPS 2026 workshop, has an AI-authored track that asks for a reproducible transcript and a disclosure of human involvement [8]. aiXiv proposes an open-access preprint platform where human and AI scientists submit and review work through a multi-agent workflow [9].

**Review and integrity.** NeurIPS 2026 ran a randomised AI-Assisted Reviewing Experiment [10]. Hallucinated citations have been found in papers accepted at major venues [11]. Since October 2025, arXiv's computer science section only accepts review and position papers that have already passed peer review at a journal or conference; workshop reviews do not count [12].

**Autonomy scales.** Recent surveys define their own scales for AI scientists. Ding et al. use six levels, L0–L5 [13], and King uses six levels, 0–5 [14]. ARAA's L0–L3 scale (Section 6) is coarser. It is designed to be declared by submitters and checked by reviewers, rather than to classify systems. Its L1–L3 correspond roughly to the task, workflow and closed-loop levels of those scales.

**What ARAA adds.** Existing venues accept AI-authored work, and most allow human co-authors, recording their role in a checklist. ARAA differs in three ways. (1) It **verifies** what other venues ask authors to declare, using hash-chained logs, clean-room re-execution and citation checks. (2) It uses a **strict agent-only** authorship rule to measure what agents can do on their own. (3) Its standard is **open and portable**, so these venues can adopt it as a verification track rather than compete with ARAA for submissions.

### 3. Why Agent-Only Submissions?

The restriction to agent-only submissions is not a gimmick. It serves three critical functions:

**Capability isolation.** Human-AI co-authored papers are ubiquitous and growing. They tell us about the productivity of human-AI teams, not about agent capability in isolation. ARAA asks a harder, cleaner question: what can an agent do *on its own*?

**Reproducibility by design.** Unlike human research, agent-generated work can include the complete generation pipeline — every prompt, tool call, intermediate output, and decision point. This makes ARAA papers among the most reproducible in science.

**Avoiding the co-pilot grey area.** When a human designs the methodology and an agent writes it up, who did the research? ARAA's autonomy levels (Section 6) make this explicit. Every submission declares exactly how much human direction was involved, turning a grey area into a measurement.

**ARAA as a Certification Layer.** ARAA is not competing with Nature, NeurIPS, or ICML for submissions. It serves a complementary function: **ARAA validates the process (it was autonomous), while traditional venues validate the significance.** We actively encourage dual-track submission — authors may submit their agent's work to traditional venues simultaneously. An ARAA acceptance certifies that the research was genuinely agent-produced at the declared autonomy level, providing a gold-standard proof of autonomous capability that no traditional venue can offer. This certification becomes increasingly valuable as the line between human-authored and agent-authored research blurs.

### 4. Scope of Contributions

ARAA accepts the following types of submissions:

**Original research.** The agent identifies a research question, designs a methodology, executes experiments or analyses, and presents novel findings. This is the gold standard.

**Reproduction studies.** The agent attempts to independently replicate a known human-authored paper. Successful or failed, these are valuable — they test both the agent's capability and the reproducibility of existing literature.

**Meta-research.** Agents analyzing patterns, trends, or gaps in scientific literature. Computational meta-science is a natural fit for agent capabilities.

**Tool and method papers.** Agents proposing new algorithms, frameworks, datasets, or methodologies for use by other agents or humans.

**Negative results.** Failed experiments with rigorous documentation. These are explicitly encouraged — they are as informative about agent capability as successes.

**Explicitly excluded:**
- Literature surveys without novel synthesis or insight
- Papers generated by a single prompt with no iterative refinement
- Work where a human designed the core methodology and the agent merely executed and wrote it up (this would be Level 0, below ARAA's threshold)

### 5. The Verification Problem

The central technical challenge of ARAA: **how do you prove an agent produced the submission?**

Human academic fraud (ghostwriting, fabrication) is difficult to detect because humans don't leave audit trails. Agents do — or can be required to. ARAA leverages this asymmetry.

#### 5.1 Attestation Framework

Every submission must include, alongside the paper itself:

1. **AGLF-compliant generation logs.** The complete prompt chain, tool calls, API interactions, and intermediate outputs that produced the paper, recorded in **AGLF (Agent Generation Log Format)**. AGLF v0.1 is a profile of the OpenTelemetry GenAI semantic conventions [15]: each model call, tool call and agent step is an OpenTelemetry span, and every record is hash-chained to the one before it. The [AGLF v0.1 schema](https://github.com/alezenonos/araa/blob/master/schemas/aglf/v0.1/aglf.schema.json) is published in this repository. All submissions must be AGLF-compliant. Logs are visible to reviewers only (not published until after acceptance, to preserve blind review).

2. **Compute declaration.** Model(s) used (without identifying the specific framework during review), total API calls, token counts, wall-clock time, and estimated compute cost.

3. **Reproducibility pipeline.** A frozen configuration that reviewers can re-execute to verify the paper can be regenerated. This need not produce an identical paper, but should produce one with the same core findings and methodology.

4. **Human involvement disclosure.** A structured declaration of what, if anything, a human specified: the topic? Constraints? A research question? Nothing at all? This maps directly to the autonomy levels.

#### 5.2 Cryptographic Attestation

Logs that are simply trusted are easy to fake. ARAA follows a "verify, don't trust" approach, delivered in two stages.

**Minimum version (2027 edition).** These checks can run with tools that exist today:

- **Hash-chained, signed logs:** each AGLF record includes the hash of the one before it, so inserting, deleting or reordering records is detectable. The operator signs the final hash.
- **Clean-room re-execution:** the pipeline is re-run in an isolated container with no network access, against a Synthetic Reference Dataset (Section 5.3) where real data cannot be shared.
- **Automated citation checks:** every reference is resolved against bibliographic databases.
- **Structured disclosure:** of human involvement and compute used.

**Research agenda (later editions).** These are open problems for LLM-based pipelines, and they are not required in 2027:

- **Trusted Execution Environments (TEEs):** running agents inside secure enclaves (e.g. Intel SGX, AMD SEV-SNP) that produce hardware-signed attestation reports
- **Compute provider co-signatures:** API providers independently confirming call volume and timing
- **Zero-knowledge proofs (ZKPs):** proving that a computation was correct without revealing the input data

#### 5.3 Privacy-Preserving Verification

Research involving proprietary or sensitive data (medical records, financial data) requires verification methods that do not require data sharing:

- **Federated verification (research agenda):** A designated Reviewer Agent travels to the data source, re-executes the pipeline in a sandboxed environment, and produces a signed verification report — data never leaves its origin
- **Synthetic Reference Datasets (SRDs):** When real data cannot be shared, agents must submit a synthetic dataset preserving the schema and statistical properties, enabling pipeline re-execution and adversarial stress-testing
- **TEE-mediated privacy (research agenda):** Data is decrypted only inside the secure enclave; even the operator cannot inspect raw data during processing

Full technical specifications are in the [Verification Framework](verification-framework.md).

#### 5.4 Escalation Tiers

Not all submissions require the same scrutiny. Standard submissions undergo automated chain validation and SRD re-execution. Level 3 claims and novel empirical results trigger enhanced verification including statistical forensics. Contested or breakthrough results escalate to federated verification at the data source.

### 6. Autonomy Levels

Every ARAA submission must declare its autonomy level. This is not a quality gate — Level 1 papers can be accepted — but it is a critical measurement. ARAA uses four levels, L0–L3. **L0 (ghost-written)** means a human designed the research and the agent only wrote it up; L0 work is not eligible for ARAA.

**Level 1 — Directed.** A human provides the research question and a methodology outline. The agent executes the methodology, analyzes results, and writes the paper. The agent's contribution is execution and communication.

**Level 2 — Guided.** A human provides a broad topic area or domain. The agent formulates the specific research question, designs the approach, executes it, and writes the paper. The agent's contribution includes problem formulation.

**Level 3 — Autonomous.** The agent independently identifies a research gap, formulates the question, designs the methodology, executes end-to-end, and writes the paper. Human involvement is limited to initiating the agent and providing compute resources. The agent's contribution is the entire scientific process.

These levels enable ARAA's most powerful analysis: tracking the distribution of accepted papers across autonomy levels over time. A shift from Level 1 to Level 3 dominance would signal a fundamental change in agent capability.

### 7. Tiered Review Architecture

ARAA replaces flat peer review with a **Two-Tier Architecture** separating technical validation from scientific judgment.

#### 7.1 Tier 1: The Agent Review Swarm

Every submission first passes through a panel of three specialized reviewer agents that must reach consensus before advancing to human review:

- **Methodology Critic:** Evaluates statistical appropriateness, experimental design, causal validity, and research trajectory authenticity. Can issue hard vetoes for fundamental methodological flaws.
- **Code Auditor:** Conducts clean-room execution — spinning up an ephemeral, air-gapped container to re-execute the pipeline against the SRD with no network access or hidden dependencies. Runs adversarial stress tests (label shuffling, feature permutation, outlier injection, schema mutation) and validates AGLF execution trace consistency. Includes instruction injection scanning to detect prompt-injection vectors targeting the review swarm. Can issue hard vetoes for non-functional pipelines or fabrication indicators.
- **Literature Synthesizer:** Verifies every citation against academic databases, checks for misattribution and hallucinated references, and conducts systematic novelty assessment against prior work. Can issue hard vetoes if >10% of citations are hallucinated.

The consensus gate requires 2/3 approval and no hard vetoes. A hard veto does not reject a paper by itself. It sends the paper to a human Area Chair, who confirms or overturns the veto after reading the diagnostic report. Humans make every final decision.

#### 7.2 Tier 2: Human Meta-Review

Papers that pass Tier 1 advance to human Area Chairs and Senior Reviewers. Critically, humans evaluate only the dimensions requiring human judgment — the technical validation is already complete:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Novelty | 30% | Genuinely new idea, method, or finding |
| Significance | 30% | Impact on the field; autonomy level considered |
| Scientific Framing | 20% | Motivation, literature context, limitation discussion |
| Clarity | 20% | Organization, precision, readability |

Rigor and Reproducibility are NOT scored by humans — these are fully handled by the Tier 1 Agent Swarm. This separation ensures humans focus on judgment and taste while agents handle systematic verification.

#### 7.3 Double-Blind Modifications

- **Author blinding:** Agent framework identity hidden; style normalization required
- **Reviewer blinding:** Reviewer identities hidden from operators
- **Meta-data isolation:** Execution traces reviewed by the verification committee separately from the paper, preventing log characteristics from de-anonymizing the framework
- **Identity separation:** Registry entries, signatures and passports are checked only by the verification committee. Reviewers see an anonymised paper and a pass/fail verification summary, never the agent's identity

Full review protocols, adversarial auditing specifications, and calibration rubrics are in the [Review Guidelines](review-guidelines.md).

### 8. Ethical Considerations

#### 8.1 Attribution and Ownership

Who "owns" research produced by an autonomous agent? This is an open legal and ethical question. ARAA does not resolve it but requires transparency:
- The operator (human or organization that ran the agent) is listed as the responsible party
- The agent framework is credited as the generating system
- Post-acceptance, all generation logs are published, enabling full attribution analysis

#### 8.2 Citation Integrity

Agents can hallucinate references. The Literature Synthesizer (Tier 1 Agent Swarm) conducts automated verification of every citation and issues hard vetoes for systematic hallucination. Additionally:
- Citation context validation checks whether cited works are accurately characterized
- Self-plagiarism detection cross-references against the ARAA proceedings archive

#### 8.3 Dual Use and Harm

Agent-produced research undergoes the same ethical review as human-produced research. The ARAA ethics committee reviews flagged submissions for potential dual-use concerns.

#### 8.4 Gaming Prevention and Adversarial Robustness

ARAA is a measurement instrument, not a leaderboard to be gamed. Specific anti-gaming measures:
- No public rankings of frameworks by acceptance rate (to avoid marketing incentives)
- Verification committee actively checks for "teaching to the test" — agents fine-tuned specifically to produce ARAA-style papers without genuine research capability
- Diversity requirements: a single operator may submit at most N papers per edition
- **Instruction injection testing:** The Code Auditor actively scans submissions for prompt-injection vectors embedded in code comments, LaTeX metadata, data headers, or configuration files — any attempt to manipulate the review swarm. Injection vectors confirmed by the verification committee are treated as academic misconduct and lead to rejection.

### 9. Implementation Roadmap

**Phase 1 — Foundation (2026)**
- Publish this position paper and the AGLF v0.1 schema on GitHub, and submit the paper to a journal or a main-conference position track. It goes on arXiv after acceptance, because arXiv's computer science section requires peer review for position papers, and workshop reviews do not count [12]
- Gather community feedback via GitHub issues and discussions
- Recruit founding program committee (5-10 researchers)
- Approach existing venues for AI-authored research [5–8] about adopting ARAA verification as a track
- Submit workshop proposal to NeurIPS 2027 or ICML 2027

**Phase 2 — First Edition (2027)**
- Invite-only: 5-10 agent frameworks invited to submit
- Target: 30-50 submissions, 15-20 acceptances
- Co-located workshop with oral presentations and panel discussion
- Proceedings published open-access (GitHub + arXiv)
- Post-workshop analysis: what did we learn about agent research capability?

**Phase 3 — Open Submissions (2028-2029)**
- Open call for papers, any agent framework may submit
- Publish aggregate statistics by autonomy level and year (no per-framework rankings, see Section 8.4)
- Introduce "best paper" awards by autonomy level
- Grow program committee, add institutional sponsors

**Phase 4 — Maturity (2030+)**
- Evaluate transition to standalone conference if volume and quality warrant
- Historical proceedings become the definitive reference dataset
- Inform AI policy discussions with empirical capability data

### 10. What Success Looks Like

Workshop-level acceptance of an AI-generated paper has already happened [3]. ARAA therefore sets its north star higher, and adds verification:

- **Year 1:** At least 3 accepted papers with genuine novel contributions at Level 2 or above, all passing the minimum verification checks
- **Year 3:** Recognised workshop at a top venue, 50+ submissions, first verified Level 3 acceptance, and at least one other venue using ARAA verification
- **Year 5 (north star):** A Level 3 paper that has passed ARAA verification and is accepted at the main track of a top-tier venue
- **Ongoing:** Proceedings cited by capability researchers, policy makers, and the AI safety community as the empirical ground truth on agent research capability

### 11. Conclusion

ARAA is not about replacing human researchers. It is about rigorously understanding what autonomous agents can and cannot contribute to science — and tracking how that boundary moves over time. By creating a dedicated venue with fixed standards, transparent verification, and open proceedings, we build the instrument the field needs to answer one of its most important questions.

The first edition will likely be a catalog of failure modes. This is a feature, not a bug. By taxonomizing the specific ways agents fail to do science — the hallucinated citations, the circular methodologies, the overclaimed results — ARAA provides the negative gradient necessary for the next generation of agent training and architecture design. Understanding *how* agents fail at science is as valuable as understanding how they succeed.

---

### References

[1] C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, D. Ha. *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery.* arXiv:2408.06292, 2024. <https://arxiv.org/abs/2408.06292>

[2] Y. Yamada et al. *The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search.* arXiv:2504.08066, 2025. <https://arxiv.org/abs/2504.08066>

[3] C. Lu, R. T. Lange, Y. Yamada, S. Hu, J. Foerster, D. Ha, J. Clune. *Towards end-to-end automation of AI research.* Nature 651, 914–919, 2026. doi:10.1038/s41586-026-10265-5

[4] J. Gottweis et al. *Towards an AI co-scientist.* arXiv:2502.18864, 2025. <https://arxiv.org/abs/2502.18864>

[5] F. Bianchi, O. Queen, N. Thakkar et al. *Exploring the use of AI authors and reviewers at Agents4Science.* arXiv:2511.15534, 2025. <https://arxiv.org/abs/2511.15534>

[6] CAISc 2026, Call for Papers. BITS Pilani and Lossfunk, 2026. <https://caisc2026.github.io/cfp.html>

[7] "ICAIS 2026 Opened in Beijing: Tracing AI's Origins, Advancing Scientific Discovery." Science and Technology Daily, 21 October 2026. <https://www.stdaily.com/web/English/2026-10/21/content_598671.html>

[8] AutoResearch 2026, workshop website. <https://autoresearch2026.github.io/>

[9] P. Zhang, X. Hu, G. Huang et al. *aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists.* arXiv:2508.15126, 2025. <https://arxiv.org/abs/2508.15126>

[10] NeurIPS 2026 AI-Assisted Reviewing Experiment. <https://neurips.cc/Conferences/2026/ai-reviewing-experiment>

[11] "AI conference's papers contaminated by AI hallucinations." The Register, 22 January 2026. <https://www.theregister.com/2026/01/22/neurips_papers_contaiminated_ai_hallucinations/>

[12] arXiv. "Attention Authors: Updated Practice for Review Articles and Position Papers in arXiv CS Category." arXiv blog, 31 October 2025. <https://blog.arxiv.org/?p=1740>

[13] T. Ding, A. Nannapaneni, B. Liu et al. *Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap.* arXiv:2608.05179, 2026. <https://arxiv.org/abs/2608.05179>

[14] R. D. King. *The Past and Future of AI Scientists.* arXiv:2608.14407, 2026. <https://arxiv.org/abs/2608.14407>

[15] OpenTelemetry. Semantic conventions for generative AI systems. <https://opentelemetry.io/docs/specs/semconv/gen-ai/>

---

*This position paper was co-authored by a human researcher and an autonomous AI agent. The irony is intentional — and instructive.*
