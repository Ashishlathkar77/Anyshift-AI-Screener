import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from app.prompt_template import screening_prompt

load_dotenv()

llm = OpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

def run_screening_llm(data: dict) -> dict:
    chain = LLMChain(llm=llm, prompt=screening_prompt)
    output = chain.run(
        name=data['candidate_responses']['name'],
        availability=data['candidate_responses']['responses']['availability'],
        experience=data['candidate_responses']['responses']['experience'],
        skills=data['candidate_responses']['responses']['skills'],
        location=data['candidate_responses']['responses']['location'],
        other=data['candidate_responses']['responses']['other'],
        title=data['shift_posting']['title'],
        job_location=data['shift_posting']['location'],
        schedule=data['shift_posting']['schedule'],
        requirements=", ".join(data['shift_posting']['requirements']),
    )
    return eval(output)  # safe here since we control the format