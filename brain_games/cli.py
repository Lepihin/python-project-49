def welcome_user():
    import prompt

    name = prompt.string('May I have you name? ')
    print(f'Hello, {name}!')


if __name__ == '__main__':
    welcome_user()
