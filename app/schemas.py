from pydantic import BaseModel
from typing import List, Dict

class CandidateResponse(BaseModel):
    name: str
    responses: Dict[str, str]

class ShiftPosting(BaseModel):
    title: str
    location: str
    schedule: str
    requirements: List[str]

class ScreeningInput(BaseModel):
    candidate_responses: CandidateResponse
    shift_posting: ShiftPosting

class ScreeningOutput(BaseModel):
    score: int
    decision: str
    explanation: str