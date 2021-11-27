import sys

if __name__ == '__main__':
    for line in sys.stdin:
        day_info = line.split()
        hour_start, min_start = list(map(int, day_info[3].split(':')))
        hour_end, min_end = list(map(int, day_info[4].split(':')))

        day_str = '{} {} {}'.format(day_info[0], day_info[1], day_info[2])
        if min_start > min_end:
            print('{} {} hours {} minutes'.format(day_str, hour_end - hour_start - 1,
                                                        60 - (min_start - min_end)))
        else:
            print('{} {} hours {} minutes'.format(day_str, hour_end - hour_start, min_end - min_start))
