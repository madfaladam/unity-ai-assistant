import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel, Field


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL", "gpt-5.6")

client = OpenAI(api_key=api_key) if api_key else None

app = FastAPI(
    title="Unity AI Assistant", 
    description="A simple AI assistant for Unity developers", 
    version="0.2.0"
    )

class UnityIssue(BaseModel):
    title: str = Field(
        min_length=3, 
        max_length=150, 
        example=["Webcam feed appears upside down"],
        )
    description: str = Field(
        min_length=10,
        example=["The webcam feed is appearing upside down on my Android device."]
    )
    platform: str = Field(
        min_length=2,
        max_length=100,
        example=["iOS"]
    )
    unity_version: str | None = Field(
        default=None,
        example=["Optional Unity C# code related to the issue"],
    )
    code: str | None = Field(
        default=None,
        description="Optional Unity C# code related to the issue",
        example=["public void Start() { }"]
    )

@app.get("/")
def home():
    return {
        "application": "Welcome to the Unity AI Assistant API!",
        "version": "0.2.0",
        "status": "running",
        "ai_configured": client is not None,
    }

@app.post("/analyze")
def analyze_issue(issue: UnityIssue):
    if client is None:
        raise HTTPException(
            status_code=500,
            detail="OpenAI API key is not configured. Please set the OPENAI_API_KEY environment variable."
        )

    prompt = f"""
You are an AI assistant for Unity developers. Analyze the following issue and provide possible causes and recommended

    Title: 
    {issue.title}

    Description: 
    {issue.description}

    Platform: 
    {issue.platform}

    Unity Version: 
    {issue.unity_version or "Not provided"}
    
    Related Code: 
    {issue.code or "Not provided"}

    Provide the answer using these sections:
    1. Most likely cause
    2. Technical explanation
    3. Recommended actions
    4. Example Unity C# code (if applicable)
    5. Additional checks

    Important requirements:
    - Do not invent Unity APIs.
    - Clearly state when information is insufficient to provide a definitive answer.
    - Consider platform-specific behavior.
    - Keep the explanation concise and practical.
"""

    try:
        response = client.responses.create(
            model=model_name,
            instructions=(
                "You are a senior Unity engineer specializing in "
                "Unity 6, mobile development, iOS, Android, camera, "
                "audio, Addressables, performance, and debugging."
            ),
            input=prompt,
        )

        return {
            "success": True,
            "model": model_name,
            "issue": issue.model_dump(),
            "analysis": response.output_text,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing the issue: {str(e)}"
        ) from e