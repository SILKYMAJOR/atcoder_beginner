def main():
    N = int(input())
    S = input()

    count = 0

    for i in range(10):
        a = S.find(str(i))
        if a == -1:
            continue

        for j in range(10):
            b = S[a+1:].find(str(j))
            if b == -1:
                continue

            for k in range(10):
                if str(k) in S[a+b+2:]:
                    # print(i*100+j*10+k)
                    count += 1

    print(count)


if __name__ == '__main__':
    main()

