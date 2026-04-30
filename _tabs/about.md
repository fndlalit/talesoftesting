---
title: About me
icon: fas fa-info-circle
order: 6
---

<style>
  /* Hide Chirpy's auto-generated page heading */
  article > h1 { display: none !important; }

  .ab-page-title {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 2rem;
    font-weight: 400;
    color: var(--heading-color, #1a1a2e);
    margin: 0 0 2.5rem;
    letter-spacing: -0.01em;
  }

  .ab { max-width: 720px; }
  .ab p { font-size: 1.05rem; line-height: 1.9; color: var(--text-color, #444); }
  .ab a { color: var(--heading-color, #1a1a2e); text-decoration: underline; text-decoration-color: #50b8a6; text-underline-offset: 3px; text-decoration-thickness: 1.5px; transition: text-decoration-color 0.2s; }
  .ab a:hover { text-decoration-color: var(--heading-color, #1a1a2e); }

  /* ── Hero ── */
  .ab-hero {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 2.8rem;
    align-items: start;
    margin-bottom: 1rem;
  }
  @media (max-width: 720px) {
    .ab-hero { grid-template-columns: 1fr; }
    .ab-hero-photo { max-width: 280px; }
  }
  .ab-hero-photo {
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.08);
  }
  .ab-hero .img-link { pointer-events: none; }
  .ab-hero-text {
    padding-top: 0.6rem;
  }
  .ab-hero-text p {
    font-size: 1.08rem;
    line-height: 1.85;
    color: var(--text-color, #444);
    margin: 0;
  }

  /* ── Pull quote ── */
  .ab-quote {
    margin: 2.8rem 0;
    padding: 0 0 0 1.5rem;
    border-left: 3px solid #50b8a6;
  }
  .ab-quote p {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.2rem;
    font-style: italic;
    line-height: 1.75;
    color: var(--heading-color, #1a1a2e);
    margin: 0;
  }

  /* ── Section heading ── */
  .ab h2 {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.5rem;
    font-weight: 400;
    font-style: italic;
    color: var(--heading-color, #1a1a2e);
    margin: 3rem 0 1.4rem;
    letter-spacing: -0.01em;
  }

  /* ── Separator ── */
  .ab-sep {
    border: none;
    height: 1px;
    background: var(--card-border-color, #e0e0e0);
    margin: 3rem 0;
    max-width: 60px;
  }

  /* ── Credential cards ── */
  .ab-cards { margin: 0.5rem 0 0; }
  .ab-card {
    display: grid;
    grid-template-columns: 44px 1fr;
    gap: 0 1.1rem;
    align-items: center;
    padding: 1rem 0;
    border-bottom: 1px solid var(--card-border-color, #eaeaea);
    text-decoration: none !important;
    transition: opacity 0.2s;
  }
  .ab-card:first-child { border-top: 1px solid var(--card-border-color, #eaeaea); }
  .ab-card:hover { opacity: 0.75; }
  .ab-card-icon {
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.15rem;
    color: #50b8a6;
    background: rgba(80,184,166,0.07);
    border-radius: 10px;
    flex-shrink: 0;
  }
  .ab-card strong {
    display: block;
    font-size: 0.95rem;
    color: var(--heading-color, #1a1a2e);
    margin-bottom: 0.15rem;
    line-height: 1.3;
  }
  .ab-card span {
    display: block;
    font-size: 0.83rem;
    color: var(--text-muted-color, #999);
    line-height: 1.45;
  }

  /* ── Connect ── */
  .ab-connect {
    margin-top: 1rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem 1.8rem;
  }
  .ab-connect a {
    font-size: 0.95rem;
    white-space: nowrap;
  }
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.ab-hero .shimmer').forEach(function(el) {
    el.classList.remove('shimmer');
  });
});
</script>

<div class="ab">

<h1 class="ab-page-title">Lalitkumar Bhamare</h1>

<div class="ab-hero">
  <img src="/assets/img/about-lalit.jpg" alt="Lalitkumar Bhamare" class="ab-hero-photo" width="900" height="1200" loading="eager">
  <div class="ab-hero-text">
    <p>For over eighteen years, I've worked at the intersection of software quality, engineering leadership, and human curiosity. I believe the best software isn't just tested - it's <em>thought about</em> deeply, cared about at every level from ideation till end user satisfaction, looked after from discovery to disaster recovery, by every person who touches it.</p>
    <p style="margin-top: 1.8rem;">I help building engineering teams where "quality is everyone's responsibility" is not just a slogan on the wall but a culture practically lived and pragmatically nurtured.</p>
  </div>
</div>

<p>I coach senior executives on leading with quality consciousness. And I speak at conferences around the world about why it matters.</p>

<div class="ab-quote">
  <p>Most organisations chase quality through process. I've spent my career proving it comes from consciousness - a deliberate, human-centred awareness woven into every stage of software delivery.</p>
</div>

<p>That conviction became <strong><a href="/qcsd/">Quality Conscious Software Delivery</a></strong> a.k.a. <strong><a href="/qcsd/">QCSD</a></strong>, an award-winning framework now adopted by teams across three continents. Its evolution, <strong>Agentic QCSD</strong>, extends that thinking into the age of AI agents, where quality consciousness becomes a design principle for autonomous systems. Through keynotes, full-day workshops, and executive coaching, I've trained over 1,000 engineers globally.</p>

<hr class="ab-sep">

<h2>Credentials</h2>

<div class="ab-cards">
  <a href="https://www.practitest.com/qa-leader-of-the-year-2025/" target="_blank" rel="noopener" class="ab-card">
    <div class="ab-card-icon"><i class="fas fa-trophy"></i></div>
    <div>
      <strong>Emerging QA Leader of the Year 2025</strong>
      <span>PractiTest, global recognition for leadership in quality engineering</span>
    </div>
  </a>
  <a href="https://huddle.eurostarsoftwaretesting.com/resources/test-management/quality-conscious-software-delivery/" target="_blank" rel="noopener" class="ab-card">
    <div class="ab-card-icon"><i class="fas fa-award"></i></div>
    <div>
      <strong>EuroSTAR Best Paper 2022</strong>
      <span>One of 26 recipients in the conference's 30-year history</span>
    </div>
  </a>
  <a href="https://www.wiley.com/en-us/Taking+Testing+Seriously%3A+The+Rapid+Software+Testing+Approach-p-9781394253197" target="_blank" rel="noopener" class="ab-card">
    <div class="ab-card-icon"><i class="fas fa-book"></i></div>
    <div>
      <strong>Taking Testing Seriously</strong>
      <span>Contributing author, James Bach &amp; Michael Bolton (Wiley)</span>
    </div>
  </a>
  <a href="https://www.teatimewithtesters.com/" target="_blank" rel="noopener" class="ab-card">
    <div class="ab-card-icon"><i class="fas fa-newspaper"></i></div>
    <div>
      <strong>Tea-time with Testers Magazine</strong>
      <span>CEO, Co-founder &amp; Chief Editor since 2011</span>
    </div>
  </a>
  <a href="http://qablog.practitest.com/state-of-testing/" target="_blank" rel="noopener" class="ab-card">
    <div class="ab-card-icon"><i class="fas fa-chart-bar"></i></div>
    <div>
      <strong>State of Testing Report</strong>
      <span>Co-creator &amp; co-author, published annually since 2013</span>
    </div>
  </a>
  <a href="https://associationforsoftwaretesting.org/" target="_blank" rel="noopener" class="ab-card">
    <div class="ab-card-icon"><i class="fas fa-university"></i></div>
    <div>
      <strong>Association for Software Testing</strong>
      <span>Director / VP of Education (2020–2024), BBST programme</span>
    </div>
  </a>
  <a href="https://rapid-software-testing.com/" target="_blank" rel="noopener" class="ab-card">
    <div class="ab-card-icon"><i class="fas fa-chalkboard-teacher"></i></div>
    <div>
      <strong>Rapid Software Testing</strong>
      <span>Peer Advisor with James Bach</span>
    </div>
  </a>
</div>

<hr class="ab-sep">

<h2>Connect</h2>

<p>Whether it's a speaking opportunity, a quality engineering challenge, or just a good conversation about the craft.</p>

<div class="ab-connect">
  <a href="https://www.linkedin.com/in/lalitkumarbhamare/" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i> LinkedIn</a>
  <a href="https://twitter.com/Lalitbhamare" target="_blank" rel="noopener"><i class="fab fa-twitter"></i> @Lalitbhamare</a>
  <a href="https://twitter.com/Ttimewidtesters" target="_blank" rel="noopener"><i class="fab fa-twitter"></i> @Ttimewidtesters</a>
  <a href="https://talesoftesting.com/" target="_blank" rel="noopener"><i class="fas fa-globe"></i> talesoftesting.com</a>
</div>

</div>
