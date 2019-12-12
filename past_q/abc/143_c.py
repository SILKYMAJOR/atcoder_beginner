def main():
    N = int(input())
    S = input()

    merged = []
    previous = ""
    for i in S:
        if i != previous:
            merged.append(i)
        previous = i

    print(len(merged))


if __name__ == '__main__':
    main()

