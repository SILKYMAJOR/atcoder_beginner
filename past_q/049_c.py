def main():
    S = input()

    while True:
        if len(S) < 5:
            break

        if S[-5:] == "dream":
            S = S[:-5]
            continue
        elif S[-7:] == "dreamer":
            S = S[:-7]
            continue
        elif S[-5:] == "erase":
            S = S[:-5]
            continue
        elif S[-6:] == "eraser":
            S = S[:-6]
            continue
        else:
            break

    if len(S) == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()

