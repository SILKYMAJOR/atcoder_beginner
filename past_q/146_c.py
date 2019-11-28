def main():
    A, B, X = map(int, input().split())

    left = 0
    right = 0

    for i in reversed(range(10)):
        if i == 0:
            print(0)
            exit()

        tmp_N = (A * (10 ** (i-1)) + B * (i-1))
        # print("tmp_N : {}".format(tmp_N))

        if X >= tmp_N :
            # print("X >= tmp_N : {} >= {}".format(X, tmp_N))
            # print("{} <= N < {}".format(10 ** (i-1), 10 ** i + 1))
            left = 10 ** (i-1)
            right = 10 ** i + 1
            break

    while True:
        center = (left + right) // 2
        if center in [left, right]:
            break

        tmp = A * center + B * len(str(center))
        # print("A : {}, B : {}, X : {}, L : {}, R : {}".format(A, B, X, left, right))
        if X == tmp:
            left = center
            break
        elif X > tmp:
            left = center
        elif X < tmp:
            right = center

    print(left)


if __name__ == '__main__':
    main()


