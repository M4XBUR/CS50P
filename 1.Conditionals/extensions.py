user_text = input('File name: ')

if '.gif' in user_text:
	print('image/gif')
elif '.jpg' in user_text:
	print('image/jpeg')
elif '.jpeg' in user_text:
	print('image/jpeg')
elif '.png' in user_text:
	print('image/png')
elif '.pdf' in user_text:
	print('application/pdf')
elif '.txt' in user_text:
	print('text/plain')
elif '.zip' in user_text:
	print('application/zip')
else:
	print('application/octet-stream')