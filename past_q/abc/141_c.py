def main():
    n, k, q = map(int, input().split())

    answer_dict = {}

    for _ in range(q):
        a = int(input())
        if a in answer_dict:
            answer_dict[a] += 1
        else:
            answer_dict[a] = 1

    for i in range(n):
        if i+1 in answer_dict:
            if k - q + answer_dict[i+1] > 0:
                print("Yes")
                continue
        else:
            if k - q > 0:
                print("Yes")
                continue

        print("No")


if __name__ == '__main__':
    main()

