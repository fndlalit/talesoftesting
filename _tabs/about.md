---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
---

<style>
  /* ───── Foundation ───── */
  .about-page { max-width: 860px; margin: 0 auto; }

  /* ───── Opening ───── */
  .about-opener {
    text-align: center;
    margin-bottom: 3rem;
    padding: 0 1rem;
  }
  .about-opener .eyebrow {
    color: #50b8a6;
    font-size: 0.82rem;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 0.8rem;
  }
  .about-opener h1 {
    font-size: 2.6rem;
    font-weight: 900;
    color: var(--heading-color, #1a1a2e);
    line-height: 1.15;
    margin: 0 0 1.2rem;
  }
  .about-opener .lead {
    font-size: 1.15rem;
    line-height: 1.85;
    color: var(--text-color, #555);
    max-width: 720px;
    margin: 0 auto;
  }
  @media (max-width: 576px) {
    .about-opener h1 { font-size: 1.8rem; }
  }

  /* ───── Stats ribbon ───── */
  .stats-ribbon {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.2rem;
    margin: 2.5rem 0 3rem;
    padding: 2rem 1.5rem;
    background: linear-gradient(135deg, #0d1b2a 0%, #1b2d45 100%);
    border-radius: 16px;
    text-align: center;
  }
  .stats-ribbon .stat-num {
    font-size: 2.2rem;
    font-weight: 900;
    color: #50b8a6;
    line-height: 1;
    margin-bottom: 0.3rem;
  }
  .stats-ribbon .stat-label {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: rgba(255,255,255,0.65);
    font-weight: 600;
  }
  @media (max-width: 576px) {
    .stats-ribbon { grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }
    .stats-ribbon .stat-num { font-size: 1.8rem; }
  }

  /* ───── Section styling ───── */
  .about-section {
    margin-bottom: 3rem;
  }
  .section-label {
    color: #50b8a6;
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 0.5rem;
  }
  .section-heading {
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--heading-color, #1a1a2e);
    margin-bottom: 1rem;
    line-height: 1.3;
  }
  .section-prose {
    font-size: 1.02rem;
    line-height: 1.85;
    color: var(--text-color, #555);
  }
  .section-prose a {
    color: #50b8a6;
    text-decoration: none;
    border-bottom: 1px dashed #50b8a6;
    transition: border-color 0.2s;
  }
  .section-prose a:hover {
    border-bottom-style: solid;
  }

  /* ───── Philosophy block ───── */
  .philosophy-block {
    position: relative;
    background: linear-gradient(135deg, #f0faf8 0%, #e8f4f1 50%, #f5f9f8 100%);
    border-radius: 16px;
    padding: 2.5rem 2.5rem 2.5rem 3rem;
    margin: 2.5rem 0 3rem;
    border-left: 5px solid #50b8a6;
  }
  .philosophy-block::before {
    content: "\201C";
    position: absolute;
    top: 0.3rem;
    left: 1rem;
    font-size: 4rem;
    color: #50b8a6;
    opacity: 0.3;
    font-family: Georgia, serif;
    line-height: 1;
  }
  .philosophy-block p {
    font-size: 1.08rem;
    line-height: 1.85;
    color: var(--heading-color, #1a1a2e);
    margin: 0;
    font-style: italic;
  }
  .philosophy-block .phil-attr {
    margin-top: 1rem;
    font-style: normal;
    font-size: 0.88rem;
    color: #50b8a6;
    font-weight: 700;
  }
  @media (max-width: 576px) {
    .philosophy-block { padding: 2rem 1.5rem 2rem 2rem; }
  }

  /* ───── Awards showcase ───── */
  .awards-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.2rem;
    margin: 1.5rem 0;
  }
  @media (max-width: 576px) {
    .awards-grid { grid-template-columns: 1fr; }
  }
  .award-card {
    background: var(--card-bg, #fff);
    border: 1px solid var(--card-border-color, #e0e0e0);
    border-radius: 14px;
    padding: 1.5rem;
    display: flex;
    gap: 1rem;
    align-items: flex-start;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .award-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  }
  .award-icon {
    font-size: 2rem;
    flex-shrink: 0;
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, #50b8a6 0%, #3d9e8f 100%);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
  }
  .award-card h4 {
    margin: 0 0 0.25rem;
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--heading-color, #1a1a2e);
  }
  .award-card p {
    margin: 0;
    font-size: 0.85rem;
    color: var(--text-muted-color, #888);
    line-height: 1.5;
  }

  /* ───── Timeline ───── */
  .timeline {
    position: relative;
    padding-left: 2.5rem;
    margin: 1.5rem 0;
  }
  .timeline::before {
    content: '';
    position: absolute;
    left: 0.6rem;
    top: 0.5rem;
    bottom: 0.5rem;
    width: 2px;
    background: linear-gradient(to bottom, #50b8a6, rgba(80,184,166,0.15));
  }
  .tl-item {
    position: relative;
    margin-bottom: 2rem;
    padding-bottom: 0.5rem;
  }
  .tl-item::before {
    content: '';
    position: absolute;
    left: -2.1rem;
    top: 0.45rem;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #50b8a6;
    border: 3px solid var(--card-bg, #fff);
    box-shadow: 0 0 0 2px #50b8a6;
  }
  .tl-item.current::before {
    background: #fff;
    box-shadow: 0 0 0 3px #50b8a6;
    animation: pulse-dot 2s infinite;
  }
  @keyframes pulse-dot {
    0%, 100% { box-shadow: 0 0 0 3px #50b8a6; }
    50% { box-shadow: 0 0 0 6px rgba(80,184,166,0.3); }
  }
  .tl-period {
    font-size: 0.78rem;
    font-weight: 700;
    color: #50b8a6;
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  .tl-role {
    font-size: 1.05rem;
    font-weight: 800;
    color: var(--heading-color, #1a1a2e);
    margin: 0.15rem 0;
  }
  .tl-org {
    font-size: 0.92rem;
    color: var(--text-color, #555);
    margin-bottom: 0.3rem;
  }
  .tl-desc {
    font-size: 0.9rem;
    color: var(--text-muted-color, #888);
    line-height: 1.65;
  }

  /* ───── Publications ───── */
  .pub-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.2rem;
    margin: 1.5rem 0;
  }
  .pub-card {
    border: 1px solid var(--card-border-color, #e0e0e0);
    border-radius: 14px;
    padding: 1.5rem;
    background: var(--card-bg, #fff);
    transition: transform 0.2s, box-shadow 0.2s;
    text-decoration: none;
    color: inherit;
    display: block;
  }
  .pub-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  }
  .pub-card .pub-type {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #50b8a6;
    font-weight: 700;
    margin-bottom: 0.5rem;
  }
  .pub-card h4 {
    font-size: 1rem;
    font-weight: 700;
    color: var(--heading-color, #1a1a2e);
    margin: 0 0 0.4rem;
    line-height: 1.35;
  }
  .pub-card .pub-meta {
    font-size: 0.85rem;
    color: var(--text-muted-color, #888);
    line-height: 1.5;
  }

  /* ───── Expertise pills ───── */
  .expertise-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin: 1rem 0;
  }
  .expertise-cloud span {
    padding: 0.45rem 1.1rem;
    border-radius: 100px;
    font-size: 0.85rem;
    font-weight: 600;
    transition: transform 0.15s;
  }
  .expertise-cloud span:hover {
    transform: scale(1.05);
  }
  .expertise-cloud .primary {
    background: linear-gradient(135deg, #50b8a6 0%, #3d9e8f 100%);
    color: #fff;
  }
  .expertise-cloud .secondary {
    background: var(--card-bg, #fff);
    border: 1.5px solid #50b8a6;
    color: #50b8a6;
  }

  /* ───── Industries ───── */
  .industry-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin: 1rem 0;
  }
  .industry-row span {
    font-size: 0.88rem;
    color: var(--text-color, #555);
    padding: 0.4rem 0;
    border-bottom: 1px dashed rgba(80,184,166,0.4);
  }

  /* ───── Education ───── */
  .edu-row {
    display: flex;
    gap: 1.2rem;
    flex-wrap: wrap;
    margin: 1rem 0;
  }
  .edu-item {
    flex: 1;
    min-width: 240px;
    padding: 1.2rem 1.4rem;
    border: 1px solid var(--card-border-color, #e0e0e0);
    border-radius: 14px;
    background: var(--card-bg, #fff);
  }
  .edu-item h4 {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--heading-color, #1a1a2e);
    margin: 0 0 0.2rem;
  }
  .edu-item p {
    margin: 0;
    font-size: 0.85rem;
    color: var(--text-muted-color, #888);
    line-height: 1.5;
  }
  .cert-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1rem;
  }
  .cert-list span {
    font-size: 0.8rem;
    padding: 0.3rem 0.8rem;
    border-radius: 6px;
    background: #f0faf8;
    color: #3d9e8f;
    font-weight: 600;
  }

  /* ───── Connect ───── */
  .connect-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin: 1.2rem 0;
  }
  .connect-row a {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.65rem 1.3rem;
    border: 1.5px solid var(--card-border-color, #e0e0e0);
    border-radius: 100px;
    text-decoration: none;
    color: var(--heading-color, #1a1a2e);
    font-weight: 600;
    font-size: 0.88rem;
    background: var(--card-bg, #fff);
    transition: all 0.2s;
  }
  .connect-row a:hover {
    border-color: #50b8a6;
    color: #50b8a6;
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(80,184,166,0.15);
  }

  /* ───── Divider ───── */
  .section-divider {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, var(--card-border-color, #e0e0e0), transparent);
    margin: 3rem 0;
  }
</style>

<div class="about-page">

<!-- ═══════ OPENING ═══════ -->
<div class="about-opener">
  <div class="eyebrow">Engineering Leader · Speaker · Author</div>
  <h1>Lalitkumar Bhamare</h1>
  <p class="lead">
    For over 18 years, I've worked at the intersection of engineering quality, leadership, and human curiosity. I believe the best software isn't just tested — it's <em>thought about</em> deeply. I build teams that think that way, and I speak around the world about why it matters.
  </p>
</div>

<!-- ═══════ STATS ═══════ -->
<div class="stats-ribbon">
  <div>
    <div class="stat-num">18+</div>
    <div class="stat-label">Years</div>
  </div>
  <div>
    <div class="stat-num">16</div>
    <div class="stat-label">Countries</div>
  </div>
  <div>
    <div class="stat-num">500+</div>
    <div class="stat-label">Engineers Trained</div>
  </div>
  <div>
    <div class="stat-num">20+</div>
    <div class="stat-label">Teams Led</div>
  </div>
</div>

<!-- ═══════ PHILOSOPHY ═══════ -->
<div class="philosophy-block">
  <p>Most organisations chase quality through process. I've spent my career proving it comes from <strong>consciousness</strong> — a deliberate, human-centred awareness woven into every stage of delivery. That conviction became QCSD, won a EuroSTAR Best Paper award, and has since shaped how teams across three continents think about building software.</p>
  <div class="phil-attr">— On Quality Conscious Software Delivery</div>
</div>

<!-- ═══════ AWARDS ═══════ -->
<div class="about-section">
  <div class="section-label">Recognition</div>
  <div class="section-heading">Awards & Milestones</div>

  <div class="awards-grid">
    <div class="award-card">
      <div class="award-icon">🏆</div>
      <div>
        <h4>QA Leader of the Year 2025</h4>
        <p>PractiTest — global recognition for leadership in quality engineering</p>
      </div>
    </div>
    <div class="award-card">
      <div class="award-icon">📄</div>
      <div>
        <h4>EuroSTAR Best Paper 2022</h4>
        <p>One of only 26 Best Paper awardees in 30 years of Europe's largest testing conference</p>
      </div>
    </div>
    <div class="award-card">
      <div class="award-icon">📘</div>
      <div>
        <h4>Contributing Author — Taking Testing Seriously</h4>
        <p>By James Bach &amp; Michael Bolton (Wiley) — the definitive RST book</p>
      </div>
    </div>
    <div class="award-card">
      <div class="award-icon">🎤</div>
      <div>
        <h4>Program Chair — Sparks 2025</h4>
        <p>Curating and directing the inaugural Sparks conference programme in Malaysia</p>
      </div>
    </div>
  </div>
</div>

<hr class="section-divider">

<!-- ═══════ WHAT I DO ═══════ -->
<div class="about-section">
  <div class="section-label">Focus</div>
  <div class="section-heading">What I Work On</div>
  <div class="section-prose">
    <p>I operate at the confluence of <strong>productivity engineering</strong>, <strong>quality coaching</strong>, and <strong>AI-driven delivery</strong>. Day to day, that means overseeing the full software delivery lifecycle — from ideation through production telemetry — while building engineering cultures that treat quality as everyone's responsibility, not a phase to endure.</p>
    <p>I created <strong>QCSD (Quality Conscious Software Delivery)</strong>, an award-winning framework that reframes quality from a gatekeeping activity into a delivery philosophy. I'm frequently invited to present this framework at international conferences, and it has been adopted by teams across industries ranging from e-commerce to banking.</p>
    <p>Through in-house trainings, public workshops, and conference sessions, I've trained over 500 engineers globally on agile development, testing, quality engineering, and AI topics.</p>
  </div>
</div>

<hr class="section-divider">

<!-- ═══════ JOURNEY ═══════ -->
<div class="about-section">
  <div class="section-label">Journey</div>
  <div class="section-heading">Career Timeline</div>

  <div class="timeline">
    <div class="tl-item current">
      <div class="tl-period">Nov 2021 — Present</div>
      <div class="tl-role">Productivity Engineering Manager & Quality Coach</div>
      <div class="tl-org">Accenture Song · Hamburg, Germany</div>
      <div class="tl-desc">Leading productivity engineering in the DevOps chapter — AI-based solutioning, quality governance, and full-lifecycle delivery from ideation to SRE.</div>
    </div>
    <div class="tl-item current">
      <div class="tl-period">Oct 2023 — Present</div>
      <div class="tl-role">Group Leader — Innovation & Thought Leadership</div>
      <div class="tl-org">Accenture EMEA · Quality Engineering Services</div>
      <div class="tl-desc">Shaping thought leadership in software testing and quality engineering across the entire EMEA region.</div>
    </div>
    <div class="tl-item">
      <div class="tl-period">Dec 2015 — Oct 2021</div>
      <div class="tl-role">Senior Software Test Engineer & Cluster QE Lead</div>
      <div class="tl-org">New Work SE (formerly XING) · Hamburg, Germany</div>
      <div class="tl-desc">Quality Engineering advocate across multiple product teams. Founding member of the Testing Community of Practice, contributing to test strategy, engineering guilds, and Quality Engineering Guardrails.</div>
    </div>
    <div class="tl-item">
      <div class="tl-period">Aug 2012 — Nov 2015</div>
      <div class="tl-role">Senior Test Analyst</div>
      <div class="tl-org">Barclays Investment Bank · Pune, India</div>
      <div class="tl-desc">Rapid Software Testing advisor, trainer, and coach across Barclays Capital. Led the Testing L&amp;D Team and served as Global Lead for the Test Strategy Community of Practice.</div>
    </div>
    <div class="tl-item">
      <div class="tl-period">2008 — 2012</div>
      <div class="tl-role">Software Test Engineer</div>
      <div class="tl-org">Various roles · India</div>
      <div class="tl-desc">Early career across life sciences, telecommunications, and e-governance domains — building the testing foundations that would inform QCSD.</div>
    </div>
  </div>
</div>

<hr class="section-divider">

<!-- ═══════ PUBLICATIONS ═══════ -->
<div class="about-section">
  <div class="section-label">Writing</div>
  <div class="section-heading">Publications</div>

  <div class="pub-cards">
    <a href="https://www.wiley.com/en-us/Taking+Testing+Seriously%3A+The+Rapid+Software+Testing+Approach-p-9781394253197" target="_blank" rel="noopener" class="pub-card">
      <div class="pub-type">Book</div>
      <h4>Taking Testing Seriously</h4>
      <div class="pub-meta">Contributing author — by James Bach &amp; Michael Bolton (Wiley)</div>
    </a>
    <a href="https://huddle.eurostarsoftwaretesting.com/resources/test-management/quality-conscious-software-delivery/" target="_blank" rel="noopener" class="pub-card">
      <div class="pub-type">Award-winning Paper</div>
      <h4>Quality Conscious Software Delivery</h4>
      <div class="pub-meta">EuroSTAR Best Paper 2022 — a framework for embedding quality consciousness into delivery</div>
    </a>
    <a href="http://qablog.practitest.com/state-of-testing/" target="_blank" rel="noopener" class="pub-card">
      <div class="pub-type">Annual Report</div>
      <h4>State of Testing Report</h4>
      <div class="pub-meta">Co-creator &amp; co-author — PractiTest + Tea-time with Testers (2013–Present)</div>
    </a>
  </div>
</div>

<hr class="section-divider">

<!-- ═══════ COMMUNITY ═══════ -->
<div class="about-section">
  <div class="section-label">Community</div>
  <div class="section-heading">Leadership & Giving Back</div>
  <div class="section-prose">
    <p>I'm the <strong>CEO, Co-founder, and Chief Editor</strong> of <a href="https://www.teatimewithtesters.com/" target="_blank" rel="noopener">Tea-time with Testers Magazine</a> (2011–Present) — a globally recognised English-language publication known for its quality content and significant contribution to advancing the software testing craft.</p>
    <p>I served as <strong>Director/VP of Education</strong> at the <a href="https://associationforsoftwaretesting.org/" target="_blank" rel="noopener">Association for Software Testing, USA</a> (2020–2024), overseeing the organisation's BBST education programme. I've also served as <strong>Advisory Board Member</strong> for AskUI (2021–2023), a German startup in AI-based automation, and as <strong>Peer Advisor</strong> with James Bach for Rapid Software Testing courses.</p>
  </div>
</div>

<hr class="section-divider">

<!-- ═══════ EXPERTISE ═══════ -->
<div class="about-section">
  <div class="section-label">Expertise</div>
  <div class="section-heading">What I Bring to the Table</div>

  <div class="expertise-cloud">
    <span class="primary">Productivity Engineering</span>
    <span class="primary">Quality Engineering</span>
    <span class="primary">AI & Automation</span>
    <span class="primary">Engineering Leadership</span>
    <span class="secondary">Test Management</span>
    <span class="secondary">Quality Coaching</span>
    <span class="secondary">Digital Transformation</span>
    <span class="secondary">Programme & Project Management</span>
  </div>

  <div class="section-heading" style="font-size: 1.1rem; margin-top: 2rem;">Industries</div>
  <div class="industry-row">
    <span>E-commerce</span>
    <span>Banking & Finance</span>
    <span>Pre-sales</span>
    <span>Telecommunications</span>
    <span>Social Networking</span>
    <span>Media & Entertainment</span>
    <span>E-Governance</span>
    <span>Life Sciences</span>
  </div>
</div>

<hr class="section-divider">

<!-- ═══════ EDUCATION ═══════ -->
<div class="about-section">
  <div class="section-label">Education</div>
  <div class="section-heading">Credentials</div>

  <div class="edu-row">
    <div class="edu-item">
      <h4>Bachelor of Engineering</h4>
      <p>Mechanical Engineering · Savitribai Phule Pune University, India (2008)</p>
    </div>
  </div>

  <div class="cert-list">
    <span>SAFe DevOps Practitioner</span>
    <span>Rapid Software Testing</span>
    <span>BBST Lead Instructor</span>
    <span>BBST Foundations</span>
    <span>ISTQB Foundations</span>
  </div>
</div>

<hr class="section-divider">

<!-- ═══════ CONNECT ═══════ -->
<div class="about-section">
  <div class="section-label">Connect</div>
  <div class="section-heading">Let's Talk</div>
  <div class="section-prose" style="margin-bottom: 1rem;">
    <p>I'm always happy to connect — whether it's about a speaking opportunity, a quality engineering challenge, or just a good conversation about the craft.</p>
  </div>

  <div class="connect-row">
    <a href="https://www.linkedin.com/in/lalitkumarbhamare/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> LinkedIn</a>
    <a href="https://twitter.com/Lalitbhamare" target="_blank" rel="noopener"><i class="fab fa-twitter"></i> @Lalitbhamare</a>
    <a href="https://twitter.com/Ttimewidtesters" target="_blank" rel="noopener"><i class="fab fa-twitter"></i> @Ttimewidtesters</a>
    <a href="https://talesoftesting.com/" target="_blank" rel="noopener"><i class="fas fa-globe"></i> talesoftesting.com</a>
  </div>
</div>

</div>
