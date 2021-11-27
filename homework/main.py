if __name__ == '__main__':
    problem_ranges = input().split(";")
    tot_nr_problems: int = 0
    for i in range(len(problem_ranges)):
        p_range = problem_ranges[i]
        if '-' in p_range:
            (range_start, range_end) = p_range.split('-', 1)
            tot_nr_problems += int(range_end) - int(range_start) + 1
        else:
            tot_nr_problems += 1
    print('{:}'.format(tot_nr_problems))
