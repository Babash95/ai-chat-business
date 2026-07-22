from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>AI Chat Business</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f6f8;
                padding: 40px;
            }

            .box {
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 15px #ccc;
            }

            textarea {
                width: 100%;
                height: 100px;
            }

            button {
                margin-top: 15px;
                padding: 12px 25px;
                background: #2563eb;
                color: white;
                border: none;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>
        <div class="box">

        <h1>🤖 AI Chat Business</h1>

        <p>AI помощник для малого бизнеса</p>

        <form action="/chat" method="post">

            <textarea 
            name="message"
            placeholder="Напишите вопрос..."
            ></textarea>

            <br>

            <button>
            Отправить
            </button>

        </form>

        </div>
    </body>
    </html>
    """


@app.post("/chat", response_class=HTMLResponse)
def chat(message: str = Form(...)):

    answer = f"""
    <h2>Ваш вопрос:</h2>
    <p>{message}</p>

    <h2>Ответ AI:</h2>
    <p>
    Спасибо за вопрос. 
    Я AI-помощник для малого бизнеса.
    Скоро я смогу помогать с клиентами,
    продажами и документами.
    </p>

    <a href="/">← Новый вопрос</a>
    """

    return answer