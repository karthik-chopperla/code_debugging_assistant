# code_debugging_assistant/app.py

import streamlit as st
from task_generator import generate_task_bug_pair
from bug_highlighter import highlight_buggy_lines, explain_bug_line
from corrector_engine import simulate_fix, learn_from_user_fix
from explain_engine import explain_code_bug
from user_tracker import track_fix, get_debugging_score
from bug_fixer import simulate_custom_fix
from utils import is_syntax_valid

st.set_page_config(page_title="Code Debugging Assistant", layout="wide")
st.title("🧠 Code Debugging Assistant")

tab1, tab2, tab3 = st.tabs(["🔁 Task Generator", "🛠 Paste Your Bug", "📊 Your Stats"])

# ------------------------------------------
# 🔁 Tab 1: Task Generator
# ------------------------------------------
with tab1:
    st.subheader("🧪 A. Generate Buggy Code from Prompt")
    prompt = st.text_input("Enter a Python task (e.g., 'reverse a string')")

    if st.button("Generate Buggy Code"):
        if prompt.strip():
            buggy = generate_task_bug_pair(prompt)
            st.code(buggy, language="python")
            st.session_state["buggy_code"] = buggy

    if "buggy_code" in st.session_state:
        if st.button("Explain This Bug"):
            explanation = explain_bug_line(st.session_state["buggy_code"])
            st.info(explanation)

        if st.button("Suggest Fix"):
            fixed_code, reason = simulate_fix(st.session_state["buggy_code"])
            st.code(fixed_code, language="python")
            st.info(reason)

            if st.button("I Accept This Fix"):
                learn_from_user_fix(st.session_state["buggy_code"], fixed_code)
                track_fix(user_fixed=True)
                st.success("✅ Fix accepted and learning updated!")

# ------------------------------------------
# 🛠 Tab 2: Custom Bug Mode
# ------------------------------------------
with tab2:
    st.subheader("🛠 Paste Your Bug")
    user_code = st.text_area("Paste your buggy Python code here", height=200)

    if st.button("Fix My Code"):
        if not is_syntax_valid(user_code):
            st.error("❌ Syntax error found. Please paste valid Python code.")
        else:
            fixed, reason = simulate_custom_fix(user_code)
            st.code(fixed, language="python")
            st.info(reason)

    if st.button("Explain Why It’s Wrong"):
        explanation = explain_code_bug(user_code)
        st.warning(explanation)

    if st.button("✔️ I Fixed It Myself"):
        track_fix(user_fixed=True)
        st.success("Your fix has been recorded.")

# ------------------------------------------
# 📊 Tab 3: Stats
# ------------------------------------------
with tab3:
    st.subheader("📈 Debugging IQ Score")
    score, total = get_debugging_score()
    st.metric("Your Debugging IQ", f"{score} / {total}")
