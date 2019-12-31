def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    count = 0
    for i in range(n):
        # print("-"*50)
        # print("A: {} A+1: {} B: {}".format(a_list[i], a_list[i+1], b_list[i]))
        if a_list[i] >= b_list[i]:
            a_list[i] -= b_list[i]
            count += b_list[i]
            b_list[i] = 0
        else:
            b_list[i] -= a_list[i]
            count += a_list[i]
            a_list[i] = 0

        # print("A: {} A+1: {} B: {}".format(a_list[i], a_list[i + 1], b_list[i]))

        if a_list[i+1] >= b_list[i]:
            a_list[i+1] -= b_list[i]
            count += b_list[i]
            b_list[i] = 0
        else:
            b_list[i] -= a_list[i+1]
            count += a_list[i+1]
            a_list[i+1] = 0

        # print("A: {} A+1: {} B: {}".format(a_list[i], a_list[i + 1], b_list[i]))

    print(count)


if __name__ == '__main__':
    main()

