def main():
    user_time = input('What times it? ')
    if 7 <= convert(user_time) <= 8:
        print('breakfast time')
    elif 12 <= convert(user_time) <= 13:
        print('lunch time')
    elif 18 <= convert(user_time) <= 19:
        print('dinner time')
    else:
        print('working bro')


def convert(time):
    hours, minutes = time.split(':')
    convert_time = int(hours) + (int(minutes) % 100) / 60
    return convert_time


if __name__ == "__main__":
    main()