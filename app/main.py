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
def chat(
    message: str = Form(...),
    assistant: str = Form(...)
):

    messages.append({
        "role": "user",
        "text": message
    })

    if assistant == "customer":

        if "не хочет" in message.lower() or "отказ" in message.lower():
            answer = """
            Здравствуйте!

            Спасибо, что сообщили нам.
            Мы понимаем ваше решение и хотели бы узнать причину отказа.

            Возможно, мы сможем предложить удобное решение.
            """

        elif "доставка" in message.lower():
            answer = """
            Здравствуйте!

            Приносим извинения за задержку доставки.
            Мы проверим статус заказа и сообщим вам актуальную информацию.
            """

        else:
            answer = """
            Я помогу обработать обращение клиента.
            Пожалуйста, уточните детали ситуации.
            """

    elif assistant == "marketing":
        answer = """
        ✍️ Я помогу создать рекламный текст,
        посты и маркетинговые идеи.
        """

    elif assistant == "sales":
        answer = """
        💼 Я помогу подготовить предложения
        и увеличить продажи.
        """

    elif assistant == "documents":
        answer = """
        📄 Я помогу создавать письма,
        инструкции и документы.
        """

    else:
        answer = "Я AI-помощник для бизнеса."

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