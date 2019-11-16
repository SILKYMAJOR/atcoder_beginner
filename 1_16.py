flag = False
a = list(map(int, input().split()))

i = 0
for j in a:
    if i == j:
        flag = True
    i = j
if flag:
    print("YES")
else:
    print("NO")

