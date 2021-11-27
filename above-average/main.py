if __name__ == '__main__':
    nr_test_cases = int(input())

    for i in range(nr_test_cases):
        test_case = input().split()
        nr_grades = int(test_case[0])
        test_case_grades = list(map(int, test_case[1:]))
        test_case_average = sum(test_case_grades) / nr_grades
        nr_above_average = len(list(filter(lambda x: x > test_case_average, test_case_grades)))
        print('{:.3f}%'.format(100* nr_above_average / nr_grades))
