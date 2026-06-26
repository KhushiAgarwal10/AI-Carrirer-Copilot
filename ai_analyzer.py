from dotenv import load_dotenv
import os

from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import Model

load_dotenv()

API_KEY = os.getenv("IBM_API_KEY")
PROJECT_ID = os.getenv("IBM_PROJECT_ID")
IBM_URL = os.getenv("IBM_URL")

credentials = Credentials(
    api_key=API_KEY,
    url=IBM_URL
)

model = Model(
    model_id="meta-llama/llama-3-3-70b-instruct",
    credentials=credentials,
    project_id=PROJECT_ID
)

from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams


def analyze_resume(resume_text):

    prompt = f"""
You are an expert ATS Resume Analyzer and Career Coach.

IMPORTANT INSTRUCTIONS:
- Generate a COMPLETE report.
- DO NOT stop after ATS Score.
- Complete EVERY section.
- The response should be around 800-1200 words.
- Use proper Markdown headings.
- Use bullet points wherever appropriate.

Generate ALL of these sections:

# 📊 ATS Score
Give a score out of 100 with explanation.

# 📝 Professional Summary

# 💻 Technical Skills

# 🤝 Soft Skills

# ❌ Missing Skills

# 💪 Strengths
Provide at least 5 points.

# ⚠ Weaknesses
Provide at least 5 points.

# 💼 Best Job Roles
Suggest at least 5 job roles.

# 🚀 Suggested Projects
Suggest exactly 3 portfolio-worthy projects.

# 📚 3-Month Learning Roadmap
Month 1
Month 2
Month 3

# 📈 Resume Improvement Tips
Provide at least 8 suggestions.

Resume:

{resume_text}
"""

    params = {
        GenParams.MAX_NEW_TOKENS: 1200,
        GenParams.MIN_NEW_TOKENS: 600,
        GenParams.TEMPERATURE: 0.3,
        GenParams.TOP_P: 0.9,
    }

    try:
        response = model.generate_text(
            prompt=prompt,
            params=params
        )

        return response

    except Exception as e:
        return f"❌ Error: {str(e)}"