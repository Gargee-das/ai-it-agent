from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from app.database import create_user, reset_password, assign_license

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    with open("frontend/index.html") as f:
        return f.read()

@app.post("/create_user")
def create(email: str = Form(...)):
    return {"message": create_user(email)}

@app.post("/reset_password")
def reset(email: str = Form(...)):
    return {"message": reset_password(email)}

@app.post("/assign_license")
def assign(email: str = Form(...)):
    return {"message": assign_license(email)}

from app.agent import parse_task
from automation.browser_agent import perform_action

@app.post("/ai_task")
def ai_task(query: str = Form(...)):
    task = parse_task(query)

    if task["action"] == "create_and_assign":
        perform_action({"action": "create_user", "email": task["email"]})
        perform_action({"action": "assign_license", "email": task["email"]})
    else:
        perform_action(task)

    return {"task": task}

from automation.browser_agent import perform_notion_task

@app.get("/test_notion")
def test_notion():
    perform_notion_task()
    return {"status": "done"}

@app.post("/chat")
def chat(message: str = Form(...)):
    task = parse_task(message)
    perform_action(task)
    return {"reply": "Task completed"}