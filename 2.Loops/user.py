def main():
    user = {
            'name': user_name(),
            'age': user_age()
            }
    print(create_report(user))


def create_report(user):
    return f"""
    ========= USER =========
    Name: {user.get('name', 'Unknown')}
    Age: {user.get('age', 'Unknown')}
    Height: {user.get('height', 'Unknown')}
    ========================
    """


def user_name():
    name = input('Enter the user\'s name: ')
    return name


def user_age():
    age = input('Enter the user\'s age: ')
    return age


if __name__ == '__main__':
    main()