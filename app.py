# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle, numpy as np
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

model = pickle.load(open("model.pkl", "rb"))

class DevInput(BaseModel):
    experience: float
    commits_per_week: float
    prs_merged: float
    review_hours: float
    bug_fix_rate: float
    focus_hours: float
    meeting_hours: float
    doc_score: float
    team_size: float

@app.post("/predict")
def predict(data: DevInput):
    features = np.array([[data.experience, data.commits_per_week, data.prs_merged,
                          data.review_hours, data.bug_fix_rate, data.focus_hours,
                          data.meeting_hours, data.doc_score, data.team_size]])
    score = model.predict(features)[0]
    return {"performance_score": round(float(score), 2)}


