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


async def login_user(username: str, password: str):
    async with httpx.AsyncClient() as client:
        response = await client.post("/account/login", data={"username": username, "password": password})
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Login failed")
    
    return response.json()

@router.post("/check")
async def check_user(request: Request, username: str, password: str):
    login_data = await login_user(username, password)
    
    status = login_data.get("Status")
    token = login_data.get("Token")
    message = login_data.get("message")
    
    return {"Status": status, "Token": token, "message": message}







