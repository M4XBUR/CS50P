def main():
	age = get_old()
	print(f'You\'re {age} old')


def get_old():
	while True:	
		try:
			age = int(input('How old are u? '))
		except ValueError:
			print('Your age have to written in a number')
		else:
			break
	return age


main()