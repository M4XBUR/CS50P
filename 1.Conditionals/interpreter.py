user_text = input('Expression: ')
x, z, y = user_text.split(' ')

if z == '+':
	print(f'result: {float(x) + float(y)}')
elif z == '-':
	print(f'result: {float(x) - float(y)}')
elif z == '*':
	print(f'result: {float(x) * float(y)}')
elif z == '/':
	if y == '0':
		print('dont do it plz!')
	else:
		print(f'result: {float(x) / float(y)}')