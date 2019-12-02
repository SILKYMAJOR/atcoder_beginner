def main():
    X = int(input())

    X_div_100 = X // 100
    res_X_div_100 = X % 100

    count = 0

    while True:
        if res_X_div_100 >= 5:
            res_X_div_100 -= 5
            count += 1
        elif res_X_div_100 >= 4:
            res_X_div_100 -= 4
            count += 1
        elif res_X_div_100 >= 3:
            res_X_div_100 -= 3
            count += 1
        elif res_X_div_100 >= 2:
            res_X_div_100 -= 2
            count += 1
        elif res_X_div_100 >= 1:
            res_X_div_100 -= 1
            count += 1
        else:
            break

    if count <= X_div_100:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()

