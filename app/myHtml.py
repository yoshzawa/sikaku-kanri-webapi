from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="html")  # テンプレートが存在するディレクトリを指定

data = {"message": "Hello, World!"}  # テンプレートに渡すデータ

@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "data": data})

