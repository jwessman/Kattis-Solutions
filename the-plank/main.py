def get_subset_sum(target):
    subset_sums = [0] * (target + 1)
    subset_sums[0] = 1

    for i in range(1, target + 1):
        for j in [1, 2, 3]:
            if i >= j:
                subset_sums[i] += subset_sums[i - j]

    return subset_sums[target]


if __name__ == '__main__':
    desired_length = int(input())
    print('{:}'.format(get_subset_sum(desired_length)))
