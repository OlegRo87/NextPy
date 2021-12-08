# def intersection(list_1, list_2):
#     nlist = list(set([i for i in list_1 if i in list_2]))
#     return nlist
#
#
# print(intersection([1, 2, 3, 4], [8, 3, 9]))
# print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
#
#
# def is_prime(number):
#     return all([(number % divider) for divider in range(2, int(number ** 0.5) + 1)]) and number > 1
#
#
# print(is_prime(42))
# print(is_prime(43))
#
#
# def is_funny(string):
#     return False not in (False if "h" != char and "a" != char else True for char in string)
#
#
# print(is_funny("hahahahahaha"))


# import string
#
# text = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
# shift = 2
# alphabet = string.ascii_lowercase
# shifted = alphabet[shift:] + alphabet[:shift]
# table = str.maketrans(alphabet, shifted)
# encrypted = text.translate(table)
# print(encrypted)
