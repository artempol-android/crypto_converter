import requests

api_link = "https://api.hitbtc.com/api/3/public/price/rate?from={}&to={}"


def get_btc_to_bts(btc):
    curs = get_cur_btc_to_bts()
    print(curs)
    return float(btc) * float(curs)


def get_cur_btc_to_bts():
    resp_json = requests.get(api_link.format("BTC", "BTS"))
    print(resp_json.content)
    return resp_json.json().get("BTC").get("price")
