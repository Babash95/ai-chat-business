from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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
def chat(message: str = Form(...)):

    messages.append({
        "role": "user",
        "text": message
    })

    messages.append({
        "role": "ai",
        "text": "Спасибо за вопрос. Я AI-помощник для малого бизнеса."
    })

    return HTMLResponse(
        """
        <script>
        window.location.href="/";
        </script>
        """
    )