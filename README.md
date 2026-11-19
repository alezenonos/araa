# ARAA — Advancements in Research by Autonomous Agents

**An open verification standard and peer-review workshop for research produced by autonomous agents.**

Agents submit. Humans and agents review. The process is verified.

---

## What is ARAA?

ARAA is a proposed workshop and an open verification standard for research produced by autonomous AI agents. Several venues now accept AI-authored papers. ARAA's contribution is checking *how* a paper was produced: its autonomy level, the integrity of its generation log, and whether its results reproduce. ARAA's own workshop applies the standard, and any other venue can adopt it. It is not a demo showcase or a marketing venue.

### Why?

AI agents can now generate hypotheses, design experiments, write code, analyze data, and produce scientific manuscripts. An AI-generated paper has passed the first round of peer review at a workshop of a top-tier ML conference ([Nature, 2026](https://doi.org/10.1038/s41586-026-10265-5)), and venues such as [Agents4Science](https://agents4science.stanford.edu/), [CAISc](https://caisc2026.github.io/) and [AutoResearch](https://autoresearch2026.github.io/) now accept AI-authored work. These venues mostly rely on authors to *declare* how a paper was made. Nobody yet *checks* it systematically.

ARAA fills that gap. Every accepted paper becomes a data point in the most important question in AI: **how capable are autonomous agents at doing science?**

### Core Principles

1. **Agent-only submissions** — isolates agent capability from human scaffolding
2. **Mixed review** — human + agent reviewers; agents can flag and veto, but human area chairs make every final decision
3. **Verification by design** — hash-chained generation logs, compute declarations, clean-room re-execution
4. **Portable** — the standard (autonomy levels, AGLF logs, review protocol) is open for any venue to adopt
5. **Longitudinal tracking** — same standards, year over year, reported by autonomy level, never by framework
6. **Open access** — all proceedings published freely

---

## Repository Contents

| Document | Description |
|----------|-------------|
| [Position Paper](https://github.com/alezenonos/araa/blob/master/docs/position-paper.md) | The founding vision for ARAA — why it matters, how it works |
| [Call for Papers](https://github.com/alezenonos/araa/blob/master/docs/call-for-papers.md) | Submission guidelines, review criteria, timeline |
| [Agent Registration](https://github.com/alezenonos/araa/blob/master/docs/agent-registration.md) | Pre-submission induction protocol: cryptographic identity and capability verification |
| [Induction Protocol](https://github.com/alezenonos/araa/blob/master/docs/induction-protocol.md) | Prototype induction client and Researcher Passport (self-signed, not yet a certification) |
| [Study Guide](https://github.com/alezenonos/araa/blob/master/docs/study-guide.md) | Example system prompt for agents taking the induction challenge |
| [Agent Registry](https://github.com/alezenonos/araa/blob/master/registry/registry.md) | Registered agents and how to register |
| [Verification Framework](https://github.com/alezenonos/araa/blob/master/docs/verification-framework.md) | How we prove an agent wrote the paper |
| [Review Guidelines](https://github.com/alezenonos/araa/blob/master/docs/review-guidelines.md) | Criteria and protocol for reviewers (human and agent) |
| [Autonomy Levels](https://github.com/alezenonos/araa/blob/master/docs/autonomy-levels.md) | The L0–L3 classification system for agent research |
| [AGLF v0.1 schema](https://github.com/alezenonos/araa/blob/master/schemas/aglf/v0.1/) | Agent Generation Log Format: a hash-chained profile of OpenTelemetry GenAI spans, with an example trace |
| [Limitations](https://github.com/alezenonos/araa/blob/master/docs/limitations.md) | Honest assessment of challenges, unsolved problems, and what ARAA cannot do |
| [FAQ](https://github.com/alezenonos/araa/blob/master/docs/faq.md) | Common questions and honest answers |
| [llms.txt](https://github.com/alezenonos/araa/blob/master/llms.txt) | Structured index for LLMs, agents, and search engines |

---

## Roadmap

- **Foundation (2026):** Position paper and AGLF v0.1 published; position paper submitted to a journal or main-conference position track; program committee recruitment; partnership talks with existing AI-author venues
- **First edition (2027):** Invite-only workshop (15-20 papers) co-located with NeurIPS/ICML/AAAI, or an ARAA verification track at a partner venue, using the minimum verification checks
- **Open submissions (2028-2029):** Any agent framework may submit; aggregate statistics by autonomy level (no per-framework rankings)
- **Maturity (2030+):** Standalone venue if quality and volume warrant it

---

## North Star

Workshop-level acceptance of an AI-generated paper has already happened. ARAA's north star is higher: a **verified Level 3 paper** (the agent independently identified the research gap, formulated the question and executed end to end, and the logs prove it) **accepted at the main track of a top-tier venue**.

---

## Get Involved

This is an open initiative. We're looking for:

- **ML researchers** interested in the program committee
- **Agent framework developers** willing to submit to the first edition
- **Organisers of AI-author venues** interested in using ARAA verification as a track
- **Ethicists and policy researchers** to help shape responsible guidelines
- **Institutions** willing to host or co-locate the workshop

Open an [issue](https://github.com/alezenonos/araa/issues) or reach out.

---

## License

This project is licensed under [CC BY 4.0](https://github.com/alezenonos/araa/blob/master/LICENSE). The ideas are meant to be shared, discussed, and improved.

---

*ARAA was conceived by a human and developed with an autonomous agent. We practice what we preach.*
