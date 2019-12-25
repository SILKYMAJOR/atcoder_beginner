def main():
    n = int(input())
    h_list = list(map(int, input().split()))

    for i in range(n-1):
        if h_list[i] < h_list[i+1]:
            h_list[i+1] -= 1

        elif h_list[i] > h_list[i+1]:
            print("No")
            exit()

    print("Yes")


if __name__ == '__main__':
    main()

