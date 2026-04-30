---
layout: page
title: Quality Conscious Software Delivery
icon: fas fa-award
order: 2
---

<style>
  .qcsd { max-width: 720px; }
  .qcsd p { font-size: 1.05rem; line-height: 1.9; color: var(--text-color, #444); }
  .qcsd a { color: var(--heading-color, #1a1a2e); text-decoration: underline; text-decoration-color: #50b8a6; text-underline-offset: 3px; text-decoration-thickness: 1.5px; transition: text-decoration-color 0.2s; }
  .qcsd a:hover { text-decoration-color: var(--heading-color, #1a1a2e); }

  .qcsd h2 {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.65rem;
    font-weight: 400;
    font-style: italic;
    color: var(--heading-color, #1a1a2e);
    margin: 3.5rem 0 1.2rem;
    letter-spacing: -0.01em;
  }

  .qcsd-lede {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.35rem;
    line-height: 1.7;
    color: var(--heading-color, #1a1a2e);
    margin-bottom: 2.5rem;
    max-width: 640px;
  }

  .qcsd-pull {
    margin: 2.5rem 0;
    padding: 0 0 0 1.5rem;
    border-left: 3px solid #50b8a6;
  }
  .qcsd-pull p {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.15rem;
    font-style: italic;
    line-height: 1.75;
    color: var(--heading-color, #1a1a2e);
  }
  .qcsd-pull cite {
    font-style: normal;
    font-family: -apple-system, sans-serif;
    font-size: 0.85rem;
    color: #50b8a6;
    display: block;
    margin-top: 0.8rem;
  }

  .qcsd-sep {
    border: none;
    height: 1px;
    background: var(--card-border-color, #e0e0e0);
    margin: 3rem 0;
    max-width: 80px;
  }

  .qcsd-trio {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 2rem;
    margin: 2rem 0 1.5rem;
  }
  @media (max-width: 720px) { .qcsd-trio { grid-template-columns: 1fr; } }
  .qcsd-trio-item h3 {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.05rem;
    font-weight: 400;
    font-style: italic;
    color: var(--heading-color, #1a1a2e);
    margin: 0 0 0.4rem;
  }
  .qcsd-trio-item p {
    font-size: 0.92rem;
    line-height: 1.65;
    color: var(--text-muted-color, #777);
    margin: 0;
  }

  .qcsd-4e {
    margin: 2rem 0;
  }
  .qcsd-4e-item {
    display: grid;
    grid-template-columns: 56px 1fr;
    gap: 0 1.2rem;
    margin-bottom: 1.8rem;
    align-items: start;
  }
  .qcsd-4e-num {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.8rem;
    font-weight: 400;
    color: #50b8a6;
    line-height: 1;
    padding-top: 0.15rem;
    text-align: right;
  }
  .qcsd-4e-body h3 {
    font-size: 1rem;
    font-weight: 700;
    color: var(--heading-color, #1a1a2e);
    margin: 0 0 0.3rem;
  }
  .qcsd-4e-body p {
    font-size: 0.95rem;
    margin: 0;
    line-height: 1.7;
  }
  .qcsd-4e-body .qcsd-agent-note {
    font-size: 0.88rem;
    color: #50b8a6;
    margin-top: 0.4rem;
    font-style: italic;
  }
</style>

<div class="qcsd">

<p class="qcsd-lede">
When you ask most teams what "quality engineering" means, the answer comes back in tooling: automation frameworks, CI/CD gates, SonarQube dashboards, DORA metrics. These things matter. But they are answers to the wrong question.
</p>

<p>The question isn't <em>how do we check more things faster</em>. It's <em>how do we make quality a conscious act at every stage of building software</em>.</p>

<p><a href="https://en.wikipedia.org/wiki/Gerald_Weinberg" target="_blank" rel="noopener">Jerry Weinberg</a> saw this decades ago when he wrote that quality is value to some person — and that no matter what they tell you at first, it is always a people problem. The cost of poor software quality in the US alone reached $2.41 trillion in 2022, yet the industry's response has been to double down on the same thinking: more automation, more dashboards, more gates. I call this the <strong>Faster Horse cycle</strong> — using 21st-century tools to optimise 20th-century objectives. Teams producing more tests than ever, while producing no better software.</p>

<p>The engineering solutions are just a tiny part of the picture. The deeper problem is one of consciousness for quality — or rather, its absence. And that's where QCSD begins.</p>

<p><strong>Quality Conscious Software Delivery</strong> is a framework built on the premise that quality comes from consciousness, not process. Its Agentic evolution extends that premise into the age of AI.</p>

<hr class="qcsd-sep">

<h2>The Framework</h2>

<p><strong>Quality Conscious Software Delivery</strong> grew out of years of experimentation with real delivery teams. I tested ideas, failed, learned, tried again — and eventually arrived at something that worked. It won the <a href="https://huddle.eurostarsoftwaretesting.com/resources/test-management/quality-conscious-software-delivery/" target="_blank" rel="noopener">EuroSTAR Best Paper Award in 2022</a>, one of only 26 recipients in the conference's 30-year history, and has since been adopted by teams across three continents.</p>

<p>At its core, QCSD rejects the idea that quality can be achieved through process alone. It introduces a model that reframes quality as an interplay of three forces most organisations never think about together — and a structured cycle that turns consciousness into craft and craft into discipline. The result is a fundamentally different way of embedding quality into software delivery: not as a gate at the end, but as a way of thinking that every person on the team carries into every decision they make.</p>

<div class="qcsd-pull">
  <p>Delivery of quality products by quality-conscious people using quality-empowering processes.</p>
  <cite>— The QCSD goal</cite>
</div>

<p>The details of the framework — its models, its implementation patterns, its adaptation to different contexts — are what I share in my <a href="/talks/">workshops, tutorials, and keynotes</a> at conferences worldwide. Each engagement is tailored to the audience: from half-day executive briefings to full-day hands-on tutorials where teams leave with a concrete implementation roadmap.</p>

<hr class="qcsd-sep">

<h2>Agentic QCSD</h2>

<p>Then came AI agents. And with them, a question the industry is mostly answering badly: <em>what happens to quality consciousness when autonomous systems become part of the delivery team?</em></p>

<p>The default answer has been predictable. Use AI to generate more test cases. Automate more of the pipeline. Chase volume again, but this time with large language models. The Faster Horse cycle with a new engine.</p>

<p>Agentic QCSD starts from a fundamentally different place. Not <em>how can agents produce more tests</em>, but <em>how can agents carry quality consciousness</em> — thinking strategically about quality at every stage of the software delivery lifecycle, the way a thoughtful senior engineer would, but at a speed and scale no human team can sustain.</p>

<p>This isn't another "AI for testing" play. It's a principled architecture for embedding quality consciousness into autonomous systems — grounded in what I call <strong>Designed Agency</strong>. The approach covers the full SDLC from ideation through production telemetry, with human-in-the-loop quality gates where they matter most.</p>

<div class="qcsd-pull">
  <p>Not replacement of human testers, but a genuine amplification of human quality consciousness — operating at the speed and scale that modern delivery demands.</p>
  <cite>— On Designed Agency</cite>
</div>

<p>I'm currently delivering Agentic QCSD as full-day tutorials and workshops at conferences including <a href="https://agiletestingdays.com/2026/session/the-70-problem/" target="_blank" rel="noopener">Agile Testing Days</a>, <a href="https://hustef.com/lalit-dragan_2026/" target="_blank" rel="noopener">HUSTEF</a>, and <a href="https://embedded.qatest.org/ponentes/lalitkumar-bhamare/?lang=en" target="_blank" rel="noopener">QA&Test Embedded</a>. If you're interested in what this looks like in practice, those are good places to start.</p>

<hr class="qcsd-sep">

<h2>Credentials</h2>

<div class="qcsd-trio">
  <div class="qcsd-trio-item">
    <h3>EuroSTAR Best Paper</h3>
    <p>One of only 26 recipients in the conference's 30-year history. Awarded for the original QCSD paper in 2022.</p>
  </div>
  <div class="qcsd-trio-item">
    <h3>Taking Testing Seriously</h3>
    <p>Contributing author in the book by <a href="https://www.wiley.com/en-us/Taking+Testing+Seriously%3A+The+Rapid+Software+Testing+Approach-p-9781394253197" target="_blank" rel="noopener">James Bach and Michael Bolton</a>, published by Wiley.</p>
  </div>
  <div class="qcsd-trio-item">
    <h3>3 Continents</h3>
    <p>QCSD has been adopted by delivery teams across Europe, Asia, and North America.</p>
  </div>
</div>

<hr class="qcsd-sep">

<h2>Work With Me</h2>

<p>I deliver QCSD and Agentic QCSD through <a href="/talks/">keynotes, full-day workshops, and executive coaching</a> — tailored to your organisation's context, maturity, and ambitions. Whether you're building a quality engineering capability from scratch, navigating AI adoption in your delivery pipeline, or looking for a keynote that changes how your organisation thinks about quality.</p>

<p><a href="https://www.linkedin.com/in/lalitkumarbhamare/" target="_blank" rel="noopener"><strong>Let's talk.</strong></a></p>

</div>
