---
title: "Rethinking Testability - so we help AI agents deliver outcomes that matter (Part 1)"
date: 2026-10-11 15:01:00 +0200
categories: [Quality Engineering, Testability, Agentic SDLC]
tags: [testability, agentic-qe, qcsd, agentic-sdlc, testing-vs-checking]
description: "Testability 2.0, Part 1: why the common understanding of testability has to move, in where it is decided, who asks for it and what it costs, before the speed of AI agents turns into outcomes that matter."
image:
  path: /assets/img/posts/testability-2-0/cover-window.jpg
  alt: "An open window in a white wall, with the room behind it in darkness. Photo by Jason Yuen on Unsplash."
---
**Can you see what your AI agents know?**

In most teams, nobody can.

The sixty seconds below show what it looks like when you can: the knowledge graph explorer in **A{i}bility** (the agentic SDLC platform with built-in quality intelligence, but more on it later) watching a search decide what context an AI agent gets to work with.

{% include embed/video.html src='/assets/img/posts/testability-2-0/aibility-kg-story.mp4' types='mp4' poster='/assets/img/posts/testability-2-0/aibility-kg-story-poster.jpg' %}

<p style="margin:1.25rem 0 2rem;text-align:center;font-style:italic;font-size:0.95rem;line-height:1.5">The A{i}bility knowledge graph explorer: a search over real embeddings, learning from its own memory. Based on RuVector Explorer with Agentic QE as intel engine.</p>

So, the explorer you see above shows exploring through 10,000 real embeddings from the A{i}bility knowledge graph. They come from code across several repositories, Jira and Confluence, business discovery and technical solution briefs, test and automation strategies, and the patterns and learnings gathered while implementing the code. The search starts cold and runs through four phases: a warm-up, a drift to unfamiliar queries, a return to familiar ones, and noise. As it goes, it keeps a memory of past queries and their answers, and tunes a single setting: how widely it searches. The graph itself and the platform's models stay exactly as they were. Across the whole run, the search needed 24.1% fewer distance evaluations than a static search, while still finding 94 to 99 per cent of the true nearest matches in each phase. You can watch it adapt, query by query. Whether anyone can see that, and check it, is a testability question. That is where this story starts.

Let me first tell you where this comes from.

