from fastapi import FastAPI
from account import app as accountApp
from exam import app as examApp
from sikaku import app as sikakuApp
from voucher import app as voucherApp
from voucherType import app as voucherTypeApp

app = FastAPI()

# "/list"にsikaku.py、voucher.pyのアプリケーションをマウント
app.mount("/account", accountApp)
app.mount("/exam", examApp)
app.mount("/sikaku", sikakuApp)
app.mount("/voucher", voucherApp)
app.mount("/voucherType", voucherTypeApp)
