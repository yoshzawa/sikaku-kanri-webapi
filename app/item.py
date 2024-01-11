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

@app.post("/add")
async def add_item(item_id: int, item_name: str, price: int, db: Session = Depends(get_db)):
    new_item = Item(item_id=item_id, item_name=item_name, price=price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": "Item was added successfully", "item": new_item}
