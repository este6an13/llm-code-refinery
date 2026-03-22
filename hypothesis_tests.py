import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load data
df = pd.read_csv("timing_results.csv")

def extract_features(row):
    # Constraint Type
    if str(row["Time Limit"]) == "inf":
        ctype = "Iteration"
        clevel = "Tight" if float(row["Iterations"]) == 3 else "Loose"
    else:
        ctype = "Time"
        # 60 seconds is technically "Tighter" than 120 seconds
        clevel = "Tight" if float(row["Time Limit"]) == 60 else "Loose"
    return pd.Series([row["Num Agents"], ctype, clevel], index=["Agents", "Type", "Level"])

df[["Agents", "Type", "Level"]] = df.apply(extract_features, axis=1)
df["Time"] = df["Execution Time (s)"]

print("--- Data Sample ---")
print(df[["Time", "Agents", "Type", "Level"]].head())

# Full 3-Way ANOVA including all factors (tighter time constraint effect)
print("\n--- Full 3-Way ANOVA (Agents x Type x Level) ---")
model_full = ols("Time ~ C(Agents) * C(Type) * C(Level)", data=df).fit()
print(sm.stats.anova_lm(model_full, typ=2))

print("\n--- Specific Hypothesis Testing ---")

# 1. Main Effect of Level (Tight vs Loose)
print("\n1. Main Effect of Constraint Level (Tight vs Loose budget)")
model1 = ols("Time ~ C(Level)", data=df).fit()
print(sm.stats.anova_lm(model1, typ=2))

# 2. Main Effect of Team Size (Agents: 1, 2, 3)
print("\n2. Main Effect of Team Size (Agents Count)")
model2 = ols("Time ~ C(Agents)", data=df).fit()
print(sm.stats.anova_lm(model2, typ=2))

# 3. Strategy Comparison (Type: Iterations vs Time limits)
print("\n3. Strategy Comparison (Iterations vs Time limits)")
model3 = ols("Time ~ C(Type)", data=df).fit()
print(sm.stats.anova_lm(model3, typ=2))

# Let's look at the estimated means for Type x Level
print("\n--- Average Execution Times by Group ---")
mean_summary = df.groupby(["Type", "Level"])["Time"].agg(["mean", "std", "count"])
print(mean_summary)

print("\n--- Average Execution Times by Strategy (Type) ---")
type_summary = df.groupby(["Type"])["Time"].agg(["mean", "std", "count"])
print(type_summary)

print("\n--- Average Execution Times by Level (Tight vs Loose) ---")
level_summary = df.groupby(["Level"])["Time"].agg(["mean", "std", "count"])
print(level_summary)

print("\n--- Average Execution Times by Team Size (Agents) ---")
agents_summary = df.groupby(["Agents"])["Time"].agg(["mean", "std", "count"])
print(agents_summary)
