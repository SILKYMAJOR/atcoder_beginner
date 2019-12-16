def main():
    n = int(input())
    b_list = list(map(int, input().split()))
    a_list = []

    previous = 10 ** 5

    for b in b_list:
      a = min(previous, b)
      a_list.append(a)
      previous = b
      
    a_list.append(b_list[-1])
    print(sum(a_list))
    

if __name__ == '__main__':
    main()

