def main():
    n = int(input())
    n_list = list(map(int, input().split()))

    previous = 0
    for i in range(n):
        if n_list[i] == previous + 1:
            previous += 1

    if previous == 0:
        print("-1")
    else:
        print(n - previous)


if __name__ == '__main__':
    main()

