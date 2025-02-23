def main():
	camelCase = input('camelCase: ')
	print(f'shake_case: ', end='')
	convert(camelCase)


def convert(text):
	for i in text:
		if i.isupper():
			print(f'_{i.lower()}', end='')
		else:
			print(i, end='')

main()