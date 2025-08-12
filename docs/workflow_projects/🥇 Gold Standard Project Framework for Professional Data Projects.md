
# Gold Standard for Data Projects

This guide outlines modular, reusable, real-world project steps for any serious data science, analytics, or scientific modeling work — based on operational best practices and scientific credibility standards.

---

# 1. 📜 Problem Framing
- [ ] Define the business/scientific question clearly.
- [ ] Identify operational constraints (sample size, data collection limits, field realities).
- [ ] State the intended user or stakeholder audience.

---

# 2. 📚 Data Context and Risk Acknowledgment
- [ ] Determine if working with sample data or population data.
- [ ] Explicitly document sampling frame and potential biases (geographic, temporal, measurement).
- [ ] Generalization limitations framed clearly at the beginning.

---

# 3. 🛠 Data Loading and Sanity Validation
- [ ] Load dataset.
- [ ] Check schema (columns present and correctly named).
- [ ] Validate key fields:
  - Categorical typos (species, sex, colony, etc.)
  - Numerical plausibility (mass, flipper size, transaction amount ranges)
  - Timestamp plausibility (dates parsed, correct years)
- [ ] Flag and correct or drop corrupt records.

---

# 4. 📚 Sampling Context Reframing
- [ ] Restate sampling limitations inside EDA and modeling notebooks.
- [ ] Clarify that reported results are estimates, not universal truths.
- [ ] Plan to use inferential statistics (t-tests, p-values, confidence intervals) to handle uncertainty.

---

# 5. 📊 Exploratory Data Analysis (EDA)
- [ ] Summarize structure: counts, means, medians, standard deviations.
- [ ] Visualize distributions (histograms, boxplots).
- [ ] Explore relationships (scatterplots, correlation matrices).
- [ ] Segment analysis by important groups:
  - Biological projects → Species, Colony
  - Business projects → Customer Segments, Regions
- [ ] Identify missingness patterns and early outliers.
- [ ] Avoid cleaning inside EDA — just exploration.

---

# 6. 🛠 Production Cleaning Planning and Execution
- [ ] Build modular, scripted cleaning functions or pipelines.
- [ ] Define cleaning rules transparently:
  - Drop conditions
  - Imputation decisions (only if justified)
  - Handling biologically or operationally implausible records
- [ ] Save cleaned version separately (never overwrite raw).

---

# 7. 🧬 Feature Engineering (for Modeling)
- [ ] Create biologically or operationally meaningful features:
  - Interactions (species × flipper length)
  - Ratios (mass deviations, price per unit)
- [ ] Encode categorical variables properly.
- [ ] Normalize or scale features if required for modeling.

---

# 8. 📈 Modeling (Prediction, Classification, Analysis)
- [ ] Choose models aligned to project goals (simple, interpretable if possible).
- [ ] Validate models carefully:
  - Cross-validation
  - Train-test splits
- [ ] Frame outputs relative to uncertainty.
- [ ] Use inferential statistics where applicable to support findings.

---

# 9. 📊 Result Summarization and Interpretation
- [ ] Summarize results relative to original business or scientific questions.
- [ ] Include uncertainty quantification (confidence intervals, standard errors).
- [ ] Report limitations openly (sample size, modeling assumptions).
- [ ] Provide clear, actionable recommendations — not just raw numbers.

---

# 10. 📚 Final Documentation and Reporting
- [ ] Create modular deliverables:
  - Cleaned dataset
  - Modular notebooks/scripts
  - README with project overview, data notes, findings
  - Executive summary report (Markdown or PDF)
- [ ] Include a "Future Work" section:
  - Where to expand
  - How better data could improve models

---

# 🛡️ Professional Guardrails Always Active
- No silent data manipulations.
- No overgeneralization from samples without confidence quantification.
- No biological/operational trait imputation without explicit justification.
- All assumptions, limitations, and risks stated clearly in documentation.

---

# 🧘‍♂️ Final Reminder

✅ **Follow these steps across any serious project — and you’ll build work that survives professional review, supports real decisions, and earns serious career trust.**

---

# 📚 Inspired By:
- Field Conservation Data Standards (Oceanites, IUCN Red List)
- Scientific Python Best Practices
- Professional Applied Data Science Workflows (DrivenData, DSSG, Zindi)
- Real-World Ecological Monitoring Protocols