from fastapi import FastAPI

app = FastAPI()

# 商品リストのデータ
voucherTypes = [
    {"ID": "FESG", "NAME": "FE/SG受験バウチャー"},
    {"ID": "OR00", "NAME": "Oracle認定資格ピアソンVUE 配信監督なし試験用"}
]

@app.get("/list")
def get_voucher_type_list(token:str):
    return voucherTypes

@app.get("/{ID}")
def get_voucher_type_item(ID:str,token:str):
    if ID == "FESG":
        return voucherTypes[0]
    elif ID == "OR00":
        return voucherTypes[1]
    else:
        return {}

@app.post("/add")
def get_voucherType_item(ID:str,NAME:str,token:str):
    return {"message": "voucherType was not added successfully", "voucherType": {}}
	