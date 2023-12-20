from fastapi import FastAPI

app = FastAPI()

# 商品リストのデータ
voucherTypes = [
    {"ID": "FESG", "NAME": "FE/SG受験バウチャー"},
    {"ID": "OR00", "NAME": "Oracle認定資格ピアソンVUE 配信監督なし試験用"}
]

@app.get("/list")
def get_voucher_type_list():
    return voucherTypes
