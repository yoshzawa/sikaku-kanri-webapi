from fastapi import FastAPI
from sikaku import app as sikakuApp

app = FastAPI()

# "/list"にmain1.pyのアプリケーションをマウント
app.mount("/sikaku", sikakuApp)
