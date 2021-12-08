from functools import reduce


def check_id_valid(id_number):
    num_list = [(id_number % 10 ** i) // 10 ** (i - 1) for i in range(9, 0, -1)]
    odd = num_list[::2]
    even = num_list[1::2]
    multiple_even = list(map(lambda x: 2 * x, even))
    fixed_even = [x // 10 + x % 10 if x > 9 else x for x in multiple_even]
    sum = reduce(lambda x, y: x + y, fixed_even) + reduce(lambda x, y: x + y, odd)
    if sum % 10 == 0:
        return True
    else:
        return False


class IDIterator():
    def __init__(self, id=100000000):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        self._id += 1
        while not check_id_valid(self._id):
            self._id += 1

        if self._id >= 999999999:
            raise StopIteration('your ID has 10 digits')
        return self._id


def id_generator(id_number):
    id = id_number
    while id < 999999999:
        id += 1
        while not check_id_valid(id):
            id += 1
        yield id


def main():
    user_id = int(input('Enter ID: '))
    choose = input('Generator or Iterator? (gen/it)? ')
    if choose == 'it':
        iterable_id = IDIterator(user_id)
    elif choose == 'gen':
        iterable_id = id_generator(user_id)
    else:
        raise Exception('Wrong Input!')

    for i in range(10):
        print(next(iterable_id))


if __name__ == "__main__":
    main()



