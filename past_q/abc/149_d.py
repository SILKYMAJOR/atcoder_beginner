def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = list(input())

    score = 0
    for i in range(n):
        if i - k >= 0:
            if t[i] == t[i-k]:
                t[i] = "x"
                continue

        if t[i] == "r":
            score += p
        elif t[i] == "s":
            score += r
        elif t[i] == "p":
            score += s

    print(score)


if __name__ == '__main__':
    main()

