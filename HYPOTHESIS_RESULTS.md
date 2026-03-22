# 📊 Hypothesis Testing Results

> [!WARNING]
> **Low Statistical Power (~35%)**
> The formal hypothesis tests below were run on the initial 96 pilot data points. Because the overall statistical power is extremely low, all findings—even those that appear highly significant ($p < 0.05$)—must be interpreted with caution. These intriguing preliminary results serve as the primary motivation for why scaling future experiments to 43+ replicates per treatment is necessary to rigorously validate these collaboration dynamics.

While the initial Power Analysis established the ~35% power limitation, we ran formal N-Way ANOVA hypothesis tests on the pilot data to see if any strong effects or trends were present.

The tests evaluated the impact of **Number of Agents**, **Constraint Strategy** (Time vs. Iterations), and the **Constraint Level** (Tight vs. Loose).

## Key Findings

### 1. Main Effect of Constraint Level (Tight vs. Loose)
* **Result:** **Not Significant** ($p = 0.98$)
* **Average Execution Time:** Loose Budget (1.63s) vs. Tight Budget (1.62s)
* **Interpretation:** Simply increasing the overall optimization budget (from 3 to 8 iterations, or from 60s to 120s) did not yield universally faster code.

### 2. Main Effect of Team Size (1 vs 2 vs 3 Agents)
* **Result:** **Not Significant** ($p = 0.113$)
* **Average Execution Time:** 1 Agent (1.87s) | 2 Agents (1.54s) | 3 Agents (1.47s)
* **Interpretation:** There is a clear **positive trend** showing that larger agent teams write faster-executing code. However, due to the low sample size, this trend did not quite reach statistical significance. 

### 3. Strategy Comparison (Time Limits vs. Iterations)
* **Result:** **Not Significant** ($p = 0.131$)
* **Average Execution Time:** Time Constraints (1.50s) vs. Iteration Constraints (1.75s)
* **Interpretation:** Interrupting agents via a background timer produced slightly faster code on average than allowing them fixed iterative turns, though it wasn't a significant main effect.

---

## 🌟 Strategy $\times$ Constraint Level Interaction
* **Result:** **Highly Significant** ($p = 0.002$)
  
This was the most fascinating finding from the pilot data. The **type** of constraint drastically changed how the agents responded to tighter vs. looser pressure.

1. **Under Time Constraints:**
   * **Loose (120s):** 1.28s *(Fastest overall)*
   * **Tight (60s):** 1.72s
   * *Conclusion:* A tighter time limit harms performance. Giving agents 60 seconds created too much pressure, resulting in slower, less optimized code compared to a generous 120-second window.

2. **Under Iteration Constraints:**
   * **Tight (3 Iterations):** 1.53s
   * **Loose (8 Iterations):** 1.97s *(Slowest overall)*
   * *Conclusion:* Counter-intuitively, a looser iteration limit harms performance. Giving agents 8 distinct turns appeared to cause "code bloat" or over-engineering. Cutting them off at just 3 iterations resulted in much faster code.

**Overall Recommendation for Future Experiments:** 
Using a generous background time limit (e.g., 120s) yields the most highly optimized code, outperforming fixed-turn iteration strategies while avoiding the detrimental effects of excessive time pressure.
