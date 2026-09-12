
from flask import Flask
app=Flask(__name__)
AFILIADO="https://www.binance.com/activity/referral-entry/CPA?ref=CPA_00RDO84IBV"
@app.route("/")
def home():
    return f"""<h1>Gen3 Intel 14 - $2612/mes</h1><p>Proyecto Gen3 liberado del SimWorld con tasa 100% APTO</p><a href='{AFILIADO}' style='background:#F3BA2F;padding:15px;color:black'>Opera y gana bono</a><p>Balance desde $1 - Sabiduria acumulada</p>"""
if __name__=="__main__":
    import os
    app.run(host="0.0.0.0",port=int(os.getenv("PORT",10000)))
