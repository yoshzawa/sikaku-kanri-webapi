from fastapi import FastAPI

app = FastAPI()


@app.post("/login")
def get_product_item(username:str,password:str):
    print(f"Login username:{username},password:{password}")  # ログにURLを出力

    if username == "User1":
        return {"Status":"OK","Token":"Kakyouin131"}
    else:
        return {"Status":"ERROR","message":"Invalid username or incorrect password"}

@app.post("/checkToken")
def get_product_item(username:str,token:str):
    if token == "Kakyouin131":
        return {"Status":"OK"}
    else:
        return {"Status":"NG"}
