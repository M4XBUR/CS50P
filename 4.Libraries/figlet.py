import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
	print(figlet.setFont(font = choice(fonts)))
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fonts:
	print(figlet.setFont(font = sys.argv[2]))
else:
	sys.exit('Invalid usage')

user_text = input('Input: ')
print(f'Output:\n{figlet.renderText(user_text)}')