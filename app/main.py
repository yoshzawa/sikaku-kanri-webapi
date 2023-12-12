from fastapi import FastAPI
from main1 import app as app1

app = FastAPI()

# "/list"にmain1.pyのアプリケーションをマウント
app.mount("/list", app1)
