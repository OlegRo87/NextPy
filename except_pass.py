
import re
from string import punctuation

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        problem = ''
        for i, char in enumerate(self._username):
            if not char.isalpha() and not char.isnumeric() and not char == '_':
                problem = ' problem: "' + char + '" in position ' + str(i)
                break
        return 'Username can include only english letters, numbers and _.' + problem

class UsernameTooShort(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return 'Username have to be 3 characters at least.'

class UsernameTooLong(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return 'Username have to be smaller than 16 characters.'

class PasswordMissingCharacter(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return 'Password have to include at least english letter, upper and lower, number and special character.'

class PasswordMissingUpper(PasswordMissingCharacter):
    def __init__(self):
        pass
    def __str__(self):
        return super().__str__() + '(missing uppercase)'

class PasswordMissingLower(PasswordMissingCharacter):
    def __init__(self):
        pass
    def __str__(self):
        return super().__str__() + '(missing lowercase)'

class PasswordMissingSpecial(PasswordMissingCharacter):
    def __init__(self):
        pass
    def __str__(self):
        return super().__str__() + '(missing special)'

class PasswordMissingNumber(PasswordMissingCharacter):
    def __init__(self):
        pass
    def __str__(self):
        return super().__str__() + '(missing number)'

class PasswordTooShort(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return 'Password must be larger than 8 characters.'

class PasswordTooLong(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return 'Password must be smaller than 40 characters.'


def check_input(username, password):
    if re.search('[^a-zA-Z_0-9]', username):
        raise UsernameContainsIllegalCharacter(username)
    elif len(username) < 3:
        raise UsernameTooShort
    elif len(username) > 16:
        raise UsernameTooLong
    elif not re.search('[a-z]', password):
        raise PasswordMissingLower
    elif not re.search('[A-Z]', password):
        raise PasswordMissingUpper
    elif not re.search('[0-9]', password):
        raise PasswordMissingNumber
    elif not len([x for x in punctuation if x in password]) > 0:
        raise PasswordMissingSpecial
    elif not (re.search('[a-z]', password) and re.search('[A-Z]', password) and re.search('[0-9]', password) and len
            ([x for x in punctuation if x in password]) > 0):
        raise PasswordMissingCharacter
    elif len(password) < 8:
        raise PasswordTooShort
    elif len(password) > 40:
        raise PasswordTooLong


# test
# check_input("1", "2")
# check_input("0123456789ABCDEFG", "2")
# check_input("A_a1.", "12345678")
# check_input("A_1", "2aA,")
# check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary8,")
# check_input("A_1", "abcdefghijklmnop")
# check_input("A_1", "ABCDEFGHIJLKMNOP")
# check_input("A_1", "ABCDEFGhijklmnop")
# check_input("A_1", "4BCD3F6h1jk1mn0p")
# check_input("A_1", "4BCD3F6.1jk1mn0p")


def main():
    while True:
        username = input('Enter username: ')
        try:
            check_input(username, "4BCD3F6.1jk1mn0p")
        except UsernameContainsIllegalCharacter:
            print(UsernameContainsIllegalCharacter(username))
        except UsernameTooShort:
            print(UsernameTooShort())
        except UsernameTooLong:
            print(UsernameTooLong())
        else:
            break

    while True:
        password = input('Enter password: ')
        try:
            check_input(username, password)
        except PasswordMissingUpper:
            print(PasswordMissingUpper())
        except PasswordMissingLower:
            print(PasswordMissingLower())
        except PasswordMissingNumber:
            print(PasswordMissingNumber())
        except PasswordMissingSpecial:
            print(PasswordMissingSpecial())
        except PasswordMissingCharacter:
            print(PasswordMissingCharacter())
        except PasswordTooShort:
            print(PasswordTooShort())
        except PasswordTooLong:
            print(PasswordTooLong())
        else:
            print('OK')
            break

main()
