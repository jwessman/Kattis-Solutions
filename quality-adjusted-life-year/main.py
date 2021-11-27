if __name__ == '__main__':
    nr_periods: int = int(input())
    total: float = 0
    for i in range(nr_periods):
        (quality, quantity) = input().split(" ", 1)
        total += float(quality) * float(quantity)

    print('{:.3f}'.format(total))
