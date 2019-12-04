def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    en_500 = 500
    en_100 = 100
    en_50 = 50

    count = 0

    for i_500 in range(A+1):
        for i_100 in range(B+1):
            for i_50 in range(C+1):
                if en_500 * i_500 + en_100 * i_100 + en_50 * i_50 == X:
                    count += 1

    print(count)


if __name__ == '__main__':
    main()

