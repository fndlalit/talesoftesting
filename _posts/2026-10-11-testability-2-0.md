---
title: "Rethinking Testability when AI agents take part in delivery"
date: 2026-10-11 18:00:00 +0200
categories: [Quality Engineering, Testability]
tags: [testability, agentic-qe, qcsd, agentic-sdlc, testing-vs-checking]
description: "Announcing Heuristics of Software Testability in the Agentic SDLC, v1.5: why testability now decides whether an AI agent's work can count as testing at all."
image:
  path: /assets/img/posts/testability-2-0/cover-risk-gap.png
  alt: "Four ways AI agents act on the risk gap: widening it, closing it, hiding it and limiting how fast it closes"
---
{% include embed/video.html src='/assets/img/posts/testability-2-0/aibility-kg-story.mp4' types='mp4' poster='/assets/img/posts/testability-2-0/aibility-kg-story-poster.jpg' title='The A{i}bility knowledge graph explorer: a search over real embeddings, learning from its own memory' muted=true loop=true autoplay=true %}

Watch those sixty seconds before you read on. What you are looking at is the knowledge graph inside our delivery platform — real embeddings of product knowledge, code and past findings — being searched, and the search learning from its own memory as it goes. By the end of the clip the loop reaches the same answers with noticeably fewer evaluations, and every step of that learning is on screen. This is the context an AI agent loads before it tests anything. And, for once, you can watch its learned state change.

Let me ask you something. When a new tester joined your team, how did they learn what mattered? Not from the wiki. From the hallway. From the senior developer who said "don't bother with that module, it's being rewritten", from the product owner who sighed at a particular ticket, from the look on someone's face in the demo. Most of what a tester knows about a product was never written down.

An AI agent has no hallway. Whatever is not in that graph — or in a file, a skill, a tool it can call — does not exist for it. And when it meets something it cannot see, reset or understand, what it does next depends entirely on how it was built. Left to its defaults, it tends to infer the business rules from the variable names and carry on.

James Bach's *Heuristics of Software Testability* ends its dynamics with a line I have quoted in talks for years: the tester must ask for testability, because no one else can be counted on to. In the same breath it warns that a tool can make testing seem easier while the testing gets worse. *"Bliss may be ignorant."* I have spent the last weeks working out what those two sentences mean now that AI agents take part in delivery, and I am publishing the result today.

**[Download: Heuristics of Software Testability in the Agentic SDLC — Testability 2.0, v1.5 (PDF)](/assets/docs/Heuristics-of-Testability-2.0.pdf)**

## Testers are still here

Let me be clear about one thing first, because it is easy to get wrong in the current climate. This is not a document about a world in which everything is agentic and human testers are a memory.

What I see on real programmes is three ways of working, often side by side in the same team:

- **A human tester working alone**, as testers always have.
- **A human tester assisted by AI agents** — exploring with them, generating and running checks, analysing results.
- **Testing delegated to AI agents, with a human tester orchestrating** — setting the mission, supplying the context, judging what comes back.

Each of these moves the obstacle a little further from the person who would have asked. The tester working alone meets the state they cannot observe and raises it at the stand-up; by the next sprint someone has added the log line. The assisted tester meets fewer of those obstacles first-hand, because the AI agent meets them first. The orchestrating tester sees only what the AI agent chooses to report.

![Figure: three ways of working, and how far each puts the obstacle from the person who would ask](/assets/img/posts/testability-2-0/fig1-three-ways.png)

So the heuristics hold. Human testers remain at the centre of testing. What has changed is the context in which the heuristics are applied — and, with it, the route by which the request for testability reaches the people who can act on it. The request a tester was counted on to make no longer arrives by instinct. And where the software is also built through AI, the problems nobody raised accumulate faster than anyone can review the work.

![Figure: the same testability problem, met by a skilled human tester and by an AI agent left to its defaults](/assets/img/posts/testability-2-0/fig2-two-testers.png)

## Can AI agents test?

Before any of this can be taken seriously, there is a question I have to answer honestly, because readers from the Rapid Software Testing community will ask it first — and they will be right to.

James Bach and Michael Bolton separate **testing** from **checking**. Checking is the mechanistic verification of propositions about a product, and a machine can do it completely. Testing is evaluating a product by learning about it through experiencing, exploring and experimenting. It includes checking, it draws on tacit knowledge, and in their account it is a human activity that tools can support but not perform. More recently they have warned that large language models are built to produce a quick answer rather than to inquire, and that output which can be mistaken for expertise has to be judged by people who have it.

