def main():
    N = int(input())
    int_list = list(map(int, input().split()))
    mod = 10 ** 9 + 7

    t = [0]*60

    for integer in int_list:
        for count, i in enumerate(reversed(format(integer, "b"))):
            if i == "1":
                t[count] += 1

    sum = 0
    for i, count in enumerate(t):
        sum += 2 ** i * count * (N - count)
    print(sum % mod)


if __name__ == '__main__':
    main()

