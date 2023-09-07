import requests
coin_id = "bitcoin"
currency = "usd"
# current price of crypto currencies provided by COINGECKO.com
url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
data = requests.get(url).json()
coin_price = data[coin_id][currency]
print(f"The price of {coin_id} in {currency} is {coin_price:.2f} ")
