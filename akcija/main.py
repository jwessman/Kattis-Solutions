import sys

if __name__ == '__main__':
    nr_books = int(input())
    prices = list(map(int, sys.stdin.read().strip().split('\n')))
    prices.sort()
    nr_left_overs = nr_books % 3
    total = sum(prices[:nr_left_overs])

    i = len(prices) - 1
    while i > nr_left_overs:
        total += prices[i]
        total += prices[i - 1]
        i -= 3
    print(total)
