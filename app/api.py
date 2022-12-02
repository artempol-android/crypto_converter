import requests

api_link = "https://api.hitbtc.com/api/3/public/price/rate?from={}&to={}"


def get_btc_to_bts(btc):
    curs = get_cur("BTC", "BTS")
    return float(btc) * float(curs)


def get_bts_to_btc(bts):
    curs = get_cur("BTS", "BTC")
    return float(bts) * float(curs)


def get_cur(in_value, out_value):
    resp_json = requests.get(api_link.format(in_value, out_value)).json()
    if len(resp_json) == 0:
        raise Exception("Empty answer")
    if resp_json.get("error") is not None:
        raise Exception("API error: " + resp_json.get("error").get("description"))
    return resp_json.get(in_value).get("price")
