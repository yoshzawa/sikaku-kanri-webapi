from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from typing import Optional
import httpx

router = APIRouter()
templates = Jinja2Templates(directory="html")  # テンプレートが存在するディレクトリを指定


@router.get("/")
async def read_root(request: Request):
    data = {"message": "Hello, World!"}  # テンプレートに渡すデータ
    return templates.TemplateResponse("login.html", {"request": request, "data": data})


async def login_user(base_url: str, username: str, password: str):
    login_url = f"{base_url}/account/login"
    print(f"Login URL: {login_url}")  # ログにURLを出力


    async with httpx.AsyncClient() as client:
        response = await client.post(login_url, data={"username": username, "password": password})
    print(f"Status Code: {response.status_code}")  # ステータスコードをログに出力
   
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Login failed")
    
    return response.json()

@router.post("/check")
async def check_user(request: Request, username: str, password: str):
    base_url = str(request.base_url)
    login_data = await login_user(base_url, username, password)

    status = login_data.get("Status")
    token = login_data.get("Token")
    message = login_data.get("message")
    
    return {"Status": status, "Token": token, "message": message}
