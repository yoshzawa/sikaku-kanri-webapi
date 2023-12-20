from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="html")  # テンプレートが存在するディレクトリを指定

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "data": data})
