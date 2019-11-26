n = list(map(int, input().split()))
apple = list(map(int, input().split()))
pine = list(map(int, input().split()))

num = n[0]
sum = n[1]
count = 0

for i in range(num):
    for j in range(num):
        if sum == (apple[i] + pine[j]):
            count += 1
print(count)

