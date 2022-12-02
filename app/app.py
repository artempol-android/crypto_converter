from flask import Flask, request

from api import get_btc_to_bts, get_bts_to_btc

app = Flask(__name__)


@app.route("/convert")
def convert():
    try:
        btc = request.args.get("btc")
        if btc is not None:
            return "{} BTC = {} BTS".format(btc, get_btc_to_bts(btc))
        else:
            bts = request.args.get("bts")
            if bts is not None:
                return "{} BTS = {} BTC".format(bts, get_bts_to_btc(bts))
    except Exception as e:
        return str(e)
