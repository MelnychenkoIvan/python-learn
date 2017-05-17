print('Enter stop for get the result')
summa = 0

while True:
    x = input('Enter a number: ')

    if x.lower() == 'stop':
        break

    if x == '':
        print("You don't put a number")
        continue

    if x[0] == '-':
        if not x[1:].isdigit():
            print('You should input a number not a string')
            continue
        else:
            summa += int(x)
    else:
        if not x.isdigit():
            print('You should input a number not a strint')
            continue
    summa += int(x)


print('The number sum = ', summa)
