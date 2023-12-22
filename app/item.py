# main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal, Item

app = FastAPI()

# データベースセッションを取得する依存関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/list")
async def get_item_list(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items
