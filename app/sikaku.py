from fastapi import FastAPI

app = FastAPI()

# 商品リストのデータ
products = [
    {"ID": 10, "NAME": "APPLE", "PRICE": 250},
    {"ID": 20, "NAME": "BANANA", "PRICE": 150}
]

@app.get("/list")
def get_product_list():
    return products