I wrote the [QCSD](/assets/docs/Quality-Conscious-Software-Delivery-Lalitkumar-Bhamare.pdf) framework to help organisations deliver quality products without having to add extra resources or spend more time. My efforts to agentify QCSD brought me closer to what my friend [Dragan Spiridonov](https://www.linkedin.com/in/dragan-spiridonov/) was building with his [Agentic QE Fleet](https://github.com/proffesor-for-testing/agentic-qe) back in September 2025.

His foundational work on the AQE fleet helped me build [**Agentic QCSD**](https://agentic-qe.dev/contributors): an agentic harness with several special-purpose agentic loops, carefully designed, defined and interconnected through cross-phase exchange, all based on the underlying QCSD philosophy. And yes, this agentic fleet and these agentic loops have been created well before "loop engineering" became a coined term.

What I started as Agentic QCSD on my agentic journey has now become a full-fledged agentic SDLC platform with built-in quality intelligence. For everything it enables teams to do, and for how it amplifies human effectiveness with the help of AI, I have named it **A{i}bility**.

I am currently delivering most of my client projects within Accenture using this A{i}bility platform. That includes leading an "AI-curious to AI-native" transformation programme for a large enterprise. And I must say, it has been a fun ride. I have learned, unlearned and re-learned a lot over this period, and it still continues.

These have been real projects, with real products, real users and real release dates, where swarms of AI agents work alongside the people who build, test and run the software. Most of what A{i}bility can do today, it learned on those projects, one hard lesson at a time.

That work also taught me something I thought I already knew. In QCSD I describe quality through three notions, which I call **QualiTri**: the **Product** notion, the **Project** notion and the **People** notion of quality. I have taught that model for years. Building and running A{i}bility across these projects made me live it.

- **People.** Testers, developers and product owners had to learn new ways of working, and some of them had to learn to trust work they did not do themselves. Every time an AI agent reported "done", a person still had to decide whether it was. Someone always has to answer for the result.
- **Project.** The pace changed overnight. AI agents could produce change faster than any team could review it, and every look, every retry and every rework now came with a token bill. How we delivered became as much a quality question as what we delivered.
- **Product.** Through all of this, the only outcome that mattered was still what the product did for the people who use it.

And in all three, the same thing kept getting in the way. When people could not see what an AI agent had done, when the project could not afford to verify it, when the product did not show its state to anyone but a human looking at a screen, the speed we had gained turned into rework, doubt and confident results nobody could trust. Every one of those problems was a testability problem. Just not where we were used to looking for one.

Let me ask you something. When someone new joined your team, whether a tester, a developer, a designer or a product owner, how did they learn what mattered?

Not from the wiki. From the hallway. From the senior developer who said "don't bother with that module, it's being rewritten". From the product owner who sighed at a particular ticket. From the tester who knew which screen always broke after a release. From the look on someone's face in the demo. In my eighteen years in this craft, I have rarely met anyone in delivery whose best knowledge of a product was written down anywhere.

An AI agent has no hallway. Whatever is not in that graph, or in a file, a skill or a tool it can call, does not exist for it. And when it meets something it cannot see, reset or understand, what it does next depends entirely on how somebody built it. Left to its defaults, it tends to guess the business rules from the variable names and carry on.

Nowhere does this hurt more than at the handoff between business and engineering. That handoff was always the biggest hallway in any enterprise. Business intent travelled as prose, and the gaps were filled in refinements, in side conversations and in the product owner's head. Today the reader on the other side of that handoff is more and more often an AI agent, and a swarm of them can turn an ambiguous requirement into thousands of lines of confident code before lunch. At enterprise speed and scale, a gap in intent gets copied into every story, every test and every AI agent that touches it.

This is where rethinking testability pays off first. If testability is decided wherever work is prepared for a tester, the first piece of work prepared is the business intent itself, and it has to be testable in its own right. Testability 2.0 asks three things of it:

- whoever writes a requirement can say, while writing it, how it will be checked (*Requirement Testability*);
- the design it points to can be checked against: tokens, states and behaviour (*Design-Spec Testability*);
- the mission, the risks and the users are written down where an AI agent can load them.

Meet those at the handoff, and every AI agent downstream starts from intent it can verify. Miss them, and no amount of testing later recovers what was never said.

Speed is the easy part of an agentic SDLC. What I keep asking is whether that speed turns into outcomes that matter: products that work for the people who use them, risks we know about before release, decisions a team can stand behind. Jerry Weinberg taught us that quality is value to some person. Speed that does not reach that person is just motion.

Whether speed reaches that person depends, far more than most teams realise, on testability. And our common understanding of testability is too narrow for the job it now has. So I sat down with the work I respect most on the subject, James Bach's *Heuristics of Software Testability*, and asked what it would take to rethink testability for delivery in which AI agents build and test alongside people. The result is a document, *Heuristics of Software Testability in the Agentic SDLC*.

If you would rather go straight to the heuristics, **[download Testability 2.0 (PDF)](/assets/docs/Heuristics-of-Testability-2.0.pdf)**. If you want the story behind them, read on.

## Where the common understanding of testability falls short

Ask most teams what testability is and you will hear something like this: a property of the code, mostly observability and controllability, that testers care about and ask for when they get stuck. Get it wrong and testing is slower.

James's heuristics have always been richer than that. They treat testability as five things at once: what we know, the conditions of the project, the quality standard, the tester and the test process, and the product itself. And they end with a line I have quoted in my talks for years. The tester must ask for testability, because no one else can be counted on to.

In an agentic SDLC, I see four parts of the common understanding stop holding.

- **Where testability is decided.** It is decided wherever work is prepared for a tester. When that tester may be an AI agent, that means the requirement, the design specification, the environment, the data, the AI agent's own skills and gates, and the output it hands back to a person. Code is still one of those places. It is rarely the first one any more.
- **Who asks for it.** The request used to arrive by instinct, from a tester who got stuck. An AI agent asks only if somebody built the asking into it. Otherwise the request never arrives, and nothing tells you it is missing.
- **How it shows up.** A human tester's complaint made poor testability visible. An AI agent's workaround makes it invisible, unless somebody built it to log the workaround.
- **What it costs.** Poor testability used to cost time. Now it costs tokens on every look, retries on every flaky check, review hours on every change too big to review, and worst of all, confident results that nobody can verify.

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

An AI agent's work sits somewhere between the two. I have watched AI agents form a hypothesis about where a product is broken, try inputs nobody specified, and change their approach when a result surprised them. I have also watched them miss what any tester in the hallway would have known, borrow their sense of what matters from whoever wrote their instructions, and finish a task they should have stopped. What an AI agent produces is an approximation of the testing done by the practitioner whose judgement was encoded into it. I have called this [**designed agency**](https://www.linkedin.com/pulse/congratulations-your-agent-does-have-agency-lalitkumar-bhamare-67kxf/).

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

- **They can hide the gap.** Confident reports that nobody verified, and problems that nobody raised, make the gap look closed while it is still open. This is "Bliss may be ignorant" at machine scale.
- **They meet a limit on how fast the gap closes.** An AI agent's result becomes knowledge only when a person can trace it, sample it and trust it. So human review capacity caps the rate at which the gap closes, however many AI agents you run.

That second force surprised me the most. It means one of the strongest testability investments available right now is simply making AI agents' output *reviewable by a person*: small, ordered by risk, backed by evidence, and summarisable in minutes. A four-thousand-line change with a one-line description cannot be reviewed claim by claim, however good the code is. In the document this became a new guideword, **Human Reviewability**.

It is also why you will not find a testability score anywhere in this work. Testability is plastic and multi-dimensional, and no single number captures it. With AI agents in the team, a healthy pass rate and falling test depth can drift apart, and a single score is exactly where that drift would hide.

## What changes in the dynamics

The testabilities act on one another. Some forces widen the gap, others close it, and improving one testability can cost you another. AI agents change several of these relationships and add some new ones. Here are the ones I would want every team adopting AI agents to know about.

- **An AI agent can make testing seem easier while it gets worse.** Left to its defaults, it produces thousands of passing checks, confident reports and no complaints about testability. A rising pass count and falling defect detection can happen together, and the dashboard shows only the pass count.
- **An AI agent that tests well costs more to build and to run.** One built to recognise testability problems, stop on them and log what it worked around costs more than one that simply completes the task. A better test strategy has always asked for more effort and skill than the one it replaced. The same holds here.
- **Making a product testable for AI agents has costs of its own.** Interfaces added so that AI agents can test cheaply, such as APIs and command lines, drift away from the interface users actually use. Testing follows the cheap path, and the user interface quietly collects untested behaviour.
- **Realistic testing now passes through a model.** Whether data containing personal information may be processed by the model you use, hosted or local, becomes a constraint on the whole project. The more realistic the data, the fewer AI agents may touch it.
- **Testability built for AI agents serves everyone.** The structured interface that lets an AI testing agent read the product's state also serves the AI coding agent, the support engineer, and the human tester debugging at 2 a.m.

Then there are the trades. I find it useful to sort them by the currency you pay in.

![Figure: each trade is paid in budget or in knowledge](/assets/img/posts/testability-2-0/fig6-trades.png)

Richer observability costs tokens on every look, and you will see that on the bill. Separating the AI agent that writes the code from the AI agent that checks it costs time and money, and you will see that too. But persistent memory trades away *repeatability*. Tighter sandboxing trades away *realism*. Throughput trades away *verified knowledge*. Interfaces built for AI agents trade away *tested user-facing behaviour*. Nobody sends you an invoice for those. Only one of the two currencies ever shows up on one.

## What comes in Part 2

That is the case for rethinking testability. [Part 2](/posts/testability-2-0-part-2/) is about what to do with it: where the request for testability has to come from when the tester is an AI agent, the claim my own evidence killed, what happened when we pointed the guidewords at our own platform, Dragan's field data, and what changes when the product itself learns. It ends with what I would ask you to try this week.

**[Read Part 2](/posts/testability-2-0-part-2/)** or **[download Testability 2.0 (PDF)](/assets/docs/Heuristics-of-Testability-2.0.pdf)**.

In your team, where is testability decided today, and who decides it? Drop your answer in the comments. Let's talk.

*Lalit*

---

## Talk to me about A{i}bility

<div style="position:relative;width:100%;aspect-ratio:16/9;border-radius:8px;overflow:hidden;background:#0A0A0F"><iframe src="/assets/aibility/aibility-platform-family.html" title="The A{i}bility platform family" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="autoplay"></iframe></div>

*Interactive: press reveal, then hover over a sub-module. [Open full screen](/assets/aibility/aibility-platform-family.html).*

A{i}bility is one platform with four sub-modules, for now. **A{i}ris** brings agentic UI and UX design for teams who craft experiences. **A{i}nstein** brings testing and quality engineering for teams who think critically. **A{i}mplifier** runs the full agentic SDLC with quality intelligence built in. **A{i}mer** brings production support intelligence, with a person approving every action that matters. Press reveal, then hover over each sub-module to see what it does.

Everything in this post comes from building and running these sub-modules with real teams.

A{i}bility is a team effort. The people in my team use it on real projects every day, contribute to it, and keep shaping it with their feedback. Much of what it does well today comes from them. Thank you, Aleksejs Demjanenko, Anju Bose, Arturs Pugejs, Daniels Gurjevs, Hariprasad Satheendran, Naresh Aithagoni, Naveen Sivakumar, Shabbir Ahmed, Shahzad Hafeez and Sivapriya V B.

If you want to explore what A{i}bility could do for your delivery organisation, or simply want to talk about testability and AI agents, I would love to hear from you.

**LinkedIn:** [linkedin.com/in/lalitkumarbhamare](https://www.linkedin.com/in/lalitkumarbhamare/)

## References and credits

1. James Bach, *Heuristics of Software Testability*, v2.9, Satisfice, Inc., 2025, [satisfice.com](https://www.satisfice.com/download/heuristics-of-software-testability).
2. James Bach and Michael Bolton, [*Testing and Checking Refined*](https://www.satisfice.com/blog/archives/856), 2013.
3. Michael Bolton and James Bach, [*What Are We Thinking in the Age of AI?*](https://developsense.com/presentations/2025-10-WhatAreWeThinkingInTheAgeOfAI-Ljubljana.pdf), conference presentation, 2025.
4. Lalitkumar Bhamare, [*Congratulations on your Agent. But does it have agency?*](https://www.linkedin.com/pulse/congratulations-your-agent-does-have-agency-lalitkumar-bhamare-67kxf/), LinkedIn, March 2026, the designed-agency lens.
5. Reuven Cohen, [RuVector Explorer](https://ruvnet.github.io/RuVector/explorer/) and the [ruvnet/ruvector](https://github.com/ruvnet/ruvector) repository (MIT).
6. The [Agentic QE engine](https://github.com/proffesor-for-testing/agentic-qe) by Dragan Spiridonov (open source, MIT), on which [Agentic QCSD](https://agentic-qe.dev/contributors) builds.
7. Lalitkumar Bhamare, [*Quality Conscious Software Delivery*](/assets/docs/Quality-Conscious-Software-Delivery-Lalitkumar-Bhamare.pdf), EuroSTAR Best Paper Award, 2022.
8. Cover photo by [Jason Yuen](https://unsplash.com/@fanfandyuen) on [Unsplash](https://unsplash.com/photos/photo-of-white-glass-panel-window-UQBmFv4u0wc).

