def main():
    N = int(input())
    v_list = list(map(int, input().split()))
    v_sorted_list = sorted(v_list)
    value = v_sorted_list[0]
    for v in sorted(v_list):
        value = (value + v) / 2

    print(value)


if __name__ == '__main__':
    main()

