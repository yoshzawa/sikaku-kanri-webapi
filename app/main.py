from fastapi import FastAPI
from sikaku import app as sikakuApp
from voucher import app as voucherApp

app = FastAPI()

# "/list"にmain1.pyのアプリケーションをマウント
app.mount("/sikaku", sikakuApp)
app.mount("/voucher", voucherApp)
