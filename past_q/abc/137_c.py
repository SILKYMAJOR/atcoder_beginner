def main():
    n = int(input())

    s_dict = {}
    count = 0
    
    for i in range(n):
        s = sorted(input())
        _s = "".join(s)
        
        if not _s in s_dict:
            s_dict[_s] = 1
        else:
            count += s_dict[_s]
            s_dict[_s] += 1
    print(count)


if __name__ == '__main__':
    main()

