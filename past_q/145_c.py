import math


def main():
    N = int(input())
    xy_list = [list(map(int, input().split())) for i in range(N)]

    sum = 0

    for i, xy1 in enumerate(xy_list):
        for j, xy2 in enumerate(xy_list):
            if i == j:
                continue

            x1 = xy1[0]
            x2 = xy2[0]
            y1 = xy1[1]
            y2 = xy2[1]

            sum += math.sqrt((x1-x2)**2 + (y1-y2)**2)

    print(sum/N)


if __name__ == '__main__':
    main()

