my_money_list = [x ** 2 for x in range(100)]
print(my_money_list)

print('**************')

list_1 = [1, 2, 3]
list_2 = [5, 6, 7]
mult_list = [x * y for x in list_1 for y in list_2]
print(mult_list)

print('***************************')

nested_list = [x * 2 for x in range(10) if x > 3 if x < 7]
print(nested_list)

print('***************************')

sentence = "the quick brown fox"
words = sentence.split()
secret = [word[0] for word in words if word != "the"]
print(secret)
