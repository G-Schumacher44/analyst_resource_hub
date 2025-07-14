import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import operator as op  # Moved here from within function

# --------------------------
# Risk Flag Generators
# --------------------------

def flag_multi_condition_risk(df, conditions, flag_col="multi_condition_flag"):
    """
    Flags rows where multiple column conditions are simultaneously met.

    Parameters:
    - df (DataFrame): Input dataset
    - conditions (list of dict): Each condition is a dictionary with:
        - 'col': column name (str)
        - 'op': comparison operator as string ('>', '>=', '<', '<=', '==', '!=')
        - 'val': value to compare against
    - flag_col (str): Name of the output binary flag column

    Returns:
    - DataFrame with a new column flagging rows where all conditions are met
    """
    op_map = {
        ">": op.gt, ">=": op.ge,
        "<": op.lt, "<=": op.le,
        "==": op.eq, "!=": op.ne
    }

    # Evaluate each condition and combine with logical AND
    cond_expr = op_map[conditions[0]["op"]](df[conditions[0]["col"]], conditions[0]["val"])
    for cond in conditions[1:]:
        cond_expr &= op_map[cond["op"]](df[cond["col"]], cond["val"])

    df[flag_col] = cond_expr.astype(int)
    return df

def flag_burnout_risk(df, workload_col="average_monthly_hours", satisfaction_col="satisfaction_level",
                      workload_thresh=250, satisfaction_thresh=0.4, flag_col="burnout_risk"):
    """
    Flags employees at burnout risk based on high workload and low satisfaction.

    Parameters:
    - df (DataFrame): The input dataset.
    - workload_col (str): Column name representing workload (e.g., hours).
    - satisfaction_col (str): Column name for satisfaction or engagement.
    - workload_thresh (float): Threshold above which workload is considered high.
    - satisfaction_thresh (float): Threshold below which satisfaction is considered low.
    - flag_col (str): Name for the resulting binary flag column.

    Returns:
    - DataFrame with a new column flagging burnout risk.
    """
    df[flag_col] = (
        (df[workload_col] > workload_thresh) &
        (df[satisfaction_col] < satisfaction_thresh)
    ).astype(int)
    return df


def flag_stagnation_risk(
    df,
    tenure_col,
    engagement_col,
    tenure_thresh=3,
    engagement_thresh=0.5,
    flag_col="stagnation_risk"
):
    """
    Flags individuals with extended tenure and low engagement, suggesting stagnation.

    Parameters:
    - df (DataFrame): Input dataset
    - tenure_col (str): Column representing duration (e.g., years with company)
    - engagement_col (str): Column for satisfaction or involvement metric
    - tenure_thresh (int): Minimum threshold for tenure
    - engagement_thresh (float): Maximum threshold for engagement
    - flag_col (str): Name of the output flag column

    Returns:
    - DataFrame with a new flag column indicating stagnation risk
    """
    df[flag_col] = (
        (df[tenure_col] > tenure_thresh) &
        (df[engagement_col] < engagement_thresh)
    ).astype(int)
    return df

# For backward compatibility
def flag_plateau_risk(df, tenure_col="time_spend_company", satisfaction_col="satisfaction_level",
                      tenure_thresh=3, satisfaction_thresh=0.5, flag_col="plateau_risk"):
    """
    Flags employees potentially plateaued due to long tenure and low satisfaction.
    (Deprecated, use flag_stagnation_risk instead.)
    """
    return flag_stagnation_risk(
        df,
        tenure_col=tenure_col,
        engagement_col=satisfaction_col,
        tenure_thresh=tenure_thresh,
        engagement_thresh=satisfaction_thresh,
        flag_col=flag_col
    )

def flag_lowpaid_loyal(df, tenure_col="time_spend_company", salary_col="salary",
                       tenure_thresh=3, low_salary_value="low", flag_col="lowpaid_loyal"):
    """
    Flags employees considered loyal but underpaid (long tenure + low salary).

    Parameters:
    - df (DataFrame): The input dataset.
    - tenure_col (str): Column name representing tenure.
    - salary_col (str): Column name indicating salary level or band.
    - tenure_thresh (int): Minimum tenure threshold.
    - low_salary_value (str): Value in salary_col indicating low pay.
    - flag_col (str): Name for the resulting binary flag column.

    Returns:
    - DataFrame with a new column flagging low-paid loyal employees.
    """
    df[flag_col] = (
        (df[tenure_col] > tenure_thresh) &
        (df[salary_col] == low_salary_value)
    ).astype(int)
    return df

# --------------------------
# Generalized Value Stagnation Flag
# --------------------------

