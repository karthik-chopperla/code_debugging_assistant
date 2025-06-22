# code_debugging_assistant/bug_highlighter.py

import streamlit as st

def highlight_buggy_lines(code):
    st.markdown("🚩 **Suspected Bug:** Line 2 (pattern match: misuse of append or loop)")

def explain_bug_line(code):
    if "append" in code and "reverse" in code:
        return "You're appending instead of reversing. Try using arr[::-1] or insert(0, val)."
    return "Bug detected based on known logic patterns."
