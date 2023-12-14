from fastapi import FastAPI

app = FastAPI()

# 商品リストのデータ
products = [
    {"ID": "FE00", "NAME": "基本情報技術者試験", "DATE": "2022/06/18"},
    {"ID": "OR00", "NAME": "Java SE Bronze", "DATE": "2023/02/20"}
]

@app.get("/list")
def get_product_list():
    return products
