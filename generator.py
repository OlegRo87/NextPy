# Do try this at home.
# prime_generator = (n for n in range(10 ** 10) if is_prime(n))
# for prime_number in prime_generator:
#     print(prime_number)


# gen = (i / 2 for i in [0, 9, 21, 32])
# print(next(gen))
# print(next(gen))


# def translate(sentence):
#     words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
#     split = sentence.split(' ')
#     gen = (word for word in split)
#     translated = ''
#     for word in gen:
#         translated += words[word] + ' '
#     return translated
#
#
# print(translate("el gato esta en la casa"))


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    num_generator = (num for num in range(n+1, 2 * n + 1))
    for num in num_generator:
        if is_prime(num):
            return num


print(first_prime_over(2))
