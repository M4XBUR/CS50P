calories = {'apple': 130, 'banana': 110, 'avocado': 50}
input_item = input(f'Item: ').lower()

if input_item in calories:
	print(f'Calories: {calories[input_item]}')
