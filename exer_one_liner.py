def add(letter):
    ds = letter + letter
    return ds


def double_letter(my_str):
    result = map(add, my_str)
    return "".join(list(result))


print(double_letter("python"))
print(double_letter("we are the champions!"))


def dvbyfour(num):
    return num % 4 == 0


def four_dividers(number):
    result = filter(dvbyfour, range(1, number))
    return list(result)


print(four_dividers(9))
print(four_dividers(3))


def sum_of_digits(number):
    return sum(map(int, str(number)))


print(sum_of_digits(104))
