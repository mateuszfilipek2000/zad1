import requests
import json

'''
{
  "base": "EUR",
  "date": "2018-04-08",
  "rates": {
    "CAD": 1.565,
    "CHF": 1.1798,
    "GBP": 0.87295,
    "SEK": 10.2983,
    "EUR": 1.092,
    "USD": 1.2234,
    ...
  }
}
'''

# currency exchange
base_currency = input("Wprowadz skrot waluty bazowej: ").upper()
target_currency = input("Wprowadz skrot waluty docelowej: ").upper()
# base_currency, target_currency = "USD", "PLN"
exchange_rate = requests.get("https://api.exchangeratesapi.io/latest?base={}&symbols={}".format(base_currency, target_currency))
# print(json.dumps(exchange_rate.json(), sort_keys=True))
# print(exchange_rate.json()["rates"])
try: 
    for key, val in exchange_rate.json()["rates"].items():
        # print(key, val)
        print("1 {} - {} {}".format(base_currency, val, key))
except KeyError:
    print("invalid input")
