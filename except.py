try:
    num_1 = int(input("first number: "))
    num_2 = int(input("second number: "))
    print("the result is: " + str(num_1 // num_2))
except ZeroDivisionError as e:
    print('dev by zero')
    print(e)
except ValueError as e:
    print('invalid input, only int')
    print(e)
else:
    print("tadadm")
finally:
    print("no meter what")
