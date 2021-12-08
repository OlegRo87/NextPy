# def city_generator():
#     print("Starting")
#     yield "London"
#     yield "Berlin"
#     yield "Amsterdam"
#
#
# def add_jerusalem_generator():
#     yield from city_generator()
#     yield "Jerusalem"
#
#
# patriot = add_jerusalem_generator()
# print(next(patriot))
# print(next(patriot))
# print(next(patriot))
# print(next(patriot))


def city_generator_2():
    print("Starting")
    yield "London"
    yield "Berlin"
    yield "Amsterdam"


city_loop_genx = city_generator_2()
for city in city_loop_genx:
    print(city)