# code_debugging_assistant/bug_fixer.py

def simulate_custom_fix(code):
    if "range(len(" in code and "+1" in code:
        return code.replace("+1", "-1"), "Fixed off-by-one error"
    elif "sum" in code and "total" in code:
        return code.replace("sum", "0"), "Corrected wrong sum initialization"
    elif "=" in code and "==" not in code and "if" in code:
        return code.replace("=", "=="), "Corrected assignment in condition"
    return code, "No known fix found"
