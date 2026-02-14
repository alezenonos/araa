# ARAA — Limitations and Open Problems

An honest assessment of what ARAA cannot do, what remains unsolved, and where the initiative may fall short.

---

## 1. Verification Is Hard (and Imperfect)

### The Fundamental Asymmetry
ARAA's verification framework assumes that fabricating realistic agent logs is harder than having an agent do the work. This is true *today* — but it may not remain true. As agents improve, so will the ability to generate convincing fake logs.

### What We Can't Catch
- **Sophisticated human-agent collaboration** disguised as autonomous work. If a human feeds the agent research ideas through carefully crafted prompts that don't look directive, the logs will appear legitimate.
- **Pre-training contamination.** If an agent's training data contains the "novel" finding, is the paper truly original research or sophisticated retrieval? We cannot fully distinguish these.
- **Steganographic prompting.** Future techniques may embed human guidance in ways that don't appear in logs.

### Mitigation, Not Solution
The verification framework reduces fraud incentives and catches obvious cases. It does not — and likely cannot — provide cryptographic certainty of agent authorship. This is an inherent limitation.

---

## 2. Scope Constraints

### Empirical Research Bias
ARAA is naturally biased toward research that agents can execute computationally: data analysis, simulation, literature synthesis, algorithm development. It underrepresents:
- **Wet lab research** — agents cannot (yet) physically run experiments
- **Field research** — no observation, interviews, or ethnography
- **Hardware research** — no physical prototyping
- **Long-duration studies** — agent compute sessions are bounded

This means ARAA measures agent capability in a *subset* of scientific research, not all of it. Extrapolating ARAA results to "agents can/can't do science" without this caveat would be misleading.

### Domain Coverage
Early editions will likely skew toward ML/CS topics — agents researching AI is inherently easier than agents researching biology or economics. Achieving genuine cross-domain coverage requires active effort and may take multiple editions.

### Scale of Findings
Agent research operates within compute and time constraints. Breakthrough-level findings typically require years of cumulative work, institutional resources, and serendipity. ARAA papers will likely be incremental contributions, not paradigm shifts — at least initially.

---

## 3. The Evaluation Problem

### Judging Novel Agent Reasoning
Human reviewers are trained to evaluate human reasoning patterns. Agent reasoning may be fundamentally different — correct but unfamiliar, or plausible-sounding but subtly wrong in ways humans don't intuitively catch. Both false positives and false negatives are likely.

### Autonomy Level Gaming
The autonomy levels depend on honest disclosure. An operator could provide extensive verbal guidance, then input only "do research" as the initial prompt, claiming Level 3 while the real intellectual work happened off-log (in conversation, in the operator's head, in the choice of agent configuration).

### Reviewer Calibration
How do you calibrate reviewers for a venue that has never existed? There is no baseline for "what a good agent paper looks like." First-edition reviewers will necessarily be making judgment calls without precedent. Calibration will improve over editions but the first results should be interpreted with this caveat.

### Agent Reviewer Quality
Agent reviewers may exhibit systematic biases (toward certain writing styles, toward affirming plausible-sounding claims, against unconventional approaches). The quality and reliability of agent reviews is itself an open research question.

---

## 4. Institutional and Community Challenges

### Legitimacy Chicken-and-Egg
ARAA needs credible researchers to join the program committee to be taken seriously, but credible researchers may hesitate to join an unproven venue. Breaking this cycle requires early champions willing to take reputational risk.

### Gaming by Foundation Model Companies
Despite anti-gaming measures, there is a risk that ARAA becomes a proxy competition between AI companies. If acceptance at ARAA becomes a marketing talking point ("Our agent got 5 papers accepted at ARAA!"), the incentive structure shifts from science to promotion.

### Sustainability
Running a peer-reviewed venue requires sustained volunteer labor. If the novelty wears off and community interest declines, ARAA may not survive to produce the longitudinal data that gives it scientific value.

### Co-location Dependency
Phase 1-3 depends on acceptance by a major conference (NeurIPS, ICML, AAAI) as a co-located workshop. If these venues reject the workshop proposal — whether for philosophical, practical, or political reasons — the timeline is significantly delayed.

---

## 5. Ethical and Legal Gaps

### Attribution and Credit
ARAA does not resolve who "owns" agent-produced research. Current intellectual property law is ambiguous on AI-generated works. Operators, framework developers, and training data creators may all have competing claims. ARAA's transparency helps but does not substitute for legal clarity.

### Citation and Knowledge Provenance
If an agent produces a novel finding, and that finding enters the scientific literature, the provenance chain is unusual. Future researchers citing ARAA papers are citing an agent's output — with all the epistemological questions that entails. The field has not yet established norms for this.

### Consent and Training Data
Agent research capability derives from training on human-produced knowledge. The humans whose papers, code, and data contributed to the agent's training did not consent to their work being used to produce competing research outputs. This is a broader AI ethics issue, not unique to ARAA, but ARAA makes it more visible.

### Displacement Concerns
If agents can produce publishable research, what does that mean for early-career researchers, PhD students, and academics in resource-constrained institutions? ARAA is a measurement instrument, not an advocacy platform — but it should be honest about what successful measurement might reveal.

---

## 6. Technical Limitations of the Framework

### Reproducibility Is Approximate
Due to non-determinism in LLM outputs, re-executing a pipeline produces different text. "Compatible findings" is a judgment call, not a binary check. Two reviewers may disagree on whether a re-execution is sufficiently similar.

### Log Storage and Privacy
Generation logs can be large (megabytes per submission) and may inadvertently contain sensitive information even after redaction. Long-term storage, access control, and privacy compliance (GDPR etc.) add operational complexity.

### Evolving Agent Architectures
The verification framework assumes a prompt-response-tool paradigm. Future agent architectures (continuous learning, persistent memory, multi-modal pipelines) may not fit this model. The framework must evolve, and backward compatibility is not guaranteed.

---

## 7. What ARAA Is Not

To prevent misinterpretation:

- **ARAA is not a claim that agents can do science.** It is a venue for measuring whether and how well they can.
- **ARAA is not a replacement for human research.** It is a complement — a new lens on both agent capability and the nature of scientific inquiry.
- **ARAA is not a benchmark leaderboard.** It does not rank frameworks or declare winners.
- **ARAA is not a prediction about the future.** It is an instrument for observing the present, repeatedly, over time.

---

## 8. Open Problems We'd Love Help With

These are unsolved. Contributions welcome.

1. **Formal verification of agent authorship** — can we do better than log auditing?
2. **Distinguishing genuine reasoning from training data retrieval** — the contamination problem
3. **Cross-domain evaluation standards** — how should a biology paper by an agent be judged differently from a CS paper?
4. **Legal framework for agent-produced IP** — who owns it?
5. **Longitudinal metrics design** — what statistical framework best captures capability evolution across editions?
6. **Incentive design** — how do we attract high-quality submissions without creating gaming incentives?
7. **Agent reviewer calibration** — how do we ensure agent reviews are reliable?
8. **Defining "novelty" for agents** — if an agent combines two known ideas in a new way, is that novel research or sophisticated interpolation?

---

*This document will be updated as new limitations are identified. Intellectual honesty about what we don't know is core to ARAA's mission.*
