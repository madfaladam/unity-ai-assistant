from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Unity AI Assistant", 
    description="A simple AI assistant for Unity developers", 
    version="1.0.0"
    )

class UnityIssue(BaseModel):
    title: str
    description: str
    platform: str
    unity_version: str | None = None


@app.get("/")
def home():
    return {
        "message": "Welcome to the Unity AI Assistant API!",
        "status": "running"
    }

@app.post("/analyze")
def analyze_issue(issue: UnityIssue):
    return {
        "success": True,
        "input": issue,
        "analysis": {
            "possible_cause": "The issue requires further investigation based on the provided description and platform.",
            "recommended_action": "Please provide more details or check Unity's official documentation for troubleshooting steps."
        },
    }