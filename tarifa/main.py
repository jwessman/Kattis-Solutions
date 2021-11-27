if __name__ == '__main__':
    mb_per_month: int = int(input())
    nr_of_months: int = int(input())

    left_over_data = mb_per_month
    for i in range(nr_of_months):
        used_data: int = int(input())
        left_over_data += mb_per_month - used_data
    print(left_over_data)
