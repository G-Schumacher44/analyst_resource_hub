# ================================
# Churn Rate by Flag Score Plot Utility
# ================================

def plot_churn_by_flag_score(df, flag_cols=["burnout_risk", "plateau_risk", "lowpaid_loyal"], churn_col="churned"):
    """
    Plot churn rate by cumulative risk score (sum of binary flags).

    Parameters:
    - df: DataFrame with flag columns and churn label
    - flag_cols: list of binary flag columns to include in score
    - churn_col: name of churn label column (default: 'churned')
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Score and aggregate
    df["churn_risk_score"] = df[flag_cols].sum(axis=1)
    score_summary = df.groupby("churn_risk_score")[churn_col].agg(["mean", "count"]).reset_index()
    score_summary.columns = ["risk_score", "churn_rate", "count"]

    # Labeling
    score_summary["label"] = score_summary["risk_score"].map({
        0: "None", 1: "1 Flag", 2: "2 Flags", 3: "3 Flags"
    })

    # Plot setup
    plt.figure(figsize=(9, 5))
    palette = sns.color_palette("Reds", n_colors=4)
    ax = sns.barplot(data=score_summary, x="label", y="churn_rate", palette=palette)

    # Annotate churn percentages
    for i, bar in enumerate(ax.patches):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.02,
            f"{height:.0%}",
            ha="center", va="bottom", fontsize=11, weight="bold"
        )

    # Add average churn reference line
    avg_churn = df[churn_col].mean()
    ax.axhline(avg_churn, ls="--", color="gray")
    ax.text(
        len(score_summary) - 0.5, avg_churn + 0.01,
        f"↕ Avg Churn: {avg_churn:.0%}",
        ha="right", color="gray", fontsize=10
    )

    # Title and labels
    ax.set_title("🧮 Churn Rate by Accumulated Risk Flags", fontsize=14)
    ax.set_xlabel("Number of Active Risk Flags")
    ax.set_ylabel("Churn Rate")
    plt.ylim(0, 1)
    plt.tight_layout()

    # Footnote with group sizes
    counts = ", ".join(f"{row['label']}: {row['count']}" for _, row in score_summary.iterrows())
    plt.figtext(0.5, -0.05, f"📦 Employees per Group — {counts}", ha="center", fontsize=9, color="gray")

    plt.show()
# ================================
# Plateau Risk Churn Plot Utility
# ================================

def plot_plateau_risk_churn(df):
    """
    Plots churn rate for employees flagged with plateau risk vs. those not flagged.

    Parameters:
    - df: DataFrame with 'plateau_risk' and 'churned' columns
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Calculate churn rates
    plateau_summary = df.groupby("plateau_risk")["churned"].agg(["mean", "count"]).reset_index()
    plateau_summary["churn_rate"] = plateau_summary["mean"]
    plateau_summary["label"] = plateau_summary["plateau_risk"].map({0: "No Risk", 1: "Plateau Risk"})

    # Plot
    plt.figure(figsize=(7, 5))
    palette = ["lightgray", "#F8766D"]
    ax = sns.barplot(
        x="label", y="churn_rate", data=plateau_summary, palette=palette
    )

    for i, bar in enumerate(ax.patches):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.01,
            f"{height:.1%}",
            ha="center", va="bottom", fontsize=11, fontweight="bold"
        )

    # Draw average churn line
    avg_churn = df["churned"].mean()
    plt.axhline(avg_churn, color="black", linestyle="--", linewidth=1)
    plt.text(
        1.03, avg_churn, f"Avg Churn: {avg_churn:.0%}",
        ha="left", va="center", fontsize=10, color="black"
    )

    # Uplift annotation
    plt.annotate(
        "+8 pts / 1.4× Churn",
        xy=(1, plateau_summary.loc[1, "churn_rate"]),
        xytext=(0.45, 0.36),
        textcoords="data",
        arrowprops=dict(arrowstyle="->", color="crimson", linestyle="--"),
        fontsize=11,
        color="crimson",
        fontweight="bold"
    )

    plt.title("📉 Churn Rate by Plateau Risk", fontsize=14)
    plt.ylabel("Churn Rate")
    plt.xlabel("")
    plt.ylim(0, 1)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()

# ---------------------------
# Engagement feature engineering and churn plotting utilities
# ---------------------------

import pandas as pd

def engineer_engagement_features(df):
    """
    Create engagement metrics and classification bins based on normalized workload.

    - projects_per_year: normalized workload metric
    - monthly_project_load: derived from avg hours / projects
    - engagement_level: binned churn modeling tier

    Returns:
    - df with new columns added
    """
    import numpy as np
    df["projects_per_year"] = df["number_project"] / np.where(df["time_spend_company"] == 0, np.nan, df["time_spend_company"])
    df["monthly_project_load"] = df["average_monthly_hours"] / np.where(df["number_project"] == 0, np.nan, df["number_project"])

    df["engagement_level"] = pd.cut(
        df["projects_per_year"],
        bins=[0, 0.5, 1.5, 2.5, 10],
        labels=["very low", "low", "average", "high"]
    )

    return df

def churn_by_engagement(df, churn_col="churned"):
    """
    Plot churn rate by binned engagement level (projects per year) with annotations.

    Parameters:
    - df: DataFrame with `engagement_level` column and churn flag
    - churn_col: column to aggregate churn behavior on
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    eng_summary = df.groupby("engagement_level")[churn_col].agg(["mean", "count"]).reset_index()
    eng_summary["churn_rate"] = eng_summary["mean"].round(2)
    eng_summary["ci"] = 1.96 * np.sqrt((eng_summary["mean"] * (1 - eng_summary["mean"])) / eng_summary["count"])

    # Plot
    plt.figure(figsize=(8, 5))
    palette = sns.color_palette("Reds", n_colors=4)
    ax = sns.barplot(x="engagement_level", y="churn_rate", data=eng_summary, palette=palette)

    for i, bar in enumerate(ax.patches):
        height = bar.get_height()
        ci = eng_summary.loc[i, "ci"]
        label = f"Churn Rate: {int(height * 100)}%"
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.01, label,
                ha='center', va='bottom', fontsize=10, weight='bold')
        ax.vlines(bar.get_x() + bar.get_width()/2, height - ci, height + ci, color='black', linewidth=1)

    avg_churn = df[churn_col].mean()
    plt.axhline(avg_churn, color="gray", linestyle="--", linewidth=1)
    plt.text(3.05, avg_churn + 0.01, f"↓ Avg Churn: {int(avg_churn*100)}%", color="gray")

    # Annotate low engagement spike
    plt.annotate(
        "📌 29% churn in low-engagement group",
        xy=(1, eng_summary.loc[1, "churn_rate"]),
        xytext=(1, 0.33),
        arrowprops=dict(arrowstyle="->", color="firebrick", linestyle="--"),
        fontsize=10, color="firebrick", weight="bold"
    )

    plt.ylim(0, 0.35)
    plt.title("📉 Churn Rate by Engagement Level", weight="bold")
    plt.xlabel("Engagement Level (Projects per Year)")
    plt.ylabel("Churn Rate")
    plt.tight_layout()
    plt.show()

import pandas as pd

def engineer_interaction_features(df):
    """
    Adds engineered interaction features and tenure bands to the dataset.

    Features:
    - salary_encoded: ordinal encoding of salary
    - salary_x_hours: compensation load
    - tenure_x_salary: low-paid loyalty
    - satisfaction_x_hours: burnout indicator
    - tenure_band: binned tenure group

    Returns:
    - Modified DataFrame
    """
    # Ordinal salary encoding
    salary_map = {"low": 1, "medium": 2, "high": 3}
    df["salary_encoded"] = df["salary"].map(salary_map)

    # Interaction terms
    df["salary_x_hours"] = df["salary_encoded"] * df["average_monthly_hours"]
    df["tenure_x_salary"] = df["time_spend_company"] * df["salary_encoded"]
    df["satisfaction_x_hours"] = df["satisfaction_level"] * df["average_monthly_hours"]

    # Tenure bands
    df["tenure_band"] = pd.cut(
        df["time_spend_company"],
        bins=[0, 3, 5, 10],
        labels=["Short (≤3 yrs)", "Mid (4–5 yrs)", "Long (6–10 yrs)"]
    )

    return df

def plot_churn_by_salary_and_tenure(df, churn_col="churned"):
    """
    Plot churn rate by salary band and tenure band.

    Parameters:
    - df: DataFrame with churn, salary, and tenure_band columns
    - churn_col: column name representing churn status
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    # 📊 Grouped Churn Stats
    churn_group = df.groupby(["tenure_band", "salary"])[churn_col].agg(["mean", "count"]).reset_index()
    churn_group["churn_rate"] = churn_group["mean"].round(2)
    avg_churn = df[churn_col].mean()

    # 📈 Plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=churn_group,
        x="tenure_band",
        y="churn_rate",
        hue="salary",
        palette={"low": "#D3D3D3", "medium": "crimson", "high": "royalblue"}
    )

    # 🔢 Bar Labels
    for bars in ax.containers:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f"{int(round(height * 100))}%",
                        (bar.get_x() + bar.get_width() / 2, height + 0.015),
                        ha='center', va='bottom', fontsize=10, weight='bold')

    # 📌 Spike Highlight
    highlight = churn_group[(churn_group["tenure_band"] == "Mid (4–5 yrs)") & (churn_group["salary"] == "low")]
    if not highlight.empty:
        churn_pct = highlight["churn_rate"].values[0]
        ax.axhline(churn_pct, ls='--', color='red', alpha=0.5)
        ax.annotate(
            "📌 Spike: 49% churn in mid-tenure + low salary group",
            xy=(1, churn_pct), xytext=(1.1, churn_pct + 0.04),
            textcoords="data", color="red", fontsize=10,
            arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
            ha='left'
        )

    # ↕ Average Churn
    ax.axhline(avg_churn, ls='--', color='gray', lw=1)
    ax.annotate(
        f"↕ Avg Churn: {int(round(avg_churn * 100))}%",
        xy=(2.2, avg_churn), xytext=(2.3, avg_churn + 0.035),
        textcoords="data", color="gray", fontsize=10,
        ha='left'
    )