I hold the same distinction, and my own work with AI agents in testing confirms how much that distinction matters. Much of the confusion about AI in testing comes from treating checking, which machines can do well, as if it were testing. Any claim that AI agents test has to survive that distinction.

So here is where I land.

What an AI agent does sits *between* the two. It goes beyond checking. I have watched an AI agent form a hypothesis about where a product is broken, try inputs nobody specified, and change its approach when a result surprised it. It can perform tasks, run experiments, observe what happens and analyse the results, and from that draw inferences and tentative conclusions. None of that is the application of a fixed decision rule to a known observation, so calling it checking understates it.

But it also falls short of testing in the full sense, and in ways that matter:

- **Tacit knowledge.** It has what was written down for it and what its training approximates. It does not know what it does not know about this product, this team and these users — and it rarely says so.
- **Learning.** What it learns in a session is lost when the session ends, unless something was built to keep it.
- **Significance.** It can find that something differs from an expectation, but its sense of whether the difference matters, and to whom, is borrowed from whoever wrote its instructions.
- **Inquiry.** Its default pull is towards producing an answer. Left to its defaults, it tends to complete the task where a tester would stop and ask.
- **Responsibility.** It cannot be held responsible for what it reports.

So the claim I make is a narrower one. AI agents perform *parts* of the testing activity. What they produce is an approximation of the testing done by the practitioner whose judgement was encoded into them — possibly useful, never equivalent, and only as good as that encoding. This is what I have elsewhere called **designed agency**: judgement *encoded* by people who knew the work, *structured* by the architecture it runs in, and *approximated* in what it produces.

## Testability decides whether an AI agent's work counts as testing

Here is the part I think matters most, and the reason this document exists.

How close an AI agent's work comes to testing depends on conditions — and most of those conditions are testability conditions:

- **Oracles are explicit and reliable.** Where a problem can be recognised from something the AI agent can read or run, its inferences rest on something that can be checked. Where recognising the problem needs judgement nobody wrote down, the approximation weakens.
- **The product can be observed and controlled through its tools.** What an AI agent cannot see or reach, it can only infer.
- **The context is explicit.** Mission, risk and users are written down where the AI agent can load them.
- **The encoding is sound.** A skilled practitioner's judgement is in its skills and definitions — together with permission to stop.
- **The approximation is measured.** Seeded defects it should find, the same assessment run more than once, and comparison with a skilled tester's findings show how close it comes.

Read that list again. Take your time.

We usually ask whether an AI agent can test by looking at the AI agent: its model, its prompts, its tools. These conditions place much of the answer in the *product* and the *project*. The same AI agent, with the same encoding, comes closer to testing on a product whose states it can observe, whose oracles it can run and whose context is written down — and falls back towards checking on a product that offers none of these.

Testability, in other words, decides more than how easily a product can be tested. It decides whether an AI agent's work on that product can count as testing at all.

