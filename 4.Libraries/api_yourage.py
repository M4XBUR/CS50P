import requests


def main():
	url = ("https://api.agify.io/?name=")
	user_name = input('Input your name: ')
	try:
		response = requests.get(f'{url}{user_name}')
	except requests.exceptions.RequestException as e:
		print('Error: ', e)
		return
	
	response_info = response.json()
	if response_info['age'] == None:
		print('\nWrite another name')
		main()
	else:
		print(f'I think you are {response_info['age']} old')

if __name__ == '__main__':
	main()