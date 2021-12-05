if __name__ == '__main__':
    X = int(input())

    nr_factors = 0
    factor = 2
    while factor*factor <= X:
        if X % factor == 0:
            X /= factor
            nr_factors += 1
            continue
        factor += 1
    nr_factors += 1
    print(nr_factors)

