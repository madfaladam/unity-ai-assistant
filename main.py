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
    description = issue.description.lower()
    possible_causes = []
    recommended_actions = []

    if "upside down" in description:
        possible_causes.append(
            "WebcamTexture.videoVerticallyMirrored is true, causing the video feed to appear upside down."
            )
        recommended_actions.append(
            "Apply a vertical UI scale based on videoVerticallyMirrored."
            )

        if "mirror" in description:
            possible_causes.append(
                "The front camera or RawImage transform may apply horizontal mirroring."
            )
            recommended_actions.append(
                "Check RawImage uvRect and localScale.x before applying another flip."
            )

        if "stretch" in description:
            possible_causes.append(
                "The camera aspect ratio does not match the RawImage container."
            )
            recommended_actions.append(
                "Update AspectRatioFitter.aspectRatio using video width and height."
            )

        if not possible_causes:
            possible_causes.append("No known pattern was detected.")
            recommended_actions.append(
                "Collect the Unity logs, platform, and reproduction steps."
            )    
            
    return {
        "success": True,
        "input": issue,
        "analysis": {
            "possible_causes": possible_causes,
            "recommended_actions": recommended_actions
        },
    }