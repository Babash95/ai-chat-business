from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
  return templates.TemplateResponse(
    request=request,
    name="index.html"
)


@app.post("/chat", response_class=HTMLResponse)
def chat(message: str = Form(...)):

    answer = """
    Спасибо за ваш вопрос.

    Я AI-помощник для малого бизнеса.
    Скоро я смогу помогать с клиентами,
    продажами и документами.
    """

    return f"""
    <html>
    <body>
        <h1>🤖 AI Chat Business</h1>

        <h3>Ваш вопрос:</h3>
        <p>{message}</p>

        <h3>Ответ AI:</h3>
        <p>{answer}</p>

        <a href="/">← Новый вопрос</a>
    </body>
    </html>
    """