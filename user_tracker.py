# code_debugging_assistant/user_tracker.py

score_data = {"correct": 0, "total": 0}

def track_fix(user_fixed=False):
    score_data["total"] += 1
    if user_fixed:
        score_data["correct"] += 1

def get_debugging_score():
    return score_data["correct"], score_data["total"]
