from fastapi import FastAPI

app = FastAPI()

# 商品リストのデータ
vouchers = [
    {"ID": "FESG", "NAME": "FE/SG受験バウチャー", "DATE": "2024/06/20"},
    {"ID": "OR00", "NAME": "Oracle認定資格ピアソンVUE 配信監督なし試験用", "DATE": "2023/12/25"}
]

@app.get("/list")
def get_voucher_list(token:str):
    return vouchers

@app.get("/{ID}")
def get_voucher_item(ID:str,token:str):
    if ID == "FESG":
        return vouchers[0]
    elif ID == "OR00":
        return vouchers[1]
    else:
        return {}

@app.post("/add")
def add_voucher_item(ID:str,DATE:str,token:str):
    return {"message": "voucher was added successfully", "voucher": {{"ID": "FESG" , "DATE": "2024/06/20"}}}
	