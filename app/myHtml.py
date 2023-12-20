from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="html")  # テンプレートが存在するディレクトリを指定

async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "data": data})
