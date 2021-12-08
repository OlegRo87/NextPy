import itertools
integers = (i for i in range(1, 11))
squared = (x * x for x in integers)
negated = (-y for y in squared)
for num in negated:
    print(num)

with open("capitals.txt") as file:
    single_line_gen = (line for line in file)
    capitals_and_cities = (l.replace("\n", ("")).split(",") for l in single_line_gen)
    capitals_dict = dict(capitals_and_cities)
    print(capitals_dict)


def parse_ranges(ranges_string):
    ranges_string = ranges_string.replace(' ', '')
    first_generator = (x.split('-') for x in ranges_string.split(','))
    second_generator = ([k for k in range(int(x), int(y) + 1)] for x, y in first_generator)
    third_generator = itertools.chain.from_iterable(second_generator)
    return third_generator

print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))