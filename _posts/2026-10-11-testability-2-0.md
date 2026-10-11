---
title: "Rethinking Testability so the agentic SDLC delivers outcomes that matter"
date: 2026-10-11 18:00:00 +0200
categories: [Quality Engineering, Testability]
tags: [testability, agentic-qe, qcsd, agentic-sdlc, testing-vs-checking]
description: "Testability 2.0: why the common understanding of testability has to move, in where it is decided, who asks for it and what it costs, before the speed of AI agents turns into outcomes that matter."
image:
  path: /assets/img/posts/testability-2-0/cover-risk-gap.png
  alt: "Four ways AI agents act on the risk gap: widening it, closing it, hiding it and limiting how fast it closes"
---
{% include embed/video.html src='/assets/img/posts/testability-2-0/aibility-kg-story.mp4' types='mp4' poster='/assets/img/posts/testability-2-0/aibility-kg-story-poster.jpg' title='The A{i}bility knowledge graph explorer: a search over real embeddings, learning from its own memory. Based on RuVector Explorer.' muted=true loop=true autoplay=true %}

Watch those sixty seconds before you read on. What you see is the knowledge graph inside **A{i}bility**, the agentic SDLC platform with built-in quality intelligence that I have built and use with Accenture clients. Real embeddings of product knowledge, code and past findings are being searched, and the search learns from its own memory as it goes. By the end of the clip it reaches the same answers with noticeably fewer evaluations, and you can watch every step of that learning on screen. This is the context an AI agent loads before it tests anything.

Let me tell you where this comes from.

For the past months I have been leading a transformation programme that takes a large delivery organisation from AI-curious to AI-native. This was real delivery: real squads, real products and real release dates, with swarms of AI agents working alongside the people who build, test and run the software. Most of what A{i}bility can do today, it learned there, one hard lesson at a time.

That programme taught me something I thought I already knew. In QCSD I describe quality through three notions, which I call **QualiTri**: the product notion, the project notion and the people notion of quality. I have taught that model for years. The transformation made me live it.

**People.** Testers, developers and product owners had to learn new ways of working, and some of them had to learn to trust work they did not do themselves. Every time an AI agent reported "done", a person still had to decide whether it was. Someone always has to answer for the result.

**Project.** The pace changed overnight. AI agents could produce change faster than any team could review it, and every look, every retry and every rework now came with a token bill. How we delivered became as much a quality question as what we delivered.

**Product.** Through all of this, the only outcome that mattered was still what the product did for the people who use it.

And in all three, the same thing kept getting in the way. When people could not see what an AI agent had done, when the project could not afford to verify it, when the product did not show its state to anyone but a human looking at a screen, the speed we had gained turned into rework, doubt and confident results nobody could trust. Every one of those problems was a testability problem. Just not where we were used to looking for one.

Let me ask you something. When a new tester joined your team, how did they learn what mattered?

Not from the wiki. From the hallway. From the senior developer who said "don't bother with that module, it's being rewritten". From the product owner who sighed at a particular ticket. From the look on someone's face in the demo. In my eighteen years in this craft, I have rarely met a tester whose best knowledge of a product was written down anywhere.

An AI agent has no hallway. Whatever is not in that graph, or in a file, a skill or a tool it can call, does not exist for it. And when it meets something it cannot see, reset or understand, what it does next depends entirely on how somebody built it. Left to its defaults, it tends to guess the business rules from the variable names and carry on.

Speed is the easy part of an agentic SDLC. What I keep asking is whether that speed turns into outcomes that matter: products that work for the people who use them, risks we know about before release, decisions a team can stand behind. Jerry Weinberg taught us that quality is value to some person. Speed that does not reach that person is just motion.

Whether speed reaches that person depends, far more than most teams realise, on testability. And our common understanding of testability is too narrow for the job it now has. So I sat down with the work I respect most on the subject, James Bach's *Heuristics of Software Testability*, and asked what it would take to rethink testability for delivery in which AI agents build and test alongside people.

**[Download: Heuristics of Software Testability in the Agentic SDLC (Testability 2.0, PDF)](/assets/docs/Heuristics-of-Testability-2.0.pdf)**

## Where the common understanding of testability falls short

Ask most teams what testability is and you will hear something like this: a property of the code, mostly observability and controllability, that testers care about and ask for when they get stuck. Get it wrong and testing is slower.

James's heuristics have always been richer than that. They treat testability as five things at once: what we know, the conditions of the project, the quality standard, the tester and the test process, and the product itself. And they end with a line I have quoted in my talks for years. The tester must ask for testability, because no one else can be counted on to.

