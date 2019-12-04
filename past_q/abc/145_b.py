def main():
    N = int(input())
    S = input()
    flag = True

    if N % 2 == 1:
        print("No")
        exit()
    
    for i in range(int(N/2)):
        if S[i] == S[i + int(N/2)]:
            continue
        flag = False

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

