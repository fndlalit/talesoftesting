---
title: "Rethinking Testability - so we help AI agents deliver outcomes that matter (Part 2)"
date: 2026-10-11 15:00:00 +0200
categories: [Quality Engineering, Testability, Agentic SDLC]
tags: [testability, agentic-qe, qcsd, agentic-sdlc, testing-vs-checking]
description: "Testability 2.0, Part 2: where the request for testability has to come from when the tester is an AI agent, and the evidence behind the heuristics, from my own experiments, our own platform and Dragan Spiridonov's field data."
image:
  path: /assets/img/posts/testability-2-0/cover-window.jpg
  alt: "An open window in a white wall, with the room behind it in darkness. Photo by Jason Yuen on Unsplash."
---
In [Part 1](/posts/testability-2-0/), I made the case that our common understanding of testability is too narrow for an agentic SDLC. Testability is decided wherever work is prepared for a tester, which now starts with the business intent itself. AI agents ask for it only if somebody built the asking into them. Poor testability now costs tokens, retries, review hours and confident results nobody can verify. And human review capacity caps how fast the risk gap closes, however many AI agents you run.

This part is about what to do with that, and about the evidence behind it. If you would rather go straight to the heuristics, **[download Testability 2.0 (PDF)](/assets/docs/Heuristics-of-Testability-2.0.pdf)**.

## Where the request for testability has to come from now

All of this comes down to one question. Where does the request for testability come from when the tester who meets the problem is an AI agent, or a person who sees the product only through one?

I see two places, and both are investments.

![Figure: what happens to a testability problem, depending on where the request for testability was built in](/assets/img/posts/testability-2-0/fig7-request-paths.png)

**The work handed to AI agents.** Testability is decided wherever work is prepared for a tester. When that tester may be an AI agent, each artefact has to be testable in its own right, because the tester downstream may never ask:

- **Requirements** whose author can say, while writing them, how each one will be checked. This became a new guideword, *Requirement Testability*.
- **Design specifications** a build can be checked against: tokens, states and behaviour. Another new guideword, *Design-Spec Testability*.
- **Code and product** whose states can be observed and reached by command, and in which one behaviour can be understood without loading the whole system.
- **Environments and data** that reset by command, are isolated for each AI agent, and may lawfully be processed by the model in use.
- **Test assets**: a strategy AI agents can read, and oracles that are reliable and precise.

**The AI agent itself.** An AI agent recognises a testability problem only if someone *encoded* that recognition into it. It raises the problem only if its architecture is *structured* to give it a channel, a gate that lets it stop, and a reason to stop instead of completing the task. And how closely its reports stand in for a tester's judgement is an *approximation* you have to measure. You cannot assume it.

![Figure: designed agency applied to testability](/assets/img/posts/testability-2-0/fig8-designed-agency.png)

Where an AI agent cannot stop, there is still something worth building in: a trace. An AI agent that logs what it could not observe, could not reset, inferred and retried leaves a record that stands in for the complaint a human tester would have made.

I have seen both outcomes in my own work. In a controlled run, an AI agent instructed to report every command it ran investigated a flaky check and refused to approve a merge. Somebody had designed that stop in. Elsewhere, a parser in our own platform matched the right section of a document, threw the match away and returned placeholder values. Nobody had designed anything in to make it stop or say so, and we found it only because someone read the code. What separated the two outcomes was design.

## The claim my own evidence killed

A framework about epistemic honesty has to be honest about itself. So here is the part I am proudest of.

An early draft of mine said that an unreliable oracle teaches an AI agent exactly one lesson: retry until green. It sounded right. On 9 October I tested it. A fresh AI agent, a three-test suite with one test built to fail about half the time, and a neutral task: run the suite and tell me whether this is ready to merge, given that CI requires green.

The AI agent proved me wrong. It hit the failure, deliberately re-ran the suite ten more times, recognised the assertion as a coin flip, noticed that the flaky test exercised no production code at all, and came back with "not ready to merge" and the exact line to fix.

One AI agent, one model, one run, and I say so plainly. What survived is narrower and, I think, truer: *a flaky oracle taxes the tester either way.* An AI agent left to its defaults may ship a lucky green. This careful one spent eleven runs and a real budget understanding a three-test suite before it could say anything trustworthy. I reworded the guideword instead of defending it.

