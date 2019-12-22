def gcd(a, b):
    if a > b:
        a, b = (b, a)
    while b:
        a, b = b, a % b
    return a


def main():
    a, b = map(int, input().split())
    ans = round(a * b / gcd(a, b))
    print(ans)


if __name__ == '__main__':
    main()

