import bisect


def main():
    n = int(input())
    l = [int(i) for i in input().split()]

    l.sort()
    ans = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            ans += bisect.bisect_left(l, l[i] + l[j]) - j - 1

    print(ans)


if __name__ == '__main__':
    main()

