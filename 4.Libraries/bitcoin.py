import requests

try:
    response = requests.get('https://api.coincap.io/v2/assets/bitcoin')
    response_json = response.json()
    price_bitcoin = float(response_json['data']['priceUsd'])
except requests.RequestException as e:
    print('Ошибка соединения:', e)
    exit()
except (KeyError, ValueError) as e:
    print(f'Ошибка обработки данных: {e}')
    exit()

while True:
	try:
		count_bitcoins = float(input('write count bitcoins: '))
		break
	except ValueError:
		print('U must write number')
		exit()

total_cost = count_bitcoins * price_bitcoin
print(f'Cost for {count_bitcoins} bitcoins: {total_cost:.2f}USD')