def flag_value_stagnation(df, tenure_col, category_col, 
                          tenure_thresh=3, low_value="low", flag_col="value_stagnation_flag"):
    """
    Flags individuals with long tenure who remain at a specified low-value category.

    This can be used to detect under-recognized loyalty or performance stagnation in HR, operations, or customer domains.

    Parameters:
    - df (DataFrame): Input dataset
    - tenure_col (str): Column name representing length of service or time
    - category_col (str): Categorical value column (e.g. salary tier, loyalty level)
    - tenure_thresh (int): Threshold above which tenure is considered long
    - low_value (str): Value in category_col representing the "low" tier
    - flag_col (str): Name of the output binary flag column

    Returns:
    - DataFrame with a new flag column
    """
    df[flag_col] = (
        (df[tenure_col] > tenure_thresh) &
        (df[category_col] == low_value)
    ).astype(int)
    return df

# --------------------------
# Risk Flag Visuals
# --------------------------

def plot_churn_by_flag_score(
    df,
    flag_cols,
    churn_col="churned",
    score_col="flag_total",
    title="🧮 Churn Rate by Accumulated Risk Flags",
    label_map=None,
    show_avg_line=True,
    annotate_bars=True
):
    """
    Plot churn rate by the sum of specified risk flags.

    Parameters:
    - df (DataFrame): Input dataset
    - flag_cols (list): List of flag columns to sum for score
    - churn_col (str): Column indicating churn (default: 'churned')
    - score_col (str): Name for the score column (default: 'flag_total')
    - title (str): Chart title
    - label_map (dict): Mapping of score to string label (optional)
    - show_avg_line (bool): Whether to display average churn line
    - annotate_bars (bool): Whether to annotate bars with churn rate values
    """
    df[score_col] = df[flag_cols].sum(axis=1)
    summary = df.groupby(score_col)[churn_col].agg(["mean", "count"]).reset_index()
    summary.columns = ["risk_score", "churn_rate", "count"]
    if label_map:
        summary["label"] = summary["risk_score"].map(label_map)
    else:
        summary["label"] = summary["risk_score"].apply(lambda x: f"{int(x)} Flag{'s' if x != 1 else ''}")

    plt.figure(figsize=(9, 5))
    palette = sns.color_palette("Reds", n_colors=len(summary))
    ax = sns.barplot(data=summary, x="label", y="churn_rate", palette=palette)

    if annotate_bars:
        for i, bar in enumerate(ax.patches):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + 0.02, f"{height:.0%}", ha="center", va="bottom", fontsize=11, weight="bold")

    if show_avg_line:
        avg = df[churn_col].mean()
        ax.axhline(avg, ls="--", color="gray")
        ax.text(len(summary) - 0.5, avg + 0.01, f"↕ Avg Churn: {avg:.0%}", ha="right", color="gray", fontsize=10)

    ax.set_title(title, fontsize=14)
    ax.set_xlabel("Number of Active Risk Flags")
    ax.set_ylabel("Churn Rate")
    plt.ylim(0, 1)
    plt.tight_layout()
    counts = ", ".join(f"{row['label']}: {row['count']}" for _, row in summary.iterrows())
    plt.figtext(0.5, -0.05, f"📦 Employees per Group — {counts}", ha="center", fontsize=9, color="gray")
    plt.show()

def plot_cumulative_flag_risk(
    df,
    flag_cols,
    churn_col="churned",
    score_col="flag_total",
    title="📊 Churn Rate by Number of Risk Flags",
    show_avg_line=True,
    annotate_bars=True
):
    """
    Plot churn rate by cumulative number of risk flags.

    Parameters:
    - df (DataFrame): Input dataset
    - flag_cols (list): List of flag columns to sum for score
    - churn_col (str): Column indicating churn (default: 'churned')
    - score_col (str): Name for the score column (default: 'flag_total')
    - title (str): Chart title
    - show_avg_line (bool): Whether to display average churn line
    - annotate_bars (bool): Whether to annotate bars with churn rate and N
    """
    df[score_col] = df[flag_cols].sum(axis=1)
    summary = df.groupby(score_col)[churn_col].agg(["count", "mean"]).reset_index()
    summary["churn_rate"] = summary["mean"].round(2)

    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x=score_col, y="churn_rate", data=summary, palette="OrRd")

    if annotate_bars:
        for i, bar in enumerate(ax.patches):
            height = bar.get_height()
            n = summary.loc[i, "count"]
            ax.text(bar.get_x() + bar.get_width()/2, height + 0.01, f"{height:.0%}\nN={n}", ha='center', va='bottom', fontsize=10, weight='bold')

    if show_avg_line:
        avg = df[churn_col].mean()
        plt.axhline(avg, linestyle="--", color="gray", alpha=0.6, label="Avg Churn")
        plt.legend()

    plt.title(title, fontsize=14)
    plt.xlabel("Number of Active Risk Flags")
    plt.ylabel("Churn Rate")
    plt.ylim(0, 1)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()

