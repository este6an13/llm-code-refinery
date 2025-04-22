import math
import os
import re
import threading
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key")

# Ensure the programs directory exists
PROGRAMS_DIR = "programs"
os.makedirs(PROGRAMS_DIR, exist_ok=True)

# Define the problem statement
PROBLEM_STATEMENT = """
Write a function `get_difference` that takes a list of 1 million random integers (each between 1 and 100,000) as input and returns an integer: the difference between the smallest and largest numbers in the list whose digits sum up to 30.
"""


def create_clients(num_agents):
    """Create a list of OpenAI clients for each agent."""
    return [OpenAI(api_key=OPENAI_API_KEY) for _ in range(num_agents)]


def extract_python_code(text):
    """Extracts Python code from a markdown-style code block."""
    match = re.search(r"```python\n(.*?)\n```", text, re.DOTALL)
    return match.group(1) if match else text


def chat_with_llm(client, prompt, conversation):
    """Send a message to the OpenAI API and return the response."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation + [{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


def time_tracker(start_time, time_limit, stop_event):
    """Track elapsed time and notify agents about remaining time."""
    while not stop_event.is_set():
        elapsed = time.time() - start_time
        if elapsed >= time_limit:
            print(f"Time limit reached: {time_limit} seconds. Stopping execution.")
            stop_event.set()
            break
        time.sleep(1)


def save_solution(num_agents, iterations, time_limit, solution, replicate):
    """Save the final solution to a text file with the appropriate naming convention."""
    iter_str = "inf" if iterations >= 10**18 else str(iterations)
    time_str = "inf" if time_limit == math.inf else str(time_limit)
    filename = f"{num_agents}_{iter_str}_{time_str}_{replicate}.py"
    file_path = os.path.join(PROGRAMS_DIR, filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(solution)

    print(f"Solution saved to {file_path}")


def main(num_agents=2, iterations=5, time_limit=60, replicate=1):
    clients = create_clients(num_agents)
    stop_event = threading.Event()
    start_time = time.time()
    generation_times = []  # Store time taken for each generation

    # Start timer thread if time_limit is not infinity
    if time_limit < math.inf:
        timer_thread = threading.Thread(
            target=time_tracker, args=(start_time, time_limit, stop_event)
        )
        timer_thread.start()
    else:
        timer_thread = None

    team_instruction = "You are part of a team with other Python programmers. Work together to solve the problem."
    prompt = f"""
    {team_instruction if num_agents > 1 else ""}
    Write Python code to solve this problem:
    {PROBLEM_STATEMENT}
    """

    print(prompt)

    conversation = [
        {"role": "system", "content": "You are a helpful Python programmer."}
    ]

    iteration_start = time.time()  # Start timing the first generation
    solution = chat_with_llm(clients[0], prompt, conversation)
    generation_times.append(time.time() - iteration_start)  # Record generation time
    conversation.append({"role": "assistant", "content": solution})

    for i in range(2, iterations + 1):  # Start from 2nd iteration
        if stop_event.is_set():
            break

        agent = (i - 1) % num_agents  # Round-robin selection of agents
        remaining_time = max(0, time_limit - (time.time() - start_time))

        if remaining_time <= 0:
            print("Time's up. Stopping further refinements.")
            stop_event.set()
            break

        time_limit_instruction = (
            f"You{'r team' if num_agents > 1 else ''} have {remaining_time:.2f} seconds remaining to deliver the final solution."
            if time_limit < math.inf
            else ""
        )

        python_solution = extract_python_code(solution)

        review_prompt = f"""
        Here is the current Python solution {"proposed by your team" if num_agents > 1 else ""}:
        Optimize it for faster execution.
        {time_limit_instruction}

        CURRENT SOLUTION:
        {python_solution}
        """

        print(review_prompt)

        iteration_start = time.time()  # Start timing
        solution = chat_with_llm(clients[agent], review_prompt, conversation)
    generation_times.append(time.time() - iteration_start)  # Record time
    conversation.append({"role": "assistant", "content": solution})

    stop_event.set()
    if timer_thread:
        timer_thread.join()

    print("Final Solution:")
    python_solution = extract_python_code(solution)
    print(python_solution)

    save_solution(num_agents, iterations, time_limit, python_solution, replicate)

    # Calculate and display the average generation time
    avg_time = sum(generation_times) / len(generation_times)
    print(f"\nAverage time per generation: {avg_time:.2f} seconds")


if __name__ == "__main__":
    main(num_agents=1, iterations=3, time_limit=math.inf, replicate=1)
    main(num_agents=1, iterations=8, time_limit=math.inf, replicate=1)
    main(num_agents=2, iterations=3, time_limit=math.inf, replicate=1)
    main(num_agents=2, iterations=8, time_limit=math.inf, replicate=1)
    main(num_agents=3, iterations=3, time_limit=math.inf, replicate=1)
    main(num_agents=3, iterations=8, time_limit=math.inf, replicate=1)

    main(num_agents=1, iterations=10**18, time_limit=60, replicate=1)
    main(num_agents=1, iterations=10**18, time_limit=120, replicate=1)
    main(num_agents=2, iterations=10**18, time_limit=60, replicate=1)
    main(num_agents=2, iterations=10**18, time_limit=120, replicate=1)
    main(num_agents=3, iterations=10**18, time_limit=60, replicate=1)
    main(num_agents=3, iterations=10**18, time_limit=120, replicate=1)

    main(num_agents=1, iterations=3, time_limit=math.inf, replicate=2)
    main(num_agents=1, iterations=8, time_limit=math.inf, replicate=2)
    main(num_agents=2, iterations=3, time_limit=math.inf, replicate=2)
    main(num_agents=2, iterations=8, time_limit=math.inf, replicate=2)
    main(num_agents=3, iterations=3, time_limit=math.inf, replicate=2)
    main(num_agents=3, iterations=8, time_limit=math.inf, replicate=2)

    main(num_agents=1, iterations=10**18, time_limit=60, replicate=2)
    main(num_agents=1, iterations=10**18, time_limit=120, replicate=2)
    main(num_agents=2, iterations=10**18, time_limit=60, replicate=2)
    main(num_agents=2, iterations=10**18, time_limit=120, replicate=2)
    main(num_agents=3, iterations=10**18, time_limit=60, replicate=2)
    main(num_agents=3, iterations=10**18, time_limit=120, replicate=2)
