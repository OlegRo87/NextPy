
def get_fibo():
	x = 0
	y = 1
	while True:
		yield x
		old_x = x
		x = y
		y = y + old_x


# fibo_gen = get_fibo()
# print(next(fibo_gen))
# print(next(fibo_gen))
# print(next(fibo_gen))
# print(next(fibo_gen))
# print('\n')

for x in get_fibo():
	if x > 100:
		break
	else:
		print(x)