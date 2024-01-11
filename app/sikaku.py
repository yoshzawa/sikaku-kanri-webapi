from fastapi import FastAPI

app = FastAPI()

# 資格リストのデータ
Passed = [
    {"ID": "FE00", "NAME": "基本情報技術者試験", "DATE": "2022/06/18"},
    {"ID": "OR00", "NAME": "Java SE Bronze", "DATE": "2023/02/20"}
]

@app.get("/list")
def get_passed_list(token:str):
    return Passed

@app.get("/{ID}")
def get_passed_item(ID:str,token:str):
    if ID == "FE00":
        return Passed[0]
    elif ID == "OR00":
        return Passed[1]
    else:
        return {}

@app.post("/add")
def add_passed_item(ID:str,DATE:str,token:str):
    return {"message": "Passed was added successfully", "Passed": {{"ID": "FE00", "DATE": "2022/06/18"},}}
