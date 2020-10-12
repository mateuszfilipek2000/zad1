import requests

# currency exchange
base_currency = input("Wprowadz skrot waluty bazowej ").upper()
target_currency = input("Wprowadz skrot waluty docelowej ").upper()
# base_currency, target_currency = "USD", "PLN"
exchange_rate = requests.get("https://api.exchangeratesapi.io/latest?base={}&symbols={}".format(base_currency, target_currency))

# print(exchange_rate.json()["rates"])
try: 
    for key, val in exchange_rate.json()["rates"].items():
        # print(key, val)
        print("1 {} - {} {}".format(base_currency, val, key))
except KeyError:
    print("invalid input")
