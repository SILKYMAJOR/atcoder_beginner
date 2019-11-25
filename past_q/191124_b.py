def main():
    N = int(input())
    S = input()
    s = []

    for x in S:
        if (ord(x) + N) > 90:
            s.append(chr(ord(x) + N - 26))
        else:
            s.append(chr(ord(x) + N))

    print(*s, sep='')


if __name__ == '__main__':
    main()