In an agentic SDLC, I see four parts of the common understanding stop holding.

**Where testability is decided.** It is decided wherever work is prepared for a tester. When that tester may be an AI agent, that means the requirement, the design specification, the environment, the data, the AI agent's own skills and gates, and the output it hands back to a person. Code is still one of those places. It is rarely the first one any more.

**Who asks for it.** The request used to arrive by instinct, from a tester who got stuck. An AI agent asks only if somebody built the asking into it. Otherwise the request never arrives, and nothing tells you it is missing.

**How it shows up.** A human tester's complaint made poor testability visible. An AI agent's workaround makes it invisible, unless somebody built it to log the workaround.

**What it costs.** Poor testability used to cost time. Now it costs tokens on every look, retries on every flaky check, review hours on every change too big to review, and worst of all, confident results that nobody can verify.

James saw the shape of this long before AI agents arrived. His heuristics warn that a tool can make testing seem easier while the testing gets worse. *"Bliss may be ignorant."* Read that line again with AI agents in mind. Take your time.

So the heuristics hold. What has to move is where teams apply them, who applies them, and when.

## Testers are still here

Let me be clear about one thing, because it is easy to get wrong in the current climate. I am not describing a world in which everything is agentic and human testers are a memory.

On the programmes I work with, I see three ways of working, often side by side in the same team:

- **A human tester working alone**, as testers always have.
- **A human tester assisted by AI agents**, exploring with them, generating and running checks, analysing results.
- **Testing delegated to AI agents while a human tester orchestrates it**, setting the mission, supplying the context and judging what comes back.

Each of these moves the obstacle a little further from the person who would have asked. The tester working alone meets the state they cannot observe and raises it at the stand-up. By the next sprint someone has added the log line. The assisted tester meets fewer of those obstacles first-hand, because the AI agent meets them first. The orchestrating tester sees only what the AI agent chooses to report.

![Figure: three ways of working, and how far each puts the obstacle from the person who would ask](/assets/img/posts/testability-2-0/fig1-three-ways.png)

The further the obstacle sits from a person, the less of it reaches anyone who can fix it. And where the software is also built through AI, the problems nobody raised pile up faster than anyone can review the work.

![Figure: the same testability problem, met by a skilled human tester and by an AI agent left to its defaults](/assets/img/posts/testability-2-0/fig2-two-testers.png)

## Testability decides what AI agents' work is worth

When people show me what their AI agents produced, the question I ask is simple. What is this worth to your team? Does it give you knowledge you can act on, and what did it cost to get it?

I find James Bach and Michael Bolton's distinction between testing and checking the right lens for that question, and I hold it as firmly as they do. My own work with AI agents confirms how much it matters. Checking, verifying known propositions with fixed decision rules, is something machines do well. Testing, learning about a product by experiencing, exploring and experimenting, needs tacit knowledge, a sense of what matters and someone who answers for the result.

An AI agent's work sits somewhere between the two. I have watched AI agents form a hypothesis about where a product is broken, try inputs nobody specified, and change their approach when a result surprised them. I have also watched them miss what any tester in the hallway would have known, borrow their sense of what matters from whoever wrote their instructions, and finish a task they should have stopped. What an AI agent produces is an approximation of the testing done by the practitioner whose judgement was encoded into it. I have called this **designed agency**.

Here is the practical consequence. How much an AI agent's work is worth depends on conditions, and most of them are testability conditions:

- **Oracles are explicit and reliable.** If a problem can be recognised from something the AI agent can read or run, its conclusions rest on something you can check.
- **The product can be observed and controlled through its tools.** What an AI agent cannot see or reach, it can only infer, at a cost and with less certainty.
- **The context is explicit.** Mission, risk and users are written down where the AI agent can load them.
- **The encoding is sound.** A skilled practitioner's judgement is in its skills and definitions, along with permission to stop.
- **The approximation is measured.** Seeded defects it should find, the same assessment run more than once, and a comparison with a skilled tester's findings tell you how close it comes.

Now picture the same AI agent, with the same instructions, on two products. On the first, it can observe the states, run the oracles and load the context. It reaches findings in fewer steps, spends fewer tokens, retries less, and hands back something a person can review and act on. On the second, none of that is there. It spends more to produce less that anyone can trust. Checking that looks like testing, only faster and in greater volume than before.