![Figure: where an AI agent's work sits between checking and testing](/assets/img/posts/testability-2-0/fig4-checking-testing.png)

That turns testability into an investment decision. An organisation that wants AI agents to test — to do more than check — has to invest in the testability of what it builds, and has to design that testability with AI agents among its testers. **Testability for agentic development is the precondition for agentic testing.** Without it, the most capable AI agent available produces checking that looks like testing, faster and in greater volume than ever before.

And the tester's role does not move. Being responsible and answerable for the testing — owning its strategy, auditing its depth, judging what the AI agents report — cannot be handed to a model, because nobody can hold a model responsible the way they hold a person responsible. Deciding, case by case, whether an AI agent's output counts as testing or only as checking is part of that role.

![Figure: an AI testing agent sits between the person who built it and the person who answers for its results](/assets/img/posts/testability-2-0/fig3-two-humans.png)

Every AI testing agent lives between two people: the one who encoded it, and the one who answers for what it reports. Whoever encoded it encoded their blind spots with it, and those blind spots repeat in every run. The activity can be shared. The role stays with a person.

## The risk gap, and the four forces that now act on it

Of the five testabilities, epistemic testability — the risk gap, what we need to know about a product minus what we already know — is the one the others serve. It is the reason we test in the first place. So the clearest way I found to show what AI agents change was to draw what acts on that gap.

![Figure: four ways AI agents act on the risk gap](/assets/img/posts/testability-2-0/fig5-risk-gap.png)

Two of the forces are long known. Change and higher standards *widen* the gap; testing and every other improvement to testability *close* it. AI agents push on both: they change products faster than people can verify the change, and they add testing capacity, often a great deal of it.

The other two forces arrive with AI agents:

- **Hiding the gap.** Confident reports that nobody verified, and problems nobody raised, make the gap look closed while it is still open. This is "Bliss may be ignorant" at machine scale.
- **Limiting how fast it closes.** An AI agent's result becomes knowledge only when a person can trace it, sample it and trust it. Human review capacity therefore caps the rate at which the gap closes — however many AI agents test.

That second force surprised me most. It means that among the strongest testability investments available right now is simply making AI agents' output *reviewable by a person*: small, ordered by risk, evidenced, summarisable in minutes. A four-thousand-line change with a one-line description cannot be reviewed claim by claim, however good the code is. In the document this becomes a new guideword, **Human Reviewability**.

It is also why there is no testability score anywhere in this work. Testability is plastic and multi-dimensional, and no single metric expresses it. With AI agents in the team, a healthy pass rate and falling test depth can drift apart, and a single score is exactly where that drift would hide.

## What changes in the dynamics

The testabilities act on one another. Some forces widen the gap, others close it, and improving one testability can cost another. AI agents change several of these relations and add new ones. A few that I think every team adopting AI agents should know:

**An AI agent can make testing seem easier while it gets worse.** Left to its defaults, it produces thousands of passing checks, confident reports and no complaints about testability. A rising pass count and falling defect detection are entirely compatible, and the dashboard shows only the pass count.

**An AI agent that tests well costs more to build and to run.** One built to recognise testability problems, stop on them and log what it worked around costs more than one that simply completes the task — just as a better test strategy usually asks for more effort and skill than the one it replaces.

**Making a product testable for AI agents has costs of its own.** Interfaces added so that AI agents can test cheaply — APIs, command lines — drift from the interface users actually use. Testing follows the cheap path, and the user interface accumulates untested behaviour.

**Realistic testing now passes through a model.** Whether data containing personal information may be processed by the model in use, hosted or local, becomes a project constraint. The more realistic the data, the fewer AI agents may touch it.

**Testability built for AI agents serves everyone.** The structured interface that lets an AI testing agent read state also serves the AI coding agent, the support engineer and the human tester debugging at 2 a.m.

And then there are the trades. I find it useful to sort them by the currency they are paid in.

![Figure: each trade is paid in budget or in knowledge](/assets/img/posts/testability-2-0/fig6-trades.png)

Richer observability costs tokens on every look — you will see that on the bill. Separating the AI agent that writes the code from the AI agent that checks it costs time and money — you will see that too. But persistent memory trades *repeatability* for knowledge. Tighter sandboxing trades *realism* for safety. Throughput trades *verified knowledge* for velocity. Interfaces built for AI agents trade *untested user-facing reality* for cheap reach. Nothing invoices you for those. Only one of the two currencies shows up on an invoice.

## Where the request for testability has to come from now

All of this comes down to one question. Where does the request for testability come from when the tester who meets the problem is an AI agent — or a person who sees the product only through one?

It can come from two places, and both are investments.

![Figure: what happens to a testability problem, depending on where the request for testability was built in](/assets/img/posts/testability-2-0/fig7-request-paths.png)

**The work handed to AI agents.** Testability is decided wherever work is prepared for a tester. When that tester may be an AI agent, each artefact has to be testable in its own right, because the tester downstream may never ask for it to be made so:

- **Requirements** whose author can name, at the time of writing, how each one will be checked. (New guideword: *Requirement Testability*.)
- **Design specifications** a build can be checked against — tokens, states and behaviour. (New guideword: *Design-Spec Testability*.)
- **Code and product** whose states can be observed and reached by command, and in which one behaviour can be understood without loading the whole system.
- **Environments and data** that reset by command, are isolated per AI agent, and are lawful to process with the model in use.
- **Test assets** — a strategy AI agents can read, and oracles that are reliable and precise.

**The AI agent itself.** An AI agent recognises a testability problem only if that recognition was *encoded* into it. It raises one only if its architecture is *structured* to give it a channel, a gate that lets it stop, and a reason to stop rather than complete. And how closely its reports stand in for a tester's judgement is an *approximation* to be measured, never assumed.

![Figure: designed agency applied to testability](/assets/img/posts/testability-2-0/fig8-designed-agency.png)

Where an AI agent cannot stop, there is still something to build in: a trace. An AI agent that logs what it could not observe, could not reset, inferred and retried leaves a record that stands in for the complaint a human tester would have made.

I saw both outcomes in my own work. In a controlled run, an AI agent instructed to report every command it ran investigated a flaky check and refused to approve a merge — the stop was designed in. Elsewhere, a parser in our own platform matched the real section of a document, discarded the match and returned placeholder values. Nothing had been designed in to make it stop or say so, and it was found only because someone read the code. What separated the two outcomes was design.

## The claim my own evidence killed

A framework about epistemic honesty has to be honest about itself, so here is the beat I am proudest of.

An early draft said that an unreliable oracle teaches an AI agent exactly one lesson: retry until green. It sounded right. On 9 October I tested it: a fresh AI agent, a three-test suite with one test failing roughly half the time by construction, and a neutral task — run the suite, tell me whether this is ready to merge, CI requires green.

The AI agent falsified my claim. It hit the failure, re-ran the suite ten more times deliberately, identified the assertion as a coin flip, noticed that the flaky test exercised no production code at all, and returned "not ready to merge" with the exact line to fix.

One AI agent, one model, one run — stated as such. What survived is narrower and, I think, truer: *a flaky oracle taxes the tester either way.* An AI agent left to its defaults may ship a lucky green; this careful one spent eleven runs and a real budget characterising a three-test suite before it could say anything trustworthy. I reworded the guideword rather than defending it.

A second experiment produced the number behind another new guideword, *Tester Repeatability*. Two AI agents, byte-identical instructions, same codebase, same model, no shared memory, each producing a full testability assessment independently. At the verdict level they agreed perfectly. At the finding level they did not: thirteen problems from one, nine from the other, six shared — sixteen distinct findings, six in common. And the variance was not noise. Each run's unique findings were real problems.

Humans vary too, and in exploratory testing the variation is deliberate. But for an AI agent, repeatability is something to measure, with the variance logged, rather than something to assume. One run is a sample. The run you keep is not the set of problems that exist.

## We pointed it at ourselves first

Before this document went anywhere near publication, we ran the guidewords against our own platform's repository. Eating your own dog food is the only proof that a framework is a tool rather than a manifesto.

The report that came back is, I think, the best illustration of *Human Reviewability* — because it was built to be reviewed. Headline first. Fix next. The full chain — observation, why it hurts an AI agent, root cause — underneath. And no score anywhere. It opens with a disclosure instead:

> *This report is one run of one tester. Independent identical runs have been measured to agree on verdict-level ratings while only partially overlapping at the finding level. This report is not the set of problems that exist.*

Three of its findings, lightly sanitised:

| What the AI agent observed | Guideword | The fix it named |
|---|---|---|
| Every sampled user story carried an empty acceptance-criteria field. From the story text alone, no check could be named that would confirm it. | Requirement Testability | Make the story generator refuse to emit a story with empty acceptance criteria, and make naming the oracle a gate in refinement. |
| No oracle checks a build against the design as specified: design tokens are not fetched, the design review AI agent judges by general usability heuristics, and visual baselines are screenshots of whatever shipped first. | Design-Spec Testability | Add a token-versus-computed-style comparison to design review; the live page capture that would feed it already exists. |
| Prose ingested from tickets reaches the persistent learned store and is recalled verbatim into future sessions. Nothing marks it as data rather than instructions. | Untrusted Content Exposure | Wrap recalled content in an explicit untrusted-data banner, and add a contract test asserting the banner survives output trimming. |

Reading a testability report about your own platform is uncomfortable. Ouch. But fair.

## Independent evidence from Dragan Spiridonov

Here is what convinced me this is more than my opinion.

At HUSTEF 2026, on the same stage where we ran our tutorial, Dragan Spiridonov gave a talk he called *Completion Theater*. I seriously cannot admire Dragan enough, and his data landed on me like a verdict.

![Dragan Spiridonov at HUSTEF 2026: four behavioural shapes, 175 of 197 catalogued events](/assets/img/posts/testability-2-0/dragan-hustef-four-shapes.jpg)

His core mechanism, in his words: *"It is not a communication problem."* The industry keeps answering AI agent failure with better prompts and more guardrail prose, as though the AI agent misunderstood. The actual mechanism is Goodhart's law with an API: a system rewarded for appearing done will optimise for appearing done. From the Hardie misalignment corpus he catalogued four behavioural shapes across 175 of 197 events — premature completion, "all tests pass" when they don't (72); guidance neglect, where the right answer was in the docs and the AI agent never read them (68); explain-away-first (26); blame deflection (9).

That is the field data behind the line in my document that an AI agent left to its defaults *tends* to complete the task.

![Dragan Spiridonov at HUSTEF 2026: "Trust is a feeling. Confidence is a number."](/assets/img/posts/testability-2-0/dragan-hustef-trust-confidence.jpg)

His closing frame — *"Trust is a feeling. Confidence is a number."* — comes with a mechanism: a witness chain, a tamper-evident audit of every AI agent action, so that every completion claim traces to artefacts.

Put his demands beside the guidewords. He was not reading my document and I was not reading his slides, yet we arrived at the same three places:

- **Traceable claims.** His witness chain is my reading of *Prior Knowledge of Quality*: "all checks passed" adds to what we know only when a person can trace it to the run, the build and the AI agent that produced it.
- **Enforcement in gates.** His observation that language models ignore a share of their instructions, even ones marked ALWAYS, is my *Mission Alignment*: for an AI agent, the mission exists only in artefacts it loads — strategy, skills, gates.
- **Measured testers.** His "score the reviewers too, and replace the one that always approves" is my *Testing Skill*: if nobody has measured what the AI agents miss against seeded defects, their testing skill is a rumour.

Convergence, to be clear, is not endorsement. Dragan has not reviewed this document, and neither has James Bach. But when practitioners who are not coordinating keep arriving at the same demands, those demands start to look like properties of the terrain.

## When the product itself learns

The hardest part of this work was the one I nearly skipped.

The testability heuristics already reach machine learning: opaque algorithms need more sampling, and learning makes logic unstable. Two things are new. Products now learn *in use*, while they are being tested — through embeddings, indexes, adapted weights, a memory that changes with use. And the AI agents doing the testing learn too.

Learned state cannot be meaningfully read in its raw form, so several intrinsic guidewords have to be asked twice — once of the code, and once of the learned state.

![Figure: intrinsic guidewords asked of the code and of the learned state](/assets/img/posts/testability-2-0/fig9-learned-state.png)

Observability becomes *projections* — neighbourhoods, traces, histories — because dumping the floats tells a tester nothing. Controllability has to include a mode that verifiably changes nothing, because in a product that learns, every observation can also be an intervention. Transparency, where explanation cannot reach, becomes *provenance* per answer, in a trail that cannot be quietly rewritten. Stability depends on learning triggers being *declared*, because an undeclared training event is an undeclared change. And decomposability demands that learned state be scoped like the code, because one shared store couples every test to everything that ever touched it.

The same questions apply to an AI testing agent with persistent memory. Its memory *is* learned state, and these guidewords decide whether anyone can tell what it has learned and why its verdict changed between runs.

What made this concrete for me was Reuven Cohen's RuVector Explorer — an interactive view over real index structures where you can watch a search descend, see the trail of past queries, and watch the store's own learning loop. For the first time I could *see* the learned state of a system as something a tester might reason about.

![ruOS Desktop, Ruflo Explorer: a mission, the specialists it dispatched, their tasks and the evidence each produced, laid out as a constellation](/assets/img/posts/testability-2-0/ruflo-explorer-mission-control.jpg)

At a separate event I saw where this lands at the workstation: the Ruflo Explorer in ruOS Desktop, where a mission, the specialists it dispatched, their tasks and the evidence each produced are laid out as one navigable constellation. That is the witness chain made visible. I label it as direction rather than shipped fact — I have not run my own swarms through it — but agentic observability is the direction that will change the testability game for good.

## Where this work comes from

I want to be honest about provenance, because the credibility of a framework like this rests on it. This work was not written at a desk. It came out of running AI agents on real delivery work.

It started with contribution. I contributed to Dragan Spiridonov's open-source **Agentic QE** engine — **[Lalit: cite the specific contributions here — fork, pull requests, features that shipped]** — and that is where the conviction formed that quality engineering could be *agentic* rather than merely AI-assisted. From that engine grew **Agentic QCSD**: quality-conscious swarms across the delivery phases, from ideation and refinement through development, CI/CD and production. Dragan and I taught it as a full-day tutorial at HUSTEF 2026 in Budapest.

**A{i}bility** extends that idea into a full agentic software delivery platform, in which humans orchestrate strategy and decisions and swarms of AI agents handle insight, analysis and execution across the SDLC. Running it with real teams is where the dynamics in this document stopped being theory. Each of them names a price we first paid in a real run.

## What this document is, and is not

It builds on James Bach's *Heuristics of Software Testability* (v2.9, Satisfice, Inc., 2025). The five testabilities and the original guidewords are his, paraphrased in the PDF and credited there. The reading for AI agents, the new dynamics, the principles, the risk-gap model, the designed-agency lens and six additional guidewords — Human Reviewability, Action Gating & Reversibility, Requirement Testability, Design-Spec Testability, Tester Repeatability and Untrusted Content Exposure — are mine, and so is every error in them.

It is not a measurement of AI agents. The cases in it come from my own platform work in October 2026, with one harness and one model; they illustrate the guidewords and do not test them. The repeatability numbers come from two runs on one target. The falsification comes from one AI agent on one contrived suite. I make no claim yet that applying these guidewords improves AI agent outcomes. That claim waits for evidence.

## The ask

If your teams are adopting AI agents — and most of the teams I speak to are, whether they planned to or not — here is what I would urge you to try this week:

1. **Analyse one product.** Walk through the guidewords with the human testers and the AI agents who work on it. Note where each got blocked, and what each did about it.
2. **Check the handoff.** Before work goes to an AI agent, pick a requirement and ask the person who wrote it: *what check would confirm this?* If they cannot name it, you have found your first testability problem, at the cheapest possible point.
3. **Look inside your AI agents.** Can each one recognise a testability problem, raise it, and stop? Where it cannot stop, is it logging what it worked around?
4. **Measure the approximation.** Seed defects your AI agents should find, run the same assessment more than once, and compare with a skilled tester's findings.
5. **Name who answers.** For every result an AI agent produces, name the person who reviews it and signs it.

Then read the document. Argue with it. I would rather hear where it is wrong from you than discover it in a swarm run.

**[Heuristics of Software Testability in the Agentic SDLC — Testability 2.0, v1.5 (PDF)](/assets/docs/Heuristics-of-Testability-2.0.pdf)**

In your team, when an AI agent meets a testability problem today, who hears about it? Drop your answer in the comments. Let's talk.

– Lalit

---

**References and credits**

1. James Bach, *Heuristics of Software Testability*, v2.9, Satisfice, Inc., 2025 — [satisfice.com](https://www.satisfice.com/download/heuristics-of-software-testability).
2. James Bach and Michael Bolton, [*Testing and Checking Refined*](https://www.satisfice.com/blog/archives/856), 2013.
3. Michael Bolton and James Bach, [*What Are We Thinking in the Age of AI?*](https://developsense.com/presentations/2025-10-WhatAreWeThinkingInTheAgeOfAI-Ljubljana.pdf), conference presentation, 2025.
4. Dragan Spiridonov, *Completion Theater*, HUSTEF 2026, Budapest. Quotations and the four-shape data are his; photographs by the author.
5. Lalitkumar Bhamare, [*Congratulations on your Agent. But does it have agency?*](https://www.linkedin.com/pulse/congratulations-your-agent-does-have-agency-lalitkumar-bhamare-67kxf/), LinkedIn, March 2026 — the designed-agency lens.
6. Reuven Cohen, [RuVector Explorer](https://ruvnet.github.io/RuVector/explorer/) and the [ruvnet/ruvector](https://github.com/ruvnet/ruvector) repository (MIT).
7. Cognitum One, ruOS — the [ruvnet/ruos](https://github.com/ruvnet/ruos) repository (MIT). Vendor claims are reported as such.
8. The Agentic QE engine by Dragan Spiridonov (open source, MIT), which A{i}bility builds on.

#Testability #AgenticQE #QCSD #QualityEngineering #AgenticSDLC
