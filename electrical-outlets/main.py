if __name__ == '__main__':
    nr_test: int = int(input())

    for i in range(nr_test):
        test_nrs = list(map(int, input().split()))
        print('{:}'.format(sum(test_nrs[1:]) - (test_nrs[0] - 1)))
