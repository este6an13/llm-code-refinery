# 🤖 LLM Code Refinery: How it Works

At a high level, this project is like a **coding competition for AI bots**. It explores how well AI agents (using GPT-4o) can iteratively write and optimize Python code, either working alone or collaborating as a team, under different constraints (like strict time limits or maximum rounds of revision).

Here’s a step-by-step breakdown of how the system works and the role of each main file:

---

## 🏗️ The Core Pipeline

### 1. The Code Generators (`main.py`)
This is where the actual code generation happens. You can think of it as the "writer's room."
* **The Task:** The script tells the AI agents to write a specific Python function: *find the difference between the smallest and largest numbers in a list of 1 million integers, but only looking at numbers whose digits add up to exactly 30.*
* **The Teams:** It tests different configurations—sometimes 1 agent works alone, sometimes 2 or 3 agents take turns refining each other's work in a round-robin style.
* **The Constraints:** Some teams are given a specific number of tries (iterations), while others race against the clock (e.g., a 60-second time limit enforced by a background timer).
* **The Output:** Every time a team finishes, their final Python code is saved into the `programs/` folder. The filename acts as a label to track how it was generated (e.g., `2_8_inf_1.py` means "2 agents, 8 iterations, no time limit, replicate #1").

### 2. The Examiners (`measure.py`)
Once the bots have written their solutions, this script puts them to the test. It acts as the "referee" checking both accuracy and speed.
* It generates two fresh lists of 1 million random numbers to use as test data.
* It dynamically imports every generated Python file inside the `programs/` folder, loads the function out of it, and runs it against the random numbers.
* It tests each program **twice per list** (4 runs total per script) to ensure a fair speed measurement.
* **The Grading:** It records two things: Did the program get the right answer (compared to a reference solution), and exactly how many seconds did it take to execute?
* **The Output:** All these individual test results get logged into a raw data spreadsheet named `timing_results.csv`.

### 3. The Data Cruncher (`summarize.py`)
Because `timing_results.csv` contains lots of raw data (4 test runs for every single script), this file cleans things up.
* It converts raw filename markers into human-readable labels (a "Treatment" like "2 AGENTS, 3 ITERATIONS").
* It averages out the execution times for each unique setup across all its test runs.
* **The Output:** It squashes all the individual measurements into a neat, high-level summary saved as `experiment_data.csv`.

### 4. The Statistician (`power-analysis.ipynb`)
Finally, we have the Jupyter notebook that answers the big question: *“Were our results actually meaningful?”*
* Because AI outputs can be non-deterministic, and computers sometimes run slightly faster or slower on different runs, we need statistics to know if one teamwork strategy is *truly* better than another. 
* This notebook runs a **Power Analysis**. In this pilot run, it found that the experiment's "statistical power" was only ~35%. That means the sample size is currently too small to be completely confident in the observed results.
* It calculates that you’d need about **43 runs (replicates)** per setup to confidently prove that one AI strategy is 0.5 seconds faster than another.

---

## 📝 Summary

1. `main.py` asks the AI to write and refine code under different teamwork setups.
2. `measure.py` runs that code to check if it works and exactly how fast it is.
3. `summarize.py` averages out the speed scores for easier reading.
4. `power-analysis.ipynb` crunches the stats to tell us if the results are scientifically reliable based on our sample size.
