
from itertools import combinations

shtarot = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
my_set = set()
for num in range(7, len(shtarot)):
    for comb in combinations(shtarot, num):
        if sum(comb) == 100:
            my_set.add(comb)

print(len(my_set))
