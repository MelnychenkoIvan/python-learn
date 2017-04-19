def find_min1(number_list):
    min_value = number_list[0]

    for k in number_list:
        for n in number_list:
            if k < n and k < min_value:
                min_value = k

    return min_value


def find_min2(number_list):
    min_value = number_list[0]

    for k in number_list:
        if k < min_value:
            min_value = k

    return min_value

print(find_min1([2, 20, -3, 12, 4, 23, 1, 34, - 1, 5]))
print(find_min2([2, 20, -3, 12, 4, 23, 1, 34, - 1, 5]))
