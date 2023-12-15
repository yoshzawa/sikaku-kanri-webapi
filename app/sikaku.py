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

@app.get("/{ID}")
def get_product_item(ID:str):
    if ID == "FE00":
        return products[0]
    elif ID == "FE01":
        return products[1]
    else:
        return {}

