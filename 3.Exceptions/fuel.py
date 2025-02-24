def main():
	fuel = get_fuel()
	print(fuel)


def get_fuel():
	while True:
		input_fuel = input('Fraction: ')
		try:
			x, y = input_fuel.split('/')
			if x > y:
				continue
			fuel = int(x) / int(y) * 100
		except (ValueError, ZeroDivisionError):
			pass
		else:
			if fuel >= 99:
				return 'F'
			elif fuel <= 0:
				return 'E'
			else:
				return f'{int(fuel)}%'


main()