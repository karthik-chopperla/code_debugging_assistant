# code_debugging_assistant/task_generator.py

import random

def generate_task_bug_pair(prompt):
    """
    Takes a user task prompt, generates a general function for it,
    and injects a random bug into it using rule-based corruption.
    """
    func_name = prompt.strip().lower().replace(" ", "_")[:15] or "task"
    func_code = f"""def {func_name}(data):
    result = []
    for item in data:
        result.append(item)
    return result"""

    buggy_code = inject_random_bug(func_code)
    return buggy_code

def inject_random_bug(code):
    """
    Applies one random bug from the bug rules below.
    """
    bug_rules = [
        lambda c: c.replace("append", "insert"),  # wrong method
        lambda c: c.replace("for item in data", "for item in range(data)"),  # wrong loop
        lambda c: c.replace("return result", "return data"),  # wrong return
        lambda c: c.replace("result = []\n", ""),  # missing init
        lambda c: c.replace("item in data", "i in data"),  # undeclared variable
        lambda c: c.replace("result.append(item)", "result += item"),  # wrong operator
    ]
    return random.choice(bug_rules)(code)
