# code_debugging_assistant/explain_engine.py

def explain_code_bug(code):
    lines = code.split("\n")
    explanations = []

    for i, line in enumerate(lines):
        if "append" in line and "reverse" in code:
            explanations.append(f"Line {i+1}: Used 'append()' instead of 'insert(0, item)' — wrong for reversing.")
        if "range(1, n)" in line:
            explanations.append(f"Line {i+1}: Off-by-one bug — range should go to n+1.")
        if "= lst[i]" in line:
            explanations.append(f"Line {i+1}: Overwriting value instead of accumulating with '+='.")
        if "==" not in line and "=" in line and "if" in line:
            explanations.append(f"Line {i+1}: Assignment '=' used in condition — should be '=='.")
        if "result *= i" in line and not any("result = 1" in l for l in lines):
            explanations.append(f"Line {i+1}: Using result before initializing it.")

    return "\n".join(explanations) if explanations else "❓ No clear bug pattern found."
