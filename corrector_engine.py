# code_debugging_assistant/corrector_engine.py

from logic_weights import get_weighted_fix, update_weights

def simulate_fix(code):
    if "append" in code and "reverse" in code:
        fixed = code.replace("append", "insert(0")
        reason = "Used 'insert(0, item)' instead of 'append()' for reversing."
    elif "= lst[i]" in code:
        fixed = code.replace("= lst[i]", "+= lst[i]")
        reason = "Changed overwrite to accumulation with '+='."
    elif "n" in code and "range(1, n)" in code:
        fixed = code.replace("range(1, n)", "range(1, n+1)")
        reason = "Fixed off-by-one in loop range."
    elif "=" in code and "==" not in code:
        fixed = code.replace("=", "==")
        reason = "Changed assignment to comparison operator."
    elif "result *= i" in code and "result" not in code.split("\n")[0]:
        fixed = "result = 1\n" + code
        reason = "Missing initialization of 'result'."
    else:
        fixed = code
        reason = "No matching fix rule found."

    return fixed, reason

def learn_from_user_fix(buggy, fixed):
    update_weights(buggy, fixed)
