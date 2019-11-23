n = int(input())
str_list = []
str_dict = {}
count = 0

for i in range(n):
    a = list(input())
    a.sort()
    b = "".join(a)
    str_list.append(b)
    try:
        str_dict[b] += 1
    except:
        str_dict[b] = 1

for key, val in str_dict.items():
    count += val * (val - 1) / 2
print(int(count))

