def main():
    N = int(input())

    if N == int(int(N/1.08) * 1.08):
        print(int(N/1.08))
    elif N == int((int(N/1.08) - 1) * 1.08):
        print(int(N / 1.08) - 1)
    elif N == int((int(N/1.08) + 1) * 1.08):
        print(int(N / 1.08) + 1)
    else:
        print(":(")


if __name__ == '__main__':
    main()