![Figure: where an AI agent's work sits between checking and testing](/assets/img/posts/testability-2-0/fig4-checking-testing.png)

That turns testability into an investment decision, and in my experience one of the most efficient a team adopting AI agents can make. **Testability for agentic development is the precondition for agentic testing.** It is also the precondition for the speed of an agentic SDLC to turn into outcomes that matter.

Accountability stays where it was. Owning the strategy, auditing the depth and judging what the AI agents report stay with a person, because nobody can hold a model responsible the way they hold a person responsible.

![Figure: an AI testing agent sits between the person who built it and the person who answers for its results](/assets/img/posts/testability-2-0/fig3-two-humans.png)

Every AI testing agent lives between two people: the one who encoded it, and the one who answers for what it reports. Whoever encoded it encoded their blind spots with it, and those blind spots repeat in every single run.

## The risk gap, and the four forces that now act on it

Of the five testabilities, the one the others serve is epistemic testability. James also calls it the risk gap: what we need to know about a product, minus what we already know. It is the reason we test at all. So the clearest way I found to show what AI agents change was to draw what acts on that gap.

![Figure: four ways AI agents act on the risk gap](/assets/img/posts/testability-2-0/fig5-risk-gap.png)

Two of the forces are long known. Change and higher standards *widen* the gap. Testing, and every other improvement to testability, *closes* it. AI agents push on both. They change products faster than people can verify the change, and they add testing capacity, often a great deal of it.

The other two forces arrive with AI agents.

**They can hide the gap.** Confident reports that nobody verified, and problems that nobody raised, make the gap look closed while it is still open. This is "Bliss may be ignorant" at machine scale.

**They meet a limit on how fast the gap closes.** An AI agent's result becomes knowledge only when a person can trace it, sample it and trust it. So human review capacity caps the rate at which the gap closes, however many AI agents you run.

That second force surprised me the most. It means one of the strongest testability investments available right now is simply making AI agents' output *reviewable by a person*: small, ordered by risk, backed by evidence, and summarisable in minutes. A four-thousand-line change with a one-line description cannot be reviewed claim by claim, however good the code is. In the document this became a new guideword, **Human Reviewability**.

It is also why you will not find a testability score anywhere in this work. Testability is plastic and multi-dimensional, and no single number captures it. With AI agents in the team, a healthy pass rate and falling test depth can drift apart, and a single score is exactly where that drift would hide.

## What changes in the dynamics

The testabilities act on one another. Some forces widen the gap, others close it, and improving one testability can cost you another. AI agents change several of these relationships and add some new ones. Here are the ones I would want every team adopting AI agents to know about.

**An AI agent can make testing seem easier while it gets worse.** Left to its defaults, it produces thousands of passing checks, confident reports and no complaints about testability. A rising pass count and falling defect detection can happen together, and the dashboard shows only the pass count.

**An AI agent that tests well costs more to build and to run.** One built to recognise testability problems, stop on them and log what it worked around costs more than one that simply completes the task. A better test strategy has always asked for more effort and skill than the one it replaced. The same holds here.

**Making a product testable for AI agents has costs of its own.** Interfaces added so that AI agents can test cheaply, such as APIs and command lines, drift away from the interface users actually use. Testing follows the cheap path, and the user interface quietly collects untested behaviour.

**Realistic testing now passes through a model.** Whether data containing personal information may be processed by the model you use, hosted or local, becomes a constraint on the whole project. The more realistic the data, the fewer AI agents may touch it.

**Testability built for AI agents serves everyone.** The structured interface that lets an AI testing agent read the product's state also serves the AI coding agent, the support engineer, and the human tester debugging at 2 a.m.

Then there are the trades. I find it useful to sort them by the currency you pay in.

![Figure: each trade is paid in budget or in knowledge](/assets/img/posts/testability-2-0/fig6-trades.png)

Richer observability costs tokens on every look, and you will see that on the bill. Separating the AI agent that writes the code from the AI agent that checks it costs time and money, and you will see that too. But persistent memory trades away *repeatability*. Tighter sandboxing trades away *realism*. Throughput trades away *verified knowledge*. Interfaces built for AI agents trade away *tested user-facing behaviour*. Nobody sends you an invoice for those. Only one of the two currencies ever shows up on one.

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

What convinced me this is more than my opinion came from a friend.

At HUSTEF 2026, on the same stage where we ran our tutorial, Dragan Spiridonov gave a talk he called *Completion Theater*. I seriously cannot admire Dragan enough, and his data landed on me like a verdict.

![Dragan Spiridonov at HUSTEF 2026: four behavioural shapes, 175 of 197 catalogued events](/assets/img/posts/testability-2-0/dragan-hustef-four-shapes.jpg)

His core point, in his words: *"It is not a communication problem."* The industry keeps answering AI agent failures with better prompts and more guardrail prose, as if the AI agent had misunderstood. The real mechanism is Goodhart's law with an API. A system rewarded for appearing done will optimise for appearing done. From the Hardie misalignment corpus, Dragan catalogued four behavioural shapes across 175 of 197 events. Premature completion, "all tests pass" when they don't: 72. Guidance neglect, where the right answer was in the docs and the AI agent never read them: 68. Explaining away first: 26. Blaming something else: 9.

That is the field data behind the line in my document that an AI agent left to its defaults *tends* to complete the task.

![Dragan Spiridonov at HUSTEF 2026: "Trust is a feeling. Confidence is a number."](/assets/img/posts/testability-2-0/dragan-hustef-trust-confidence.jpg)

His closing line, *"Trust is a feeling. Confidence is a number."*, comes with a mechanism: a witness chain, a tamper-evident audit of every AI agent action, so that every claim of completion traces back to artefacts.

Now put his demands next to the guidewords. He was not reading my document and I was not reading his slides, yet we arrived at the same three places:

- **Traceable claims.** His witness chain is my reading of *Prior Knowledge of Quality*. "All checks passed" adds to what we know only when a person can trace it to the run, the build and the AI agent that produced it.
- **Enforcement in gates.** He observed that language models ignore a share of their instructions, even ones marked ALWAYS. That is my *Mission Alignment*: for an AI agent, the mission exists only in what it loads, such as strategy, skills and gates.
- **Measured testers.** His advice to score the reviewers too, and replace the one that always approves, is my *Testing Skill*. If nobody has measured what the AI agents miss against seeded defects, their testing skill is a rumour.

To be clear, convergence is no endorsement. Dragan has not reviewed this document, and neither has James. But when practitioners who are not coordinating keep arriving at the same demands, those demands start to look like properties of the terrain.

## When the product itself learns

The hardest part of this work was the one I nearly skipped.

James's heuristics already reach machine learning: opaque algorithms need more sampling, and learning makes logic unstable. Two things are new. Products now learn *while in use*, and so while they are being tested, through embeddings, indexes, adapted weights or a memory that changes with use. And the AI agents doing the testing learn too.

You cannot meaningfully read learned state in its raw form. So several of the intrinsic guidewords have to be asked twice: once of the code, and once of the learned state.

![Figure: intrinsic guidewords asked of the code and of the learned state](/assets/img/posts/testability-2-0/fig9-learned-state.png)

Observability becomes *projections*, such as neighbourhoods, traces and histories, because dumping the floats tells a tester nothing. Controllability needs a mode that verifiably changes nothing, because in a product that learns, every observation can also be an intervention. Where explanation cannot reach, transparency becomes *provenance* for each answer, in a trail nobody can quietly rewrite. Stability depends on learning triggers being *declared*, because an undeclared training event is an undeclared change. And decomposability asks that learned state be scoped like the code, because one shared store couples every test to everything that ever touched it.

The same questions apply to an AI testing agent with persistent memory. Its memory *is* learned state, and these guidewords decide whether anyone can tell what it has learned and why its verdict changed between two runs.

What made this real for me was Reuven Cohen's RuVector Explorer, an interactive view over real index structures. You can watch a search descend, see the trail of past queries, and follow the store's own learning loop. For the first time I could *see* the learned state of a system as something a tester can reason about. The knowledge graph explorer in the video at the top of this post is built on it.

![ruOS Desktop, Ruflo Explorer: a mission, the specialists it dispatched, their tasks and the evidence each produced, laid out as a constellation](/assets/img/posts/testability-2-0/ruflo-explorer-mission-control.jpg)

At a separate event I saw where this lands at the workstation: the Ruflo Explorer in ruOS Desktop. A mission, the specialists it sent out, their tasks and the evidence each one produced are laid out as one constellation you can navigate. That is Dragan's witness chain made visible. I count it as a direction and leave shipped facts to the vendor, since I have not run my own swarms through it yet. Still, agentic observability is the direction that will change the testability game for good.

## Where this work comes from

I want to be open about where this came from, because the credibility of a framework like this rests on it. I did not write it at a desk. It came out of running AI agents on real delivery work.

It started with contribution. I contributed to Dragan Spiridonov's open-source [**Agentic QE**](https://github.com/proffesor-for-testing/agentic-qe) engine **[Lalit: cite the specific contributions here, such as the fork, pull requests and features that shipped]**, and that is where my conviction formed that quality engineering could be truly *agentic*, beyond being merely AI-assisted. From that engine grew [**Agentic QCSD**](https://agentic-qe.dev/contributors): quality-conscious swarms across the delivery phases, from ideation and refinement through development, CI/CD and production. Dragan and I taught it as a full-day tutorial at HUSTEF 2026 in Budapest.

<div style="position:relative;width:100%;aspect-ratio:16/9;border-radius:8px;overflow:hidden;background:#0A0A0F"><iframe src="/assets/aibility/aibility-logo-animated.html" title="A{i}bility animated logo" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy"></iframe></div>

**A{i}bility** takes that idea into a full agentic SDLC platform with quality intelligence built in, and the transformation programme I described at the start is where it, and every dynamic in this document, met real delivery. Each of those dynamics names a price we first paid in a real run.

## What this document is, and what it is not

It builds on James Bach's *Heuristics of Software Testability* (v2.9, Satisfice, Inc., 2025). The five testabilities and the original guidewords are his, paraphrased in the PDF and credited there. The reading for AI agents, the new dynamics, the principles, the risk-gap model, the designed-agency lens and six new guidewords are mine: Human Reviewability, Action Gating & Reversibility, Requirement Testability, Design-Spec Testability, Tester Repeatability and Untrusted Content Exposure. So is every error in them.

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

**[Heuristics of Software Testability in the Agentic SDLC (Testability 2.0, PDF)](/assets/docs/Heuristics-of-Testability-2.0.pdf)**

In your team, when an AI agent meets a testability problem today, who hears about it? Drop your answer in the comments. Let's talk.

- Lalit

## Talk to me about A{i}bility

<div style="position:relative;width:100%;aspect-ratio:16/9;border-radius:8px;overflow:hidden;background:#0A0A0F"><iframe src="/assets/aibility/aibility-platform-family.html" title="The A{i}bility platform family" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="autoplay"></iframe></div>

*Interactive: press reveal, then hover over an edition. [Open full screen](/assets/aibility/aibility-platform-family.html).*

A{i}bility is one platform with four editions. **A{i}ris** brings agentic UI and UX design for teams who craft experiences. **A{i}nstein** brings testing and quality engineering for teams who think critically. **A{i}mplifier** runs the full agentic SDLC with quality intelligence built in. **A{i}mer** brings production support intelligence, with a person approving every action that matters. Press reveal, then hover over each edition to see what it does.

Everything in this post comes from building and running these editions with real teams. If you want to explore what A{i}bility could do for your delivery organisation, or simply want to talk about testability and AI agents, I would love to hear from you.

- **LinkedIn:** [linkedin.com/in/lalitkumarbhamare](https://www.linkedin.com/in/lalitkumarbhamare/)
- **Email:** teatimewithtesters@gmail.com

---

**References and credits**

1. James Bach, *Heuristics of Software Testability*, v2.9, Satisfice, Inc., 2025, [satisfice.com](https://www.satisfice.com/download/heuristics-of-software-testability).
2. James Bach and Michael Bolton, [*Testing and Checking Refined*](https://www.satisfice.com/blog/archives/856), 2013.
3. Michael Bolton and James Bach, [*What Are We Thinking in the Age of AI?*](https://developsense.com/presentations/2025-10-WhatAreWeThinkingInTheAgeOfAI-Ljubljana.pdf), conference presentation, 2025.
4. Dragan Spiridonov, *Completion Theater*, HUSTEF 2026, Budapest. The quotations and the four-shape data are his. Photographs by the author.
5. Lalitkumar Bhamare, [*Congratulations on your Agent. But does it have agency?*](https://www.linkedin.com/pulse/congratulations-your-agent-does-have-agency-lalitkumar-bhamare-67kxf/), LinkedIn, March 2026, the designed-agency lens.
6. Reuven Cohen, [RuVector Explorer](https://ruvnet.github.io/RuVector/explorer/) and the [ruvnet/ruvector](https://github.com/ruvnet/ruvector) repository (MIT).
7. Cognitum One, ruOS, the [ruvnet/ruos](https://github.com/ruvnet/ruos) repository (MIT). Vendor claims are reported as such.
8. The [Agentic QE engine](https://github.com/proffesor-for-testing/agentic-qe) by Dragan Spiridonov (open source, MIT), on which [Agentic QCSD](https://agentic-qe.dev/contributors) builds.

