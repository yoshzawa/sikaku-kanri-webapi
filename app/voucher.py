from fastapi import FastAPI

app = FastAPI()

# 商品リストのデータ
vouchers = [
    {"ID": "FESG", "NAME": "FE/SG受験バウチャー", "DATE": "2024/06/20"},
    {"ID": "OR00", "NAME": "Oracle認定資格ピアソンVUE 配信監督なし試験用", "DATE": "2023/12/25"}
]

@app.get("/list")
def get_voucher_list():
    return vouchers
