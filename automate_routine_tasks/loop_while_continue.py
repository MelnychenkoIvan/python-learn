while True:
    print('Who are you?')
    name = input()

    if name != 'Go':
        continue

    print('Hello Go. What is your password?')
    password = input()

    if password == 'qwerty123':
        break

print('Access granted')