user_text = input('Input: ')

print('Output:', end='')
for i in user_text:
	if i.lower() in ('a', 'e', 'i', 'o', 'u'):
		continue
	else:
		print(i, end='')