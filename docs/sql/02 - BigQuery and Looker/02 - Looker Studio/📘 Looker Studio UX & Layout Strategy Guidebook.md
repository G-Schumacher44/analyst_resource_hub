___
🎯 Purpose

This guidebook covers **dashboard layout and UX best practices** in Looker Studio. It focuses on layout grids, visual hierarchy, card prioritization, mobile responsiveness, and cognitive load reduction.

---

## 🧱 1. Grid-Based Layout Design

| Layout Rule                                                     | Why It Matters                                   |
| --------------------------------------------------------------- | ------------------------------------------------ |
| Use **consistent columns** (e.g., 2, 3, or 4 even-width blocks) | Avoids jagged layout and increases readability   |
| Align charts vertically by type                                 | Easier for users to scan trends, then breakdowns |
| Avoid floating components                                       | Anchored layouts guide user flow                 |

### ✅ Recommended Structure

```
[ Row 1: KPIs (Scorecards) ]
[ Row 2: Time Trends (Line/Bar) ]
[ Row 3: Breakdowns (Bar, Table, Pie) ]
[ Row 4: Filters + Drilldowns ]
```

---

## 🧭 2. Information Hierarchy

| Position | Content                                    |
| -------- | ------------------------------------------ |
| Top Left | Primary KPI (most important)               |
| Top Row  | Supporting metrics, high-level trendline   |
| Middle   | Behavioral comparisons or grouped visuals  |
| Bottom   | Raw tables, explanatory footnotes, filters |

✔️ Apply F-shaped or Z-pattern visual flow when in doubt

---

## 🎯 3. KPI Placement Strategy

* Use **scorecards** with change vs previous period (`% change`) for emphasis
* Color-code performance (green = up, red = down) sparingly
* Include last updated timestamp at top or footer

```text
KPI block example:
[ Revenue: $120k ] [+6% MoM]
[ Active Users: 1.2k ] [+2.3% vs last week]
```

---

## 🖼️ 4. Visual Cleanliness Guidelines

| Element       | UX Best Practice                                       |
| ------------- | ------------------------------------------------------ |
| Axis titles   | Always included, clear labels                          |
| Legends       | Use only when colors repeat or aren’t self-explanatory |
| Chart borders | Avoid unless needed to separate dense visuals          |
| Background    | Use white or light gray, never gradients               |

✔️ Remove chart clutter — prioritize white space and cognitive breathing room

---

## 📱 5. Responsive / Mobile Dashboarding

* Keep card widths to minimum unit size (avoid horizontal scroll)
* Stack filters vertically on mobile; hide if they clutter
* Test dashboard preview in "fit to width" and device modes
* Use toggleable **report pages** (tabs) to reduce single-page clutter

---

## ✅ UX Checklist

* [ ] KPIs clearly visible at the top
* [ ] Consistent visual grid used (rows, alignment)
* [ ] Font, color, and spacing are standardized
* [ ] Tables and filters placed at the bottom or in appendix tabs
* [ ] Dashboard previewed in narrow (mobile) and wide modes

---

## 💡 Tip

> “If a stakeholder can’t find the answer in 10 seconds — it’s a layout issue, not a data issue.”
