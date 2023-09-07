# SQLAlch-currencies-3
Recreate python SQLAlch CLI app replacing .db files with .sqlite files

SQLAlch-Currencies-2 is a Python CLI app that manages crypto currency investments submitted for a bootcamp assignment.

The crypto currency date and rate data is provided with an api from CoinGecko https://www.coingecko.com/ 

This app is a modification of the Douglas Starnes Pluralsight  tutorial  https://www.pluralsight.com/ covering the use of  SQLalchemy with a variety of databases 

----------

Create a venv (this step is only necessary w/ init app install). 
$ python -m venv 
$ python -m venv venv

Activate the venv
$ source venv/bin/activate

Check version of SQLite
(venv) $ sqlite3
SQLite version 3.19.3...

create/open text.sqlite file
sqlite> .open test.sqlite

Install requests package
python -m pip install requests

Create get_price.py to test coingecko api
<!--
import requests
coin_id = "bitcoin"
currency = "usd"
# current price of crypto currencies provided by COINGECKO.com
url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
data = requests.get(url).json()
coin_price = data[coin_id][currency]
print(f"The price of {coin_id} in {currency} is {coin_price:.2f} ")
-->

(venv) $ python get_price.py

Create main.py from get_price.py code
install/import click package
python -m pip install click

add click decorators for 
def get_coin_price(coin_id, currency)