# ================================
# Distribution Plots
# ================================

    # 🎨 Style
    plt.title("📊 Churn Rate by Salary Band and Tenure", fontsize=14)
    plt.xlabel("Tenure Group")
    plt.ylabel("Churn Rate")
    plt.ylim(0, 0.7)
    plt.legend(title="Salary Band", loc='upper right')
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
    
def plot_numeric_distributions(df, numeric_cols, hue_col="churn_status", figsize=(14, 10), title="📈 Numeric Feature Behavior by Churn Status"):
    """
    Plots KDE-overlaid histograms for numeric columns, grouped by a churn label column.

    Parameters:
    - df: DataFrame containing the numeric columns and churn label column
    - numeric_cols: list of numeric column names to visualize
    - hue_col: str, the column to use for hue separation (default: 'churn_status')
    - figsize: tuple, figure size
    - title: str, plot title
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    fig, axes = plt.subplots(3, 2, figsize=figsize)
    axes = axes.flatten()

    for i, col in enumerate(numeric_cols):
        sns.histplot(
            data=df,
            x=col,
            hue=hue_col,
            kde=True,
            element="step",
            stat="density",
            common_norm=False,
            ax=axes[i],
            palette={"Retained": "#5DA5DA", "Churned": "#FAA43A"}
        )
        axes[i].set_title(f"{col.replace('_', ' ').title()} by {hue_col.replace('_', ' ').title()}")
        axes[i].grid(True, linestyle='--', alpha=0.5)

    axes[-1].axis("off")  # hide last subplot
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles=handles,
        labels=labels,
        title="Churn Status",
        loc="lower right",
        frameon=True
    )

    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

def plot_categorical_distributions(df, categorical_features_dict, figsize=(13, 8), title="📊 Baseline Categorical Distributions"):
    """
    Generates a 2x2 grid of count plots for categorical features.

    Parameters:
    - df: DataFrame (not directly used but consistent with interface)
    - categorical_features_dict: dict of {label: pd.Series} where each series is a mapped categorical feature
    - figsize: tuple, figure size for the grid
    - title: str, overall title for the figure
    """
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    axes = axes.flatten()

    for i, (label, series) in enumerate(categorical_features_dict.items()):
        sns.countplot(x=series, ax=axes[i], order=sorted(series.unique()))
        axes[i].set_title(f"{label.replace('_', ' ').title()} Distribution")
        axes[i].set_xlabel("")
        axes[i].set_ylabel("Count")
        axes[i].grid(axis='y', linestyle='--', alpha=0.5)

        if label == "department":
            axes[i].tick_params(axis='x', rotation=45)

    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()



# ================================
# Engagement Burnout Composite & Plots
# ================================

def add_burnout_risk_flag(df):
    """
    Create burnout risk flag based on defined thresholds for high effort and low satisfaction.
    """
    df["engagement_burn"] = df["projects_per_year"] * df["average_monthly_hours"]
    
    if "burnout_risk" not in df.columns:
        df["burnout_risk"] = (
            (df["average_monthly_hours"] > 250) &
            (df["satisfaction_level"] < 0.4)
        ).astype(int)
    
    return df


def plot_engagement_burn_kde(df):
    """
    KDE of engagement burn score by churn status.
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.kdeplot(
        data=df,
        x="engagement_burn",
        hue="churn_status",
        fill=True,
        common_norm=False,
        palette="coolwarm"
    )
    plt.title("📊 Engagement Burn Distribution by Churn Status")
    plt.xlabel("Engagement Burn (Projects × Monthly Hours)")
    plt.ylabel("Density")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_burnout_flag_churn(df):
    """
    Plot churn rate by burnout risk flag.
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    burnout_summary = df.groupby("burnout_risk")["churned"].agg(["count", "mean"]).reset_index()
    burnout_summary["churned_label"] = burnout_summary["mean"].apply(lambda x: f"{x:.2%}")
    burnout_summary["burnout_risk"] = burnout_summary["burnout_risk"].map({0: "No Risk", 1: "Burnout Risk"})

    plt.figure(figsize=(7, 7))  # slightly taller for visual balance
    ax = sns.barplot(x="burnout_risk", y="mean", data=burnout_summary, palette=["lightgray", "orangered"])
    plt.axhline(df["churned"].mean(), linestyle="--", color="black", alpha=0.7, label="Avg Churn")
    plt.title("🔥 Churn Rate by Burnout Risk", fontsize=14)
    plt.ylabel("Churn Rate")
    plt.xlabel("")
    plt.ylim(0, 1)
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    for i, bar in enumerate(ax.patches):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.01, f"{height:.1%}",
                ha='center', va='bottom', fontsize=10, weight='bold')

    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()


# ================================
# Plateau, Lowpaid Loyal, and Flag Churn Summary Utilities
# ================================

def add_plateau_risk_flag(df, tenure_threshold=3, satisfaction_threshold=0.5):
    """
    Flags employees who have been at the company longer than `tenure_threshold`
    and show low satisfaction. Intended to capture stagnation or plateau behavior.
    """
    df["plateau_risk"] = (
        (df["time_spend_company"] > tenure_threshold) &
        (df["satisfaction_level"] < satisfaction_threshold)
    ).astype(int)
    return df


def add_lowpaid_loyal_flag(df, tenure_threshold=3, salary_level="low"):
    """
    Flags employees who have long tenure but are still classified as low salary.
    Suggests under-recognized, possibly disengaged loyal employees.
    """
    df["lowpaid_loyal"] = (
        (df["time_spend_company"] > tenure_threshold) &
        (df["salary"] == salary_level)
    ).astype(int)
    return df


def summarize_flag_churn(df, flag_cols, target_col="churned"):
    """
    Creates a summary table showing churn rates for each flag variable provided.

    Parameters:
    - df: DataFrame containing churn label and flag columns
    - flag_cols: list of binary flag column names
    - target_col: churn indicator column (default: 'churned')

    Returns:
    - DataFrame with churn summary for each flag
    """
    summary = {}

    for col in flag_cols:
        grouped = df.groupby(col)[target_col].mean().round(2)
        summary[col] = grouped.to_dict()

    return pd.DataFrame(summary).T.round(2)
def combine_flag_churn_summary(df, flag_cols, target_col="churned"):
    """
    Combines both churn-facing and flag-facing summaries into a single DataFrame.

    Output includes:
    - % of retained and churned users who had each flag
    - Churn rates for flagged vs. non-flagged users

    Parameters:
    - df: DataFrame with churn column and binary flag columns
    - flag_cols: list of binary flag column names
    - target_col: name of the churn column (default: 'churned')

    Returns:
    - Merged DataFrame suitable for export or dashboarding
    """
    results = []

    for flag in flag_cols:
        # % of users with flag in each churn group
        flag_by_churn = df.groupby(target_col)[flag].mean().round(2)
        percent_retained = flag_by_churn.get(0, 0.0)
        percent_churned = flag_by_churn.get(1, 0.0)

        # Churn rates for those with and without the flag
        churn_rate_by_flag = df.groupby(flag)[target_col].mean().round(2)
        churn_rate_no_flag = churn_rate_by_flag.get(0, 0.0)
        churn_rate_flagged = churn_rate_by_flag.get(1, 0.0)

        results.append({
            "Flag": flag,
            "% Retained w/ Flag": percent_retained,
            "% Churned w/ Flag": percent_churned,
            "Churn Rate (No Flag)": churn_rate_no_flag,
            "Churn Rate (Flagged)": churn_rate_flagged
        })

    return pd.DataFrame(results)


# ================================
# Cumulative Flag Risk Plot
# ================================

def plot_cumulative_flag_risk(df, flag_cols, churn_col="churned"):
    """
    Plots churn rate by the number of active risk flags (accumulated risk level).
    
    Parameters:
    - df: DataFrame with churn and flag columns
    - flag_cols: list of binary flag column names
    - churn_col: name of the churn indicator column
    
    Output:
    - Bar plot showing churn rate by cumulative number of flags
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Count number of flags triggered per employee
    df["flag_total"] = df[flag_cols].sum(axis=1)

    # Aggregate churn stats
    summary = df.groupby("flag_total")[churn_col].agg(["count", "mean"]).reset_index()
    summary["churn_rate"] = summary["mean"].round(2)

    # Plot
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x="flag_total", y="churn_rate", data=summary, palette="OrRd")

    # Annotate churn rates and sample sizes
    for i, bar in enumerate(ax.patches):
        height = bar.get_height()
        n = summary.loc[i, "count"]
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.01,
                f"{height:.0%}\nN={n}",
                ha='center', va='bottom', fontsize=10, weight='bold')

    plt.axhline(df[churn_col].mean(), linestyle="--", color="gray", alpha=0.6, label="Avg Churn")
    plt.title("📊 Churn Rate by Number of Risk Flags", fontsize=14)
    plt.xlabel("Number of Active Risk Flags")
    plt.ylabel("Churn Rate")
    plt.ylim(0, 1)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()
