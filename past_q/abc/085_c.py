def main():
    N, Y = map(int, input().split())

    en_10000 = 10000
    en_5000 = 5000
    en_1000 = 1000

    if en_10000 * N < Y:
        print("-1 -1 -1")
        exit()
    elif en_1000 * N > Y:
        print("-1 -1 -1")
        exit()

    for x in range(N + 1):
        if en_10000 * x > Y:
            continue
        for y in range(N - x + 1):
            z = N - x - y
            if en_10000 * x + en_5000 * y + en_1000 * z == Y:
                print("{} {} {}".format(x, y, z))
                exit()

    print("-1 -1 -1")


if __name__ == '__main__':
    main()

