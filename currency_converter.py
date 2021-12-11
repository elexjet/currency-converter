import requests
import json

if __name__ == "__main__":
    currency_in = str(input()).lower()
    response = requests.get(f'http://www.floatrates.com/daily/{currency_in}.json')
    currency_rates = json.loads(response.text)  # Creates a python dictionary of the input currency from the retrieved JSON file
    cache = {}

    if 'usd' in currency_rates.keys():
        cache['usd'] = currency_rates['usd']

    if 'eur' in currency_rates.keys():
        cache['eur'] = currency_rates['eur']

    while True:
        currency_out = str(input()).lower()

        if currency_out == "" or currency_in == "":
            break

        cash_owned = int(input())
        print(f'Checking the cache...')
        
        if currency_out in cache.keys():
            exchange_rate = cache[currency_out]['rate']
            amount = exchange_rate * cash_owned
            print('Oh! It is in the cache!')
        elif currency_out not in cache.keys():
            print('Sorry, but it is not in the cache!')
            cache[currency_out] = currency_rates[currency_out]
            exchange_rate = cache[currency_out]['rate']
            amount = exchange_rate * cash_owned

        print(f'You received {amount:.2f} {currency_out.upper()}')