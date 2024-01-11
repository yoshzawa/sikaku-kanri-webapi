from fastapi import FastAPI

app = FastAPI()

# 資格リストのデータ
Exams = [
    {"ID": "FE00", "NAME": "基本情報技術者試験"},
    {"ID": "OR00", "NAME": "Java SE Bronze"}
]

@app.get("/list")
def get_exam_list(token:str):
    return Exams

@app.get("/{ID}")
def get_exam_item(ID:str,token:str):
    if ID == "FE00":
        return Exams[0]
    elif ID == "OR00":
        return Exams[1]
    else:
        return {}

@app.post("/add")
def add_exam_item(ID:str,NAME:str,token:str):
    return {"message": "Exam added successfully", "exam": {"ID": "FE00", "NAME": "基本情報技術者試験"}}
    