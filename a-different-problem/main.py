import sys

if __name__ == '__main__':
    cases = sys.stdin.read().strip()
    cases = cases.split('\n')
    for case in cases:
        nrs = list(map(int, case.split(' ', 1)))
        print('{:}'.format(abs(nrs[0] - nrs[1])))
