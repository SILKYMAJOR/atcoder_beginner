import math
N = int(input())
n = math.floor(N**(1/2))
r = []
for i in range(1,n+1):
    if(N%i == 0):
        r.append(i + N//i)

print(min(r)-2)