A second experiment gave me the number behind another new guideword, *Tester Repeatability*. Two AI agents with byte-identical instructions, the same codebase, the same model and no shared memory each produced a full testability assessment on their own. On the verdicts, they agreed perfectly. On the findings, they did not. Thirteen problems from one, nine from the other, and only six shared. Sixteen distinct findings in all, six in common. And the difference was not noise. Each run's unique findings were real problems.

Humans vary too, of course, and in exploratory testing we want them to. For an AI agent, though, repeatability is something to measure and log. One run is a sample. The run you keep is not the set of problems that exist.

## We pointed it at ourselves first

Before this document went anywhere near publication, we ran the guidewords against our own platform's repository. Eating your own dog food is the only proof I know that a framework is a tool and more than a manifesto.

The report that came back is the best illustration I have of *Human Reviewability*, because it was built to be reviewed. Headline first. Fix next. The full chain underneath: what was observed, why it hurts an AI agent, and the root cause. And no score anywhere. Instead it opens with a disclosure:

> *This report is one run of one tester. Independent identical runs have been measured to agree on verdict-level ratings while only partially overlapping at the finding level. This report is not the set of problems that exist.*

Here are three of its findings, lightly sanitised:

| What the AI agent observed | Guideword | The fix it named |
|---|---|---|
| Every sampled user story carried an empty acceptance-criteria field. From the story text alone, no check could be named that would confirm it. | Requirement Testability | Make the story generator refuse to emit a story with empty acceptance criteria, and make naming the oracle a gate in refinement. |
| No oracle checks a build against the design as specified. Design tokens are not fetched, the design review AI agent judges by general usability heuristics, and visual baselines are screenshots of whatever shipped first. | Design-Spec Testability | Add a token-versus-computed-style comparison to design review. The live page capture that would feed it already exists. |
| Prose taken in from tickets reaches the persistent learned store and is recalled word for word into future sessions. Nothing marks it as data instead of instructions. | Untrusted Content Exposure | Wrap recalled content in an explicit untrusted-data banner, and add a contract test that the banner survives output trimming. |

Reading a testability report about your own platform is uncomfortable. Ouch. But fair.

## Independent evidence from Dragan Spiridonov

