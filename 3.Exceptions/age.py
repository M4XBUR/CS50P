def main():
	age = get_old()
	print(f'You\'re {age} old')


def get_old():
	while True:	
		try:
			age = int(input('How old are u? '))
			return age
		except ValueError:
			print('Your age have to written in a number')


main()