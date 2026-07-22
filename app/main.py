from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.ai_service import generate_response

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

messages = []


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "messages": messages
        }
    )


@app.post("/chat", response_class=HTMLResponse)
def chat(
    message: str = Form(...),
    assistant: str = Form(...)
):

    messages.append({
        "role": "user",
        "text": message
    })

    answer = generate_response(message, assistant)

    messages.append({
        "role": "ai",
        "text": answer
    })

    return HTMLResponse(
        """
        <script>
        window.location.href="/";
        </script>
        """
    )