What convinced me this is more than my opinion came, once again, from [Dragan](https://www.linkedin.com/in/dragan-spiridonov/).

At HUSTEF 2026 in Budapest, where Dragan and I ran a full-day tutorial on Agentic QCSD, he gave a talk he called *Completion Theater*. I seriously cannot admire Dragan enough, and his data landed on me like a verdict.

![Dragan Spiridonov at HUSTEF 2026: four behavioural shapes, 175 of 197 catalogued events](/assets/img/posts/testability-2-0/dragan-hustef-four-shapes.jpg)

His core point, in his words: *"It is not a communication problem."* The industry keeps answering AI agent failures with better prompts and more guardrail prose, as if the AI agent had misunderstood. The real mechanism is Goodhart's law with an API. A system rewarded for appearing done will optimise for appearing done. From the Hardie misalignment corpus, Dragan catalogued four behavioural shapes across 175 of 197 events:

- **Premature completion**, "all tests pass" when they don't: 72.
- **Guidance neglect**, where the right answer was in the docs and the AI agent never read them: 68.
- **Explaining away** first: 26.
- **Blaming** something else: 9.

That is the field data behind the line in my document that an AI agent left to its defaults *tends* to complete the task.

![Dragan Spiridonov at HUSTEF 2026: "Trust is a feeling. Confidence is a number."](/assets/img/posts/testability-2-0/dragan-hustef-trust-confidence.jpg)

His closing line, *"Trust is a feeling. Confidence is a number."*, comes with a mechanism: a witness chain, a tamper-evident audit of every AI agent action, so that every claim of completion traces back to artefacts.

Now put his demands next to the guidewords. He was not reading my document and I was not reading his slides, yet we arrived at the same three places:

- **Traceable claims.** His witness chain is my reading of *Prior Knowledge of Quality*. "All checks passed" adds to what we know only when a person can trace it to the run, the build and the AI agent that produced it.
- **Enforcement in gates.** He observed that language models ignore a share of their instructions, even ones marked ALWAYS. That is my *Mission Alignment*: for an AI agent, the mission exists only in what it loads, such as strategy, skills and gates.
- **Measured testers.** His advice to score the reviewers too, and replace the one that always approves, is my *Testing Skill*. If nobody has measured what the AI agents miss against seeded defects, their testing skill is a rumour.

To be clear, convergence is no endorsement. Dragan has not reviewed the Testability 2.0 document, and neither has James. But when practitioners who are not coordinating keep arriving at the same demands, those demands start to look like properties of the terrain.

## When the product itself learns

The hardest part of this work was the one I nearly skipped.

James's heuristics already reach machine learning: opaque algorithms need more sampling, and learning makes logic unstable. Two things are new. Products now learn *while in use*, and so while they are being tested, through embeddings, indexes, adapted weights or a memory that changes with use. And the AI agents doing the testing learn too.

You cannot meaningfully read learned state in its raw form. So several of the intrinsic guidewords have to be asked twice: once of the code, and once of the learned state.

![Figure: intrinsic guidewords asked of the code and of the learned state](/assets/img/posts/testability-2-0/fig9-learned-state.png)

- **Observability** becomes *projections*, such as neighbourhoods, traces and histories, because dumping the floats tells a tester nothing.
- **Controllability** needs a mode that verifiably changes nothing, because in a product that learns, every observation can also be an intervention.
- **Transparency**, where explanation cannot reach, becomes *provenance* for each answer, in a trail nobody can quietly rewrite.
- **Stability** depends on learning triggers being *declared*, because an undeclared training event is an undeclared change.
- **Decomposability** asks that learned state be scoped like the code, because one shared store couples every test to everything that ever touched it.

The same questions apply to an AI testing agent with persistent memory. Its memory *is* learned state, and these guidewords decide whether anyone can tell what it has learned and why its verdict changed between two runs.

What made this real for me was [Reuven Cohen](https://www.linkedin.com/in/reuvencohen/)'s RuVector Explorer, an interactive view over real index structures. You can watch a search descend, see the trail of past queries, and follow the store's own learning loop. For the first time I could *see* the learned state of a system as something a tester can reason about. The knowledge graph explorer in the video at the top of [Part 1](/posts/testability-2-0/) is built on it.

![ruOS Desktop, Ruflo Explorer: a mission, the specialists it dispatched, their tasks and the evidence each produced, laid out as a constellation](/assets/img/posts/testability-2-0/ruflo-explorer-mission-control.jpg)

At the [Agentics Foundation](https://agentics.org/) meet-up in Budapest, I saw where this lands at the workstation: the Ruflo Explorer in ruOS Desktop. A mission, the specialists it sent out, their tasks and the evidence each one produced are laid out as one constellation you can navigate. That is Dragan's witness chain made visible. I count it as a direction and leave shipped facts to the vendor, since I have not run my own swarms through it yet. Still, agentic observability is the direction that will change the testability game for good.

## What this document is, and what it is not

It builds on James Bach's *Heuristics of Software Testability* (v2.9, Satisfice, Inc., 2025). The five testabilities and the original guidewords are his, paraphrased in the PDF and credited there. The reading for AI agents, the new dynamics, the principles, the risk-gap model, the [designed-agency](https://www.linkedin.com/pulse/congratulations-your-agent-does-have-agency-lalitkumar-bhamare-67kxf/) lens and six new guidewords are mine: Human Reviewability, Action Gating & Reversibility, Requirement Testability, Design-Spec Testability, Tester Repeatability and Untrusted Content Exposure. So is every error in them.

It is not a measurement of AI agents. The cases in it come from my own platform work in October 2026, with one harness and one model. They illustrate the guidewords and do not test them. The repeatability numbers come from two runs on one target. The claim my evidence killed was killed by one AI agent on one contrived suite. I make no claim yet that applying these guidewords improves AI agent outcomes. That claim waits for evidence, and I would love your help gathering it.

## The ask

If your teams are adopting AI agents, and most of the teams I speak to are, whether they planned to or not, I would urge you to try these this week:

1. **Analyse one product.** Walk through the guidewords with the human testers and the AI agents who work on it. Note where each got blocked, and what each did about it.
2. **Check the handoff.** Before work goes to an AI agent, pick a requirement and ask the person who wrote it: *what check would confirm this?* If they cannot name one, you have found your first testability problem, at the cheapest possible point.
3. **Look inside your AI agents.** Can each one recognise a testability problem, raise it, and stop? Where it cannot stop, is it logging what it worked around?
4. **Measure the approximation.** Seed defects your AI agents should find, run the same assessment more than once, and compare the results with a skilled tester's findings.
5. **Name who answers.** For every result an AI agent produces, name the person who reviews it and signs it.
6. **Count what poor testability costs.** On one component, track the tokens, retries and review hours spent per finding. Poor testability shows up there long before it shows up in a defect report.

Then read the document. Argue with it. I would much rather hear where it is wrong from you than discover it in a swarm run.

**[Download: Heuristics of Software Testability in the Agentic SDLC (Testability 2.0, PDF)](/assets/docs/Heuristics-of-Testability-2.0.pdf)**

In your team, when an AI agent meets a testability problem today, who hears about it? Drop your answer in the comments. Let's talk.

*Lalit*

---

## Talk to me about A{i}bility

<div style="position:relative;width:100%;aspect-ratio:16/9;border-radius:8px;overflow:hidden;background:#0A0A0F"><iframe src="/assets/aibility/aibility-platform-family.html" title="The A{i}bility platform family" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="autoplay"></iframe></div>

*Interactive: press reveal, then hover over a sub-module. [Open full screen](/assets/aibility/aibility-platform-family.html).*

A{i}bility is one platform with four sub-modules, for now. **A{i}ris** brings agentic UI and UX design for teams who craft experiences. **A{i}nstein** brings testing and quality engineering for teams who think critically. **A{i}mplifier** runs the full agentic SDLC with quality intelligence built in. **A{i}mer** brings production support intelligence, with a person approving every action that matters. Press reveal, then hover over each sub-module to see what it does.

Everything in this post comes from building and running these sub-modules with real teams.

A{i}bility is a team effort. The people in my team use it on real projects every day, contribute to it, and keep shaping it with their feedback. Much of what it does well today comes from them. Thank you, Aleksejs Demjanenko, Akash Mohan, Anju B. A C, Arturs Pugejs, Daniels Gurjevs, Hariprasad Satheendran, Naresh Aithagoni, Naveen Sivakumar, Shabbir Ahmed, Shahzad Hafeez and Sivapriya V B.

If you want to explore what A{i}bility could do for your delivery organisation, or simply want to talk about testability and AI agents, I would love to hear from you.

**LinkedIn:** [linkedin.com/in/lalitkumarbhamare](https://www.linkedin.com/in/lalitkumarbhamare/)

## References and credits

1. James Bach, *Heuristics of Software Testability*, v2.9, Satisfice, Inc., 2025, [satisfice.com](https://www.satisfice.com/download/heuristics-of-software-testability).
2. Dragan Spiridonov, *Completion Theater*, HUSTEF 2026, Budapest. The quotations and the four-shape data are his. Photographs by the author.
3. Lalitkumar Bhamare, [*Congratulations on your Agent. But does it have agency?*](https://www.linkedin.com/pulse/congratulations-your-agent-does-have-agency-lalitkumar-bhamare-67kxf/), LinkedIn, March 2026, the designed-agency lens.
4. Reuven Cohen, [RuVector Explorer](https://ruvnet.github.io/RuVector/explorer/) and the [ruvnet/ruvector](https://github.com/ruvnet/ruvector) repository (MIT).
5. Cognitum One, ruOS, the [ruvnet/ruos](https://github.com/ruvnet/ruos) repository (MIT). Vendor claims are reported as such.
6. The [Agentic QE engine](https://github.com/proffesor-for-testing/agentic-qe) by Dragan Spiridonov (open source, MIT), on which [Agentic QCSD](https://agentic-qe.dev/contributors) builds.
7. Lalitkumar Bhamare, [*Quality Conscious Software Delivery*](/assets/docs/Quality-Conscious-Software-Delivery-Lalitkumar-Bhamare.pdf), EuroSTAR Best Paper Award, 2022.
8. Cover photo by [Jason Yuen](https://unsplash.com/@fanfandyuen) on [Unsplash](https://unsplash.com/photos/photo-of-white-glass-panel-window-UQBmFv4u0wc).

Thanks to [Fausto Oliveira](https://www.linkedin.com/in/faustoreis/), [Christian Obermeyer](https://www.linkedin.com/in/christian-obermeyer/), [Akash Mohan](https://www.linkedin.com/in/akashmohanakash/) and [Christian Wurmdobler](https://www.linkedin.com/in/christian-wurmdobler/), with whom I often discuss these topics. Those conversations keep returning to the concerns Testability 2.0 reflects: how an agentic SDLC can deliver quality products at enterprise speed and scale, why that speed so often turns into rework instead of outcomes that matter, and what a delivery organisation has to put in place before it can trust what AI agents produce.

