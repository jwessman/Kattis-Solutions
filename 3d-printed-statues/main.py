def nr_days(nr_statues):
    printed = 1
    days = 0

    while printed < nr_statues:
        printed *= 2
        days += 1

    days += 1

    return days


if __name__ == '__main__':
    nr_statues = int(input())
    print('{:}'.format(nr_days(nr_statues)))
