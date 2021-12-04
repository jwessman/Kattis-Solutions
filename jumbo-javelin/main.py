if __name__ == '__main__':
    nr_rods = int(input())
    total_length = sum([int(input()) for i in range(nr_rods)])
    total_length = total_length - (nr_rods - 1)
    print(total_length)
