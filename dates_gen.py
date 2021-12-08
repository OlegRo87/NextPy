import itertools


def gen_secs():
    return (x for x in range(60))


def gen_minutes():
    return (x for x in range(60))


def gen_hours():
    return (x for x in range(24))


def gen_time():
    secs_generator = gen_secs()
    mins_generator = gen_minutes()
    hours_generator = gen_hours()

    sec = next(secs_generator)
    min = next(mins_generator)
    hour = next(hours_generator)

    while True:
        yield '%s:%s:%s' % (str(hour).zfill(2), str(min).zfill(2), str(sec).zfill(2))
        try:
            sec = next(secs_generator)
        except:
            try:
                min = next(mins_generator)
            except:
                try:
                    hour = next(hours_generator)
                except:
                    break
                else:
                    mins_generator = gen_minutes()
                    min = next(mins_generator)
            finally:
                secs_generator = gen_secs()
                sec = next(secs_generator)


# for gt in gen_time():
#     print(gt)


def gen_years(start=2021):
    return itertools.count(start)


def gen_months():
    return (x for x in range(1, 13))


def gen_days(month, leap_year=True):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return (x for x in range(1, 32))
    elif month in [4, 6, 9, 11]:
        return (x for x in range(1, 31))
    elif month == 2:
        if leap_year:
            return (x for x in range(1, 30))
        else:
            return (x for x in range(1, 29))


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def gen_date():
    months_generator = gen_months()
    years_generator = gen_years()
    time_generator = gen_time()

    month = next(months_generator)
    year = next(years_generator)
    is_leap_year = is_leap(year)
    time = next(time_generator)

    days_generator = gen_days(month, is_leap_year)
    day = next(days_generator)

    while True:
        yield '%s/%s/%s %s' % (str(day).zfill(2), str(month).zfill(2), str(year), time)
        try:
            time = next(time_generator)
        except:
            try:
                day = next(days_generator)
            except:
                try:
                    month = next(months_generator)
                except:
                    year = next(years_generator)
                    is_leap_year = is_leap(year)
                    months_generator = gen_months()
                    month = next(months_generator)
                finally:
                    days_generator = gen_days(month, is_leap_year)
                    day = next(days_generator)
            finally:
                time_generator = gen_time()
                time = next(time_generator)


counter = 0
for gd in gen_date():
    if counter == 1000000:
        print(gd)
        counter = 0
    counter += 1