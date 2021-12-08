#
# import winsound
#
# freqs = {"la": 220,
#          "si": 247,
#          "do": 261,
#          "re": 293,
#          "mi": 329,
#          "fa": 349,
#          "sol": 392,
#          }
#
# notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
# tavim = notes.split('-')
# iterator = iter(tavim)
#
# for tav in iterator:
#     tav_list = tav.split(',')
#     print(freqs[tav_list[0]])
# winsound.Beep(freqs[tav_list[0]], tav_list[1])\


# x = iter([1, 2, 3, 4, 5])
# next(x)
# next(x)
# for i in x:
#     print(i)


numbers = iter(list(range(1, 101)))
next(numbers)
next(numbers)
for i in numbers:
    print(i)
    try:
        next(numbers)
        next(numbers)
    except:
        pass
