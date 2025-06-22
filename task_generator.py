# code_debugging_assistant/task_generator.py

import random

def generate_task_bug_pair(prompt):
    base_function = build_function_from_prompt(prompt)
    buggy_function = inject_bug(base_function)
    return buggy_function

def build_function_from_prompt(prompt):
    task = prompt.lower()

    if "sum" in task:
        return """def calc_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total"""

    elif "reverse" in task:
        return """def reverse_list(lst):
    result = []
    for item in lst:
        result.insert(0, item)
    return result"""

    elif "factorial" in task:
        return """def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result"""

    else:
        return f"""def custom_func(input_data):
    # TODO: Implement task - '{prompt}'
    return input_data"""

def inject_bug(code):
    bug_rules = [
        lambda c: c.replace("n+1", "n"),  # off-by-one
        lambda c: c.replace("==", "="),  # logic error
        lambda c: c.replace("result = 1", ""),  # missing init
        lambda c: c.replace("total += lst[i]", "total = lst[i]"),  # overwrite instead of sum
        lambda c: c.replace("insert(0", "append"),  # wrong method
    ]
    return random.choice(bug_rules)(code)
