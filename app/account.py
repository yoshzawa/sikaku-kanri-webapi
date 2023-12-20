from fastapi import FastAPI

app = FastAPI()


@app.post("/login")
def get_product_item(userID:str,passcd:str):
    if userID == "User1":
        return {"Status":"OK","Token":"Kakyouin131"}
    else:
        return {"Status":"ERROR","message":"Invalid username or incorrect password"}

@app.post("/checkToken")
def get_product_item(userID:str,token:str):
    if token == "Kakyouin131":
        return {"Status":"OK"}
    else:
        return {"Status":"NG"}
