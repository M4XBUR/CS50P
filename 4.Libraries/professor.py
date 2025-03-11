from random import randint

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        try:
            user_answer = int(input(f'{x} + {y} = '))
        except ValueError:
            print('EEE')
            continue
        if user_answer == correct_answer:
            score += 1
        else:
            print('EEE')
    print(f'Score: {score}')


def get_level():
    while True:
        level = input('Level: ')
        if level in ['1', '2', '3']:
            return level


def generate_integer(level):
    if level == '1':
        return randint(0,9)
    elif level == '2':
        return randint(10,99)
    elif level == '3':
        return randint(100,999)  


if __name__ == "__main__":
    main()