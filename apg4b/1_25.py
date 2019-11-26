def intersection(a, b):
    print(*(a & b), sep=' ')


def union_set(a, b):
    print(*(a | b), sep=' ')


def symmetric_diff(a, b):
    print(*(a ^ b), sep=' ')


def subtract(a, sub):
    a.remove(sub)
    print(*a, sep=' ')


def increment(a):
    tmp = []
    for x in a:
        if x == 49:
            tmp.append(0)
        else:
            tmp.append(x+1)
    print(*sorted(tmp), sep=' ')


def decrement(a):
    tmp = []
    for x in a:
        if x == 0:
            tmp.append(49)
        else:
            tmp.append(x-1)
    print(*sorted(tmp), sep=' ')


def main():
    _ = input()
    n_set = set(map(int, input().split()))
    _ = input()
    m_set = set(map(int, input().split()))
    type_str = input()

    if type_str == "intersection": intersection(n_set, m_set)
    elif type_str == "union_set": union_set(n_set, m_set)
    elif type_str == "symmetric_diff": symmetric_diff(n_set, m_set)
    elif type_str == "increment": increment(n_set)
    elif type_str == "decrement": decrement(n_set)
    else:
        subtract(n_set, int(type_str.split()[1]))


if __name__ == '__main__':
    main()

