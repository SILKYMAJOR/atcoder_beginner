def int_lines_to_list():
    retlist = []
    for _ in range(9):
        retlist.append(list(map(int, input().split())))
    return retlist


def main():
    array = int_lines_to_list()

    true_count = 0
    for i in range(9):
        for j in range(9):
            if array[i][j] == (i+1) * (j+1):
                true_count += 1
            else:
                array[i][j] = (i+1) * (j+1)

    # 二次元配列の書き出し
    for i in array:
        print(*i, sep=' ')

    print(true_count)
    print(81-true_count)


if __name__ == '__main__':
    main()

