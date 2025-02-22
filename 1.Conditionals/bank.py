user_answer = input('Greeting: ')

if 'hello' in user_answer.lower():
	print('$0')
elif user_answer.lower()[0] == 'h':
	print('$20')
else:
	print('$100')