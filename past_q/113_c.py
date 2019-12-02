# TLE 

import sys
from operator import itemgetter


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    p_y = [list(map(int, input().split())) for _ in range(m)]

    sorted_p_y = sorted(p_y, key=itemgetter(0, 1))

    for row in p_y:
        count = 0
        for sorted_row in sorted_p_y:
            if row[0] == sorted_row[0]:
                count += 1

            if row[0] == sorted_row[0] and row[1] == sorted_row[1]:
                print(str(row[0]).zfill(6), str(count).zfill(6), sep="")
                break


if __name__ == '__main__':
    main()

