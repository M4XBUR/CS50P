import requests

try:
    response = requests.get('https://api.coincap.io/v2/assets/bitcoin')
    response_json = response.json()
    price_bitcoin = float(response_json['data']['priceUsd'])
except requests.RequestException as e:
    print('Ошибка:', e)
    exit()
except (KeyError, ValueError) as e:
    print(f'Ошибка обработки данных: {e}')
    exit()

while True:
	try:
		count_bitcoins = float(input('Введите количество биткойнов: '))
		break
	except ValueError:
		print('Вы должны написать число')
		exit()

total_cost = count_bitcoins * price_bitcoin
print(f'Цена за {count_bitcoins} биткойна: {total_cost:.2f}USD')
