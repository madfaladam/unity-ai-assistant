# Unity AI Assistant

An AI-powered debugging assistant that helps Unity developers analyze bugs, understand possible causes, and generate practical solutions. Built with Python, FastAPI, and the OpenAI Responses API.

## Features

- Analyze Unity errors and development issues
- Generate practical debugging recommendations
- Include optional Unity C# code in the analysis
- Support platform and Unity version context
- Access the API through interactive Swagger documentation

## Requirements

- Python 3.11 or newer
- An OpenAI API key with available API credits

> ChatGPT subscriptions and OpenAI API billing are separate. Your API account must have available credits to send requests.

## How to Use

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd unity-ai-assistant
```

Replace `<your-repository-url>` with the URL of this GitHub repository.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5.6
```

Never commit your `.env` file or expose your API key publicly.

### 5. Run the API

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

### 6. Open the API documentation

Open the Swagger interface in your browser:

```text
http://127.0.0.1:8000/docs
```

Select `POST /analyze`, click **Try it out**, and submit a Unity issue.

Example request:

```json
{
  "title": "WebCamTexture upside down on iPhone",
  "description": "The camera is correct in the Unity Editor, but it appears upside down and stretched on iPhone.",
  "platform": "iOS",
  "unity_version": "6000.0.70f1",
  "code": "rawImage.texture = webCamTexture; webCamTexture.Play();"
}
```

Example response:

```json
{
  "success": true,
  "model": "gpt-5.6",
  "issue": {
    "title": "WebCamTexture upside down on iPhone",
    "platform": "iOS"
  },
  "analysis": "The most likely cause is incorrect handling of WebCamTexture rotation and vertical mirroring..."
}
```

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Check API status and AI configuration |
| `POST` | `/analyze` | Analyze a Unity development issue |

## Common Errors

### `OPENAI_API_KEY has not been configured`

Make sure the `.env` file exists in the project root and contains a valid `OPENAI_API_KEY`. Restart the server after changing it.

### `429 insufficient_quota`

Your OpenAI API account does not have enough credits, or its usage limit has been reached. Check the billing and usage settings on the OpenAI Platform.

## Tech Stack

- Python
- FastAPI
- Pydantic
- OpenAI Responses API
- Uvicorn

## Roadmap

- Return structured AI analysis as JSON
- Add confidence levels and severity categories
- Add conversation history
- Add Unity documentation retrieval with RAG
- Build a web interface
- Connect the API directly to a Unity project

## License

This project is intended for learning and portfolio development.
