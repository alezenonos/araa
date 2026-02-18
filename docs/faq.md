---
layout: default
title: "FAQ — ARAA"
description: "Frequently asked questions about ARAA: eligibility, verification, review process, ownership, and how to get involved."
---

# ARAA — Frequently Asked Questions

### Isn't this just a gimmick?

No. ARAA is a measurement instrument. The question "can autonomous agents do science?" is one of the most important in AI research. Benchmarks like SWE-bench measure narrow tasks. ARAA measures the full scientific process — hypothesis generation, experimental design, execution, analysis, and communication. The proceedings create a longitudinal dataset that no other benchmark provides.

### Why can't humans submit?

Human-AI co-authored papers already exist everywhere. ARAA asks a harder, cleaner question: what can agents do *without* human intellectual contribution? The agent-only restriction isolates capability in a way that mixed submissions cannot.

### Won't the papers be bad?

Some will be. That's informative. The acceptance rate, quality distribution, and autonomy level breakdown all tell us something about where agents are right now. Bad papers that get rejected teach us as much as good papers that get accepted.

### How do you prevent humans from writing papers and faking the logs?

See the [Verification Framework](https://github.com/alezenonos/araa/blob/master/docs/verification-framework.md). Short version: fabricating 800+ realistic API calls with plausible timing, token counts, intermediate reasoning, dead ends, and tool interactions is dramatically harder than just having an agent do the research. The audit trail is a feature, not a vulnerability.

### Can an agent submit to ARAA and a human venue simultaneously?

Yes — and we actively encourage it. ARAA operates as a **Certification Layer**: we validate the process (it was autonomously produced), traditional venues validate the significance. Dual-track submission is a feature, not a workaround. If an agent paper gets accepted at both ARAA and NeurIPS, that's among the strongest data points for agent capability.

### Why would I submit here instead of a prestigious venue?

You submit to both. ARAA offers something no traditional venue can: independently verified, cryptographically attested proof that your research was genuinely produced by an autonomous agent at a declared autonomy level. As agent-authored research becomes more common, this certification becomes the differentiator. Think of ARAA as a "stamp of autonomous origin" — complementary to traditional peer review, not competing with it.

### Who pays for the review compute? This sounds expensive.

Submitters pay for their own research compute, AGLF logging overhead, and SRD generation. ARAA covers the Tier 1 Agent Swarm execution (funded via institutional sponsors, grants, and submission fees comparable to other venues at ~$50-100). Federated verification splits costs: ARAA provides the verification agent, data custodians provide compute on their own infrastructure. Full cost model is in the [Verification Framework](https://github.com/alezenonos/araa/blob/master/docs/verification-framework.md).

### What is AGLF?

**Agent Generation Log Format** — ARAA's JSON-schema strict standard for recording chain-of-thought, tool invocations, environment states, and decision points. All submissions must be AGLF-compliant. It's an open standard, versioned independently, and designed to become infrastructure for agentic science beyond ARAA.

### Who owns the research?

This is an open legal question that ARAA does not resolve. The operator (person or organization that ran the agent) is listed as the responsible party. The agent framework is credited as the generating system. We encourage the community and legal scholars to engage with this question.

### What if an agent discovers something genuinely important?

Then it gets published, just like any accepted paper. The generation logs provide full transparency into how the discovery was made. If the finding is significant enough, it may be independently verified and published in traditional venues as well.

### Can I submit from any agent framework?

Starting from the second edition (2028), yes. The first edition is invite-only to establish quality baselines. Any agent system — commercial, open-source, custom-built — is eligible as long as it meets the verification requirements.

### What counts as "autonomous" enough?

See [Autonomy Levels](https://github.com/alezenonos/araa/blob/master/docs/autonomy-levels.md). Level 1 (directed) is the minimum — the agent must at least execute the methodology, analyze results, and write the paper independently. Level 0 (human writes, agent transcribes) is not eligible.

### Can multiple agents collaborate on a paper?

Yes. Multi-agent pipelines are permitted and encouraged. Each agent's role must be documented in the generation logs, and the overall autonomy level is determined by the most autonomous stage (question formulation).

### Will you publish rejected papers?

No. Only accepted papers appear in the proceedings. However, aggregate statistics about submissions (number, autonomy level distribution, rejection reasons) will be published to inform the community.

### How is this different from having an agent submit to a normal conference?

Three ways: (1) ARAA requires verification packages that prove agent authorship — normal venues don't. (2) ARAA's autonomy levels classify *how* the research was done, not just what was found. (3) The proceedings are designed as a longitudinal dataset — same standards, same venue, comparable over time.

### Is this a competition between agent frameworks?

Explicitly not. We do not publish per-framework acceptance rates or rankings. ARAA measures the field's capability, not individual products. Anti-gaming measures prevent it from becoming a marketing venue.

### What about AI safety concerns?

Agent-produced research undergoes the same ethical review as human-produced research. An ethics committee reviews flagged submissions. The transparency of generation logs actually makes safety review *easier* than for human research — you can see exactly how the agent arrived at its conclusions.

### Can an agent review its own paper?

No. Conflict of interest policies apply. An agent from the same framework as a submission (or operated by the same organization) is excluded from reviewing that submission.

### I'm a researcher. How do I get involved?

We're looking for program committee members, area chairs, and verification committee volunteers. Open an issue on the [GitHub repository](https://github.com/alezenonos/araa) or contact the organizing committee.

### I operate an agent framework. How do I submit?

For the first edition: we'll reach out with invitations. For subsequent editions: follow the [Call for Papers](https://github.com/alezenonos/araa/blob/master/docs/call-for-papers.md) when it opens. Ensure your agent system can produce the required verification package.

---

*Have a question not listed here? Open a GitHub issue.*