def plot_stacked_flag_outcomes(
    df,
    flag_cols,
    churn_col="churned",
    score_col="flag_total",
    title="📊 Churn vs. Retention by Number of Risk Flags",
    label_map=None,
    annotate_bars=True
):
    """
    Plot stacked bar chart of churn vs retention by number of risk flags.

    Parameters:
    - df (DataFrame): Input dataset
    - flag_cols (list): List of flag columns to sum for score
    - churn_col (str): Column indicating churn (default: 'churned')
    - score_col (str): Name for the score column (default: 'flag_total')
    - title (str): Chart title
    - label_map (dict): Mapping of score to string label (optional)
    - annotate_bars (bool): Whether to annotate bars with counts
    """
    df[score_col] = df[flag_cols].sum(axis=1)
    summary = df.groupby(score_col)[churn_col].value_counts(normalize=True).unstack().fillna(0)
    summary.columns = ["Retained" if col == 0 else "Churned" for col in summary.columns]
    summary = summary.reset_index()
    # For x labels
    if label_map:
        x_labels = summary[score_col].map(label_map)
    else:
        x_labels = summary[score_col].apply(lambda x: f"{int(x)} Flag{'s' if x != 1 else ''}")

    plt.figure(figsize=(9, 5))
    bar_width = 0.4
    x_pos = list(range(len(summary)))
    plt.bar([p - bar_width/2 for p in x_pos], summary["Retained"], width=bar_width, label="Retained", color="lightgray")
    plt.bar([p + bar_width/2 for p in x_pos], summary["Churned"], width=bar_width, label="Churned", color="firebrick")
    plt.xticks(ticks=x_pos, labels=x_labels)

    if annotate_bars:
        for i, xpos in enumerate(x_pos):
            total_n = df[df[score_col] == summary.loc[i, score_col]].shape[0]
            churn_count = int(round(summary.loc[i, "Churned"] * total_n))
            retained_count = int(round(summary.loc[i, "Retained"] * total_n))
            plt.text(xpos - bar_width/2, summary.loc[i, "Retained"] + 0.01, f"{retained_count} Retained\nN={total_n}", ha='center', fontsize=9, weight='bold')
            plt.text(xpos + bar_width/2, summary.loc[i, "Churned"] + 0.01, f"{churn_count} Churned\nN={total_n}", ha='center', fontsize=9, weight='bold')

    plt.title(title, fontsize=14)
    plt.xlabel("Number of Active Risk Flags")
    plt.ylabel("Percentage of Employees")
    plt.ylim(0, 1.1)
    plt.legend(loc="upper right", bbox_to_anchor=(1.0, 1.02), ncol=2, frameon=True)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()

def plot_churn_line_by_flag_score(df, flag_cols, churn_col="churned"):
    """
    Line plot of churn rate by number of active risk flags.
    """
    # Calculate total active flags per employee
    df["flag_total"] = df[flag_cols].sum(axis=1)
    # Aggregate mean churn rate by flag total
    summary = df.groupby("flag_total")[churn_col].mean().reset_index()

    plt.figure(figsize=(8, 5))
    sns.lineplot(data=summary, x="flag_total", y=churn_col, marker="o", linewidth=2.5, color="firebrick")
    # Plot average churn rate line for reference
    plt.axhline(df[churn_col].mean(), linestyle="--", color="gray", alpha=0.7, label="Avg Churn")

    # Annotate each point with churn percentage
    for i, row in summary.iterrows():
        plt.text(row["flag_total"], row[churn_col] + 0.015, f"{row[churn_col]:.0%}", ha='center', va='bottom', fontsize=10, weight='bold')

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
    Plot KDE distribution of total active risk flags separated by churn status.

    Parameters:
    - df (DataFrame): Input dataset
    - flag_cols (list): List of flag columns to sum for score
    - churn_col (str): Column indicating churn (default: 'churned')
    """
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

# --------------------------
# Summary Tables
# --------------------------

def summarize_flag_churn(df, flag_cols, target_col="churned"):
    """
    Summarize mean churn rates grouped by each flag column.

    Parameters:
    - df (DataFrame): Input dataset
    - flag_cols (list): List of flag columns to summarize
    - target_col (str): Target column indicating churn (default: 'churned')

    Returns:
    - DataFrame with mean churn rates per flag value
    """
    summary = {}
    for col in flag_cols:
        grouped = df.groupby(col)[target_col].mean().round(2)
        summary[col] = grouped.to_dict()
    return pd.DataFrame(summary).T.round(2)

def combine_flag_churn_summary(df, flag_cols, target_col="churned"):
    """
    Combine flag and churn statistics into a summary table for analysis.

    Parameters:
    - df (DataFrame): Input dataset
    - flag_cols (list): List of flag columns to analyze
    - target_col (str): Target column indicating churn (default: 'churned')

    Returns:
    - DataFrame summarizing retention and churn rates by flag presence
    """
    results = []
    for flag in flag_cols:
        # Mean flag value by churn status (0 = retained, 1 = churned)
        flag_by_churn = df.groupby(target_col)[flag].mean().round(2)
        percent_retained = flag_by_churn.get(0, 0.0)
        percent_churned = flag_by_churn.get(1, 0.0)

        # Churn rate by flag presence (0 = no flag, 1 = flagged)
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