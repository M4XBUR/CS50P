def main():
	camelCase = input('camelCase: ')
	print('shake_case: ', end='')
	convert(camelCase)


def convert(text):
	for i in text:
		if i.isupper():
			print(i.lower(), end='')
		else:
			print(i, end='')

main()