def combine_coins(coin, numbers):
    output = ""
    for num in numbers:
        output += coin + str(num) + ', '
    # Ignore the last comma.
    return output[:-2]


print(combine_coins('$', range(5)))


def combine_coins_2(coin, numbers):
    return ', '.join([coin + str(i) for i in numbers])


print(combine_coins('$', range(5)))
