import requests

api_link = "https://api.hitbtc.com/api/3/public/price/rate?from={}&to={}"


def get_btc_to_bts(btc):
    curs = get_cur_btc_to_bts()
    return float(btc) * float(curs)


def get_cur_btc_to_bts():
    resp_json = requests.get(api_link.format("BTC", "BTS")).json()
    if len(resp_json) == 0:
        raise Exception("Empty answer")
    if resp_json.get("error") is not None:
        raise Exception("API error: " + resp_json.get("error").get("description"))
    return resp_json.get("BTC").get("price")
