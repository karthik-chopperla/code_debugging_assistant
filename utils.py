# code_debugging_assistant/utils.py

def is_syntax_valid(code: str) -> bool:
    try:
        compile(code, "<string>", "exec")
        return True
    except:
        return False

def get_timer():
    import time
    return time.time()
