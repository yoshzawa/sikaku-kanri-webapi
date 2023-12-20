from fastapi import FastAPI
from sikaku import app as sikakuApp
from voucher import app as voucherApp
from account import app as accountApp

app = FastAPI()

# "/list"にsikaku.py、voucher.pyのアプリケーションをマウント
app.mount("/sikaku", sikakuApp)
app.mount("/voucher", voucherApp)
app.mount("/account", accountApp)