# ================================
# Stacked Bar Plot: Churn vs. Retention by Number of Flags
# ================================

def plot_stacked_flag_outcomes(df, flag_cols, churn_col="churned"):
    """
    Plots stacked bar chart of churn vs. retention by number of active risk flags.

    Parameters:
    - df: DataFrame with churn and flag columns
    - flag_cols: list of binary flag column names
    - churn_col: churn outcome column
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Count number of flags per user
    df["flag_total"] = df[flag_cols].sum(axis=1)

    # Aggregate churn counts
    summary = df.groupby("flag_total")[churn_col].value_counts(normalize=True).unstack().fillna(0)
    # Ensure columns are labeled as Retained (0) and Churned (1)
    col_names = []
    for col in summary.columns:
        if col == 0:
            col_names.append("Retained")
        elif col == 1:
            col_names.append("Churned")
        else:
            col_names.append(str(col))
    summary.columns = col_names
    summary = summary.reset_index()

    # Plot as side-by-side bars with explicit control of x-tick positions
    plt.figure(figsize=(9, 5))
    bar_width = 0.4
    x_pos = list(range(len(summary)))
    x_labels = summary["flag_total"]
    plt.bar([p - bar_width/2 for p in x_pos], summary["Retained"], width=bar_width, label="Retained", color="lightgray")
    plt.bar([p + bar_width/2 for p in x_pos], summary["Churned"], width=bar_width, label="Churned", color="firebrick")
    plt.xticks(ticks=x_pos, labels=x_labels)

    # Annotate each bar individually above its own height
    for i, xpos in enumerate(x_pos):
        total_n = df[df["flag_total"] == summary.loc[i, "flag_total"]].shape[0]
        churn_count = int(round(summary.loc[i, "Churned"] * total_n))
        retained_count = int(round(summary.loc[i, "Retained"] * total_n))
        
        # Annotate each bar individually above its own height
        plt.text(xpos - bar_width/2, summary.loc[i, "Retained"] + 0.01,
                 f"{retained_count} Retained\nN={total_n}",
                 ha='center', fontsize=9, weight='bold')

        plt.text(xpos + bar_width/2, summary.loc[i, "Churned"] + 0.01,
                 f"{churn_count} Churned\nN={total_n}",
                 ha='center', fontsize=9, weight='bold')

    plt.title("📊 Churn vs. Retention by Number of Risk Flags", fontsize=14)
    plt.xlabel("Number of Active Risk Flags")
    plt.ylabel("Percentage of Employees")
    plt.ylim(0, 1.1)
    plt.legend(loc="upper right", bbox_to_anchor=(1.0, 1.02), ncol=2, frameon=True)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()


# ================================
# Lowpaid Loyal Churn Plot Utility
# ================================

def plot_lowpaid_loyal_churn(df):
    """
    Plots churn rate for employees flagged as lowpaid_loyal vs. others.

    Parameters:
    - df: DataFrame with 'lowpaid_loyal' and 'churned' columns
    """
    import matplotlib.pyplot as plt

    # Calculate churn metrics
    group_labels = ['Underpaid with Tenure', 'All Other Employees']
    churn_rates = [
        df[df["lowpaid_loyal"] == 1]["churned"].mean(),
        df[df["lowpaid_loyal"] == 0]["churned"].mean()
    ]
    confidence_intervals = [
        1.96 * (churn_rates[0] * (1 - churn_rates[0]) / len(df[df["lowpaid_loyal"] == 1])) ** 0.5,
        1.96 * (churn_rates[1] * (1 - churn_rates[1]) / len(df[df["lowpaid_loyal"] == 0])) ** 0.5
    ]
    global_churn_rate = df["churned"].mean()

    fig, ax = plt.subplots(figsize=(6, 5))

    bars = ax.bar(
        group_labels,
        churn_rates,
        yerr=confidence_intervals,
        capsize=5,
        color=["#c0392b", "#f39c12"],
        edgecolor="black"
    )

    # Annotate churn percentages
    for bar, rate in zip(bars, churn_rates):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.015,
            f"{int(rate * 100)}%",
            ha="center",
            va="bottom",
            fontsize=11,
            weight="bold"
        )

    # Highlight uplift
    uplift_pts = round((churn_rates[0] - churn_rates[1]) * 100)
    uplift_ratio = round(churn_rates[0] / churn_rates[1], 1)
    ax.text(
        0.5, max(churn_rates) + 0.05,
        f"⬆️ +{uplift_pts} pts / {uplift_ratio}× Churn",
        ha="center",
        fontsize=12,
        weight="bold",
        color="crimson"
    )

    # Reference line
    ax.axhline(global_churn_rate, color='gray', linestyle='--', alpha=0.6)
    ax.text(1.05, global_churn_rate + 0.01, f"↕ Avg Churn: {int(global_churn_rate * 100)}%", color='gray')

    ax.set_title("📉 Churn Rate: Underpaid with Tenure vs. Others", fontsize=14, weight="bold")
    ax.set_ylabel("Churn Rate")
    ax.set_ylim(0, 0.55)
    ax.set_xlabel("")
    plt.tight_layout()
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()
def plot_churn_line_by_flag_score(df, flag_cols, churn_col="churned"):
    """
    Plots a line chart showing churn rate vs. total number of active risk flags.

    Parameters:
    - df: DataFrame with churn and flag columns
    - flag_cols: list of binary flag column names
    - churn_col: name of the churn indicator column
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    df["flag_total"] = df[flag_cols].sum(axis=1)
    summary = df.groupby("flag_total")[churn_col].mean().reset_index()

    plt.figure(figsize=(8, 5))
    sns.lineplot(data=summary, x="flag_total", y=churn_col, marker="o", linewidth=2.5, color="firebrick")
    plt.axhline(df[churn_col].mean(), linestyle="--", color="gray", alpha=0.7, label="Avg Churn")

    for i, row in summary.iterrows():
        plt.text(row["flag_total"], row[churn_col] + 0.015, f"{row[churn_col]:.0%}", 
                 ha='center', va='bottom', fontsize=10, weight='bold')

    plt.title("📈 Churn Rate by Number of Risk Flags", fontsize=14)
    plt.xlabel("Number of Active Risk Flags")
    plt.ylabel("Churn Rate")
    plt.ylim(0, 1)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_flag_total_distribution_by_churn(df, flag_cols, churn_col="churned"):
    """
    KDE plot showing the distribution of cumulative flag totals by churn status.

    Parameters:
    - df: DataFrame with binary flag columns and churn column
    - flag_cols: list of binary flag column names
    - churn_col: churn indicator column
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    df["flag_total"] = df[flag_cols].sum(axis=1)
    df["churn_status"] = df[churn_col].map({0: "Retained", 1: "Churned"})

    plt.figure(figsize=(8, 5))
    sns.kdeplot(data=df, x="flag_total", hue="churn_status", fill=True, common_norm=False, palette="Set2")
    plt.title("📊 Flag Total Distribution by Churn Status")
    plt.xlabel("Number of Active Risk Flags")
    plt.ylabel("Density")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()