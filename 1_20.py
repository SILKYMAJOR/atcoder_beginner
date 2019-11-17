num = int(input())
parent_id = list(map(int, input().split()))

sum = [0]*num

for i in (reversed(parent_id)):
    sum[0] += 1
    if i != 0:
        sum[i] += 1 + sum[num - 1]
    sum[num - 1] += 1
    num -= 1

sum[0] += 1

print(*sum, sep="\n")

