import numpy as np
import pandas as pd

CSV_INPUT_FILE = "timing_results.csv"
CSV_OUTPUT_FILE = "experiment_data.csv"

df = pd.read_csv(CSV_INPUT_FILE)

# Replace string 'inf' with actual np.inf
df["Iterations"] = df["Iterations"].replace("inf", np.inf).astype(float)
df["Time Limit"] = df["Time Limit"].replace("inf", np.inf).astype(float)


# Create the Treatment column
def get_treatment(row):
    if np.isinf(row["Time Limit"]):
        return f"{int(row['Num Agents'])} AGENTS, {int(row['Iterations'])} ITERATIONS"
    elif np.isinf(row["Iterations"]):
        return (
            f"{int(row['Num Agents'])} AGENTS, {int(row['Time Limit'] // 60)} MINUTES"
        )
    else:
        return f"{int(row['Num Agents'])} AGENTS, {int(row['Iterations'])} ITERATIONS"  # fallback


df["Treatment"] = df.apply(get_treatment, axis=1)

# Group by Treatment and Replicate and calculate average execution time
summary_df = (
    df.groupby(["Treatment", "Replicate"])["Execution Time (s)"]
    .mean()
    .reset_index()
    .rename(columns={"Execution Time (s)": "Avg. Execution Time"})
)

summary_df.to_csv(CSV_OUTPUT_FILE, index=False)
print(f"Summary saved to {CSV_OUTPUT_FILE}")
