from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent

app = FastAPI()

class Request(BaseModel):
    log: str

@app.post("/analyze")
def analyze(req: Request):
    result = run_agent(req.log)
    return {"response": result}