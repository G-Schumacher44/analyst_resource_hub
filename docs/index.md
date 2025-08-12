<!-- Landing page written fully in HTML for precise layout/control -->
<div class="hero">
  <h1 style="color: white; font-weight: bold;">🗂 Analyst Resource Hub</h1>
  <div class="hero-actions">
    <a href="python/" class="md-button md-button--primary">Python Resources</a>
    <a href="python/05%20-%20Scripts/01%20-%20Python/" class="md-button md-button--primary">Tools & Scripts</a>
    <a href="workflow_projects/" class="md-button md-button--primary">Production & Projects</a>
    <a href="sql/" class="md-button md-button--primary">SQL & BI Tools</a>
  </div>
</div>

<div class="home-card">
  <h2>📚 About This Hub & Its Custodian</h2>
  <p>This site is a living resource, consisting of refined notes and study materials I compiled while earning certifications and building skills in data analysis, Python, SQL, and machine learning.</p>
  <p>Created as both a personal reference and a shared learning tool, it’s open to anyone looking to learn—and contributions are always welcome.</p>
  <ul>
    <li>Cleaning & QA</li>
    <li>Modeling & evaluation</li>
    <li>SQL optimization & dashboard design</li>
    <li>Project delivery & documentation best practices</li>
  </ul>
  <p>Maintained by Garrett Schumacher. Have ideas or spot an issue? Open a ticket on <a href="https://github.com/G-Schumacher44/analyst_resource_hub/issues">GitHub Issues</a>.</p>
</div>

<!-- Quick section grid -->
<style>
  /* GS Analytics palette pulled from logo */
  :root {
    --gs-navy: #0b1a24;     /* deep background */
    --gs-blue: #1e65b0;     /* G (blue) */
    --gs-teal: #00a39a;     /* S (teal) */
    --gs-surface: #142635;  /* card surface */
    --gs-text: #ffffff;     /* primary text */
  }

  .home-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.25rem;
    margin-top: 1rem;
  }

  @media (max-width: 1200px) {
    .home-grid {
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    }
  }

  .home-card {
    border: 1px solid transparent;
    border-radius: 12px;
    padding: 1rem 1rem 1.25rem;
    background: var(--gs-surface);
    color: var(--gs-text);
    box-shadow: 0 8px 18px rgba(0,0,0,0.25);
  }

  /* Normalize card heights and layout */
  .home-card {
    display: flex;
    flex-direction: column;
    min-height: clamp(220px, 28vh, 320px);
  }

  /* Clamp the first blurb paragraph to two lines to avoid tall cards */
  .home-card p:first-of-type {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  /* Keep the button stack anchored at the bottom for even-looking cards */
  .home-card .links {
    margin-top: auto;
  }

  /* Slightly tighten buttons so they don’t bloat card height */
  .home-card .md-button {
    padding: 0.35rem 0.75rem;
    font-size: 0.9rem;
    line-height: 1.2;
  }

  /* On smaller screens, let cards auto-size naturally */
  @media (max-width: 900px) {
    .home-card {
      min-height: auto;
    }
  }
  .home-card h2 { margin: 0 0 .5rem 0; font-size: 1.1rem; }
  .home-card p { margin: 0 0 .75rem 0; opacity: 1; }
  .home-card .links { display: flex; flex-direction: column; gap: .35rem; }
  .home-card .links a { text-decoration: none; color: var(--gs-text); }

  .footer-actions { margin-top: 2rem; text-align: center; }
  .footer-actions a { margin: .25rem; }

  /* Center hero content and apply GS gradient */
  .hero {
    text-align: center;
    background: linear-gradient(135deg, #123a66, #00635c);
    color: var(--gs-text);
    padding: 2.75rem 1rem 2.25rem 1rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 10px 22px rgba(0,0,0,0.25);
  }
  .hero-actions {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.7rem;
    justify-items: stretch;
    align-items: stretch;
    margin: 0 auto 0 auto;
    max-width: 800px;
  }
  .hero-actions .md-button {
    margin: 0;
    width: 100%;
    box-sizing: border-box;
    justify-self: stretch;
    align-self: stretch;
    text-align: center;
    min-width: 0;
  }
  @media (max-width: 900px) {
    .hero-actions {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  @media (max-width: 600px) {
    .hero-actions {
      grid-template-columns: 1fr;
    }
  }

  /* Subtle rounding for all buttons and apply brand colors */
  .hero .md-button,
  .links .md-button,
  .footer-actions .md-button {
    border-radius: 6px;
    border: none;
  }

  /* Reduce button height and padding for hero and links */
  .hero-actions .md-button,
  .links .md-button {
    padding: 0.4rem 0.8rem;
    font-size: 0.9rem;
  }

  /* Primary buttons: match card background for consistency */
  .md-button--primary {
    background: var(--gs-surface) !important;
    color: var(--gs-text) !important;
  }
  .md-button--primary:hover {
    /* Slightly lighter shade for feedback */
    background: #20384e !important;
  }

  /* Secondary buttons: navy surface with subtle outline */
  .home-card .md-button:not(.md-button--primary),
  .footer-actions .md-button:not(.md-button--primary) {
    background: var(--gs-navy);
    color: var(--gs-text);
    border: 1px solid rgba(255,255,255,0.15);
  }
  .home-card .md-button:not(.md-button--primary):hover,
  .footer-actions .md-button:not(.md-button--primary):hover {
    border-color: rgba(255,255,255,0.35);
  }
</style>

<div class="home-grid">
  <div class="home-card">
    <h2>🐍 Python Resources</h2>
    <p>QuickRefs, EDA, cleaning, modeling, and runnable scripts.</p>
    <div class="links">
      <a class="md-button" href="python/01%20-%20QuickRef/">QuickRef</a>
      <a class="md-button" href="python/02%20-%20Data%20Wrangling%20%26%20EDA/">Data Wrangling & EDA</a>
      <a class="md-button" href="python/03%20-%20Cleaning/">Cleaning</a>
      <a class="md-button" href="python/04%20-%20Machine%20Learning%20Models/">Machine Learning Models</a>
    </div>
  </div>

  <div class="home-card">
    <h2>🛠️ Tools & Scripts</h2>
    <p>Starter scripts and boilerplate for EDA, cleaning, modeling, and utilities.</p>
    <div class="links">
      <a class="md-button" href="python/05%20-%20Scripts/01%20-%20Python/02%20-%20EDA/">EDA Scripts</a>
      <a class="md-button" href="python/05%20-%20Scripts/01%20-%20Python/03%20-%20Cleaning/">Cleaning Scripts</a>
      <a class="md-button" href="python/05%20-%20Scripts/01%20-%20Python/04%20-%20Machine%20Learning%20Models/">Modeling Scripts</a>
      <a class="md-button" href="python/05%20-%20Scripts/01%20-%20Python/05%20-%20Utilities/">Utilities</a>
    </div>
  </div>

  <div class="home-card">
    <h2>🗄️ SQL & BI Tools</h2>
    <p>Guidebooks, BigQuery patterns, and Looker Studio best practices.</p>
    <div class="links">
      <a class="md-button" href="sql/01%20-%20Guidebooks/">Guidebooks</a>
      <a class="md-button" href="sql/02%20-%20BigQuery%20and%20Looker/01%20-%20BigQuery/">BigQuery</a>
      <a class="md-button" href="sql/02%20-%20BigQuery%20and%20Looker/02%20-%20Looker%20Studio/">Looker Studio</a>
    </div>
  </div>

  <div class="home-card">
    <h2>📦 Production & Projects</h2>
    <p>Project scaffolds, delivery checklists, and pipelines.</p>
    <div class="links">
      <a class="md-button" href="workflow_projects/">Projects Hub</a>
    </div>
  </div>
</div>

<div class="footer-actions">
  <a href="https://github.com/G-Schumacher44/analyst_resource_hub" class="md-button md-button--primary">⬇️ Download Repository</a>
  <a href="https://github.com/G-Schumacher44/analyst_resource_hub/fork" class="md-button">🔧 Contribute on GitHub</a>
</div>
