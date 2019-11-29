def main():
    _ = int(input())
    A_list = list(map(int, input().split()))

    max_count = 10**9 / 2
    for A in A_list:
        count = 0
        while True:
            if max_count == count:
                break
            elif A % 2 == 1:
                break
            else:
                A = A / 2
                count += 1
        if max_count > count:
            max_count = count

    print(max_count)


if __name__ == '__main__':
    main()

