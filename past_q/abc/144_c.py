def main():
    N = int(input())

    i = 1
    ans = 10 ** 18

    while i ** 2 <= N:
        if N % i == 0:
            j = N/i
            ans = min(ans, i+j-2)
        i += 1

    print(int(ans))


if __name__ == '__main__':
    main()

