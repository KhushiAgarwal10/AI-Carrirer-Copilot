# import streamlit as st
# from resume_parser import extract_text
# from ai_analyzer import analyze_resume

# st.set_page_config(
#     page_title="AI Career Copilot",
#     page_icon="🤖",
#     layout="wide"
# )

# st.title("🤖 AI Career Copilot")

# st.markdown("""
# ### AI Powered Resume Analyzer

# Upload your resume and receive:

# - 📊 ATS Score
# - 👨‍💻 Skills Analysis
# - ❌ Missing Skills
# - 💪 Strengths
# - ⚠ Weaknesses
# - 💼 Career Recommendations
# - 🚀 Suggested Projects
# - 📚 Learning Roadmap
# """)

# uploaded_file = st.file_uploader(
#     "Upload Resume (PDF)",
#     type=["pdf"]
# )

# if uploaded_file is not None:

#     resume_text = extract_text(uploaded_file)

#     st.success("✅ Resume uploaded successfully!")

#     with st.expander("📄 Extracted Resume Text"):

#         st.write(resume_text)

#     if st.button("🚀 Analyze Resume"):

#         with st.spinner("Analyzing resume using IBM watsonx.ai..."):

#             result = analyze_resume(resume_text)

#         st.success("Analysis Completed!")

#         st.markdown("---")

#         st.subheader("📊 Analysis Result")

#         st.write(result)

# st.markdown("---")

# st.caption("Powered by IBM watsonx.ai | Meta Llama 3.3 70B | Streamlit")




import streamlit as st
from resume_parser import extract_text
from ai_analyzer import analyze_resume

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Load CSS
# -----------------------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🤖 AI Career Copilot")

st.sidebar.markdown("---")

st.sidebar.info("""
### Features

✅ ATS Score

✅ Skills Detection

✅ Missing Skills

✅ Career Recommendations

✅ Suggested Projects

✅ Learning Roadmap

Powered by IBM watsonx.ai
""")

st.sidebar.markdown("---")

st.sidebar.success("AI Resume Analyzer")

# -----------------------------
# Header
# -----------------------------
st.title("🤖 AI Career Copilot")

st.markdown(
"""
### AI Powered Resume Analyzer

Upload your resume and receive:

- 📊 ATS Score
- 💻 Technical Skills
- 🤝 Soft Skills
- ❌ Missing Skills
- 💪 Strengths
- ⚠ Weaknesses
- 💼 Career Recommendations
- 🚀 Suggested Projects
- 📚 Learning Roadmap
"""
)

st.divider()

# -----------------------------
# Upload Section
# -----------------------------
uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

# -----------------------------
# Resume Processing
# -----------------------------
if uploaded_file is not None:

    resume_text = extract_text(uploaded_file)

    st.success("✅ Resume uploaded successfully!")

    with st.expander("📄 Preview Extracted Resume"):

        st.write(resume_text)

    if st.button("🚀 Analyze Resume"):

        with st.spinner("Analyzing Resume using IBM watsonx.ai..."):

            result = analyze_resume(resume_text)

        st.success("✅ Analysis Completed")

        st.divider()

        st.subheader("📊 Analysis Report")

        st.markdown(result)

        st.divider()

        st.download_button(
            label="📥 Download Report",
            data=result,
            file_name="AI_Career_Copilot_Report.txt",
            mime="text/plain"
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.markdown(
"""
<div class='footer'>
Developed by <b>Khushi Agarwal</b><br>
Powered by IBM watsonx.ai • Meta Llama 3.3 • Streamlit
</div>
""",
unsafe_allow_html=True
)