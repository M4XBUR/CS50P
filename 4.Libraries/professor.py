from random import randint

def main():
    generate_integer(get_level())


def get_level():
    while True:
        input_level = input('Level: ')
        if input_level in ['1', '2', '3']:
            return input_level
        else:
            continue


def generate_integer(level):
    count_game = 0
    while count_game <= 10:
        if level == '1':
            x = randint(0,9)
            y = randint(0,9)
        elif level == '2':
            x = randint(10,99)
            y = randint(10,99)
        elif level == '3':
            x = randint(100,999)
            y = randint(100,999)
        
        score = 0
        try:
            print(f'{x} + {y} = ', end='')
            user_answer = int(input(''))
        except ValueError:
            print('EEE')
            continue
        if user_answer == x + y:
            score += 1
            count_game += 1
        else:
            print('EEE')
            count_game += 1
            continue
    print(f'Score: {score}')


if __name__ == "__main__":
    main()