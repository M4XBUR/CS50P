shop_list = {}

while True:
	try:
		list_add = input().lower().strip()
		shop_list[list_add] += 1
	except KeyError:
		shop_list[list_add] = 1
	except EOFError:
		print('\n')
		shop_list_sorted = sorted(shop_list.items())
		for key, value in shop_list_sorted:
			print(f'{value}. {key.upper()}')
		break