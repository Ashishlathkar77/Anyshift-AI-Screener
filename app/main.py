from fastapi import FastAPI
from app.schemas import ScreeningInput, ScreeningOutput
from app.model import run_screening_llm
from app.evaluation import evaluate_match

app = FastAPI()

@app.post("/screen", response_model=ScreeningOutput)
def screen_candidate(data: ScreeningInput):
    result = run_screening_llm(data.dict())
    explanation = evaluate_match(result["score"])
    return {
        "score": result["score"],
        "decision": result["decision"],
        "explanation": explanation
    }