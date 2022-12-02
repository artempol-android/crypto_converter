from flask import Flask, request

from api import get_btc_to_bts, get_bts_to_btc, get_cur

app = Flask(__name__)

btc_possible = ["btc", "BTC", "Btc", "bitcoin", "Bitcoin", "BITCOIN"]
bts_possible = ["bts", "BTS", "Bts", "BitShares", "bitshares", "BITSHARES"]


@app.route("/convert")
def convert():
    try:
        for str_btc in btc_possible:
            btc = request.args.get(str_btc)
            if btc is not None:
                btc = btc.replace(',', '.')
                return "{} BTC = {} BTS".format(btc, get_btc_to_bts(btc))
        for str_bts in bts_possible:
            bts = request.args.get(str_bts)
            if bts is not None:
                bts = bts.replace(',', '.')
                return "{} BTS = {} BTC".format(bts, get_bts_to_btc(bts))
    except Exception as e:
        return str(e)


@app.route("/rate")
def exchange_rate():
    try:
        return "<p>1 BTC = {} BTS</p><p>1 BTS = {} BTC</p>".format(get_cur("BTC", "BTS"), get_cur("BTS", "BTC"))
    except Exception as e:
        return str(e)
