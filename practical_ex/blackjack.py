from random import shuffle


def create_cart_desk():
    koloda = [6, 7, 8, 9, 2, 3, 4, 11] * 4
    shuffle(koloda)

    return koloda


def start_game():
    game_loop(create_cart_desk())


def game_loop(koloda):
    count = 0

    while True:
        choise = input('You have {0}. Will you take a card? y\\n '.format(count))

        if choise == 'y':
            current_card = koloda.pop()
            print('You have a dignity card {0}'.format(current_card))
            count += current_card

            if count > 21:
                print('Sorry, but you lost!((')
                break
            if count == 21:
                print('Congratulations, you won!!!!!')
                break
        elif choise == 'n':
            break

    print('You have a {0} points and you have finished the game'.format(count))


start_game()
