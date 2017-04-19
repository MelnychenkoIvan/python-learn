import random
import time

alphabet = 'abcdefghijklmnopqrstuvwxyz .!'


def score(goal, current):
    return goal == current


def generator_rand_str(str_len, alphabet):
    result = ''

    for k in range(str_len):
        rand = random.randrange(len(alphabet))
        result = result + alphabet[rand]

    return result


def some(goal_str, current_str, prev_str):
    result_str = ''

    for i in range(len(current_str)):
        if prev_str[i] == goal_str[i]:
            result_str = result_str + prev_str[i]
        elif current_str[i] == goal_str[i]:
            result_str = result_str + current_str[i]
        else:
            result_str = result_str + current_str[i]

    return result_str


def generator_str(input_str, alphabet):
    start = time.time()

    random_str = generator_rand_str(len(input_str), alphabet)
    counter = 1
    while not score(input_str, random_str):
        random_str = some(input_str, generator_rand_str(len(input_str), alphabet), random_str)
        counter = counter + 1
        print(random_str)

    end = time.time()
    return counter, end - start

print('Attempt %d require %f seconds' % generator_str('some string', alphabet))