# code_debugging_assistant/logic_weights.py

# Simulates AI learning via rule weights (offline logic engine)

rule_memory = {}

def get_weighted_fix(code):
    return rule_memory.get(code, code)

def update_weights(buggy, fixed):
    rule_memory[buggy] = fixed
