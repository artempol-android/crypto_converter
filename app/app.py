from flask import Flask, request

from api import get_btc_to_bts

app = Flask(__name__)


@app.route("/convert")
def convert():
    try:
        btc = request.args.get("btc")
        if btc is not None:
            return "{} BTC = {} BTS".format(btc, get_btc_to_bts(btc))
    except Exception as e:
        return str(e)
