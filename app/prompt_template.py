from langchain.prompts import PromptTemplate

screening_prompt = PromptTemplate.from_template("""
You are an AI screening assistant. Given the candidate's responses and job requirements, evaluate their fit.
Respond with:
- A score (0–100),
- A short hiring decision,
- A brief explanation why.

Candidate Responses:
Name: {name}
Availability: {availability}
Experience: {experience}
Skills: {skills}
Location: {location}
Other: {other}

Shift Details:
Title: {title}
Location: {job_location}
Schedule: {schedule}
Requirements: {requirements}

Respond in this format (JSON):
{{
  "score": <int>,
  "decision": "<Great fit|Good fit|Average|Poor fit|Missing requirement>",
  "explanation": "<brief explanation>"
}}
""")