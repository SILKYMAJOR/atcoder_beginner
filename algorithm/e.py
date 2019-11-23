n, m = map(int, input().split())
cnt = [0]*(n + 1)
PY = [[i]+list(map(int, input().split())) for i in range(m)]
XY = sorted(PY, key=lambda x: x[2])

ans = [0]*m
for i, x, y in XY:
    cnt[x] += 1
    a = "{:0=6}".format(x)
    b = "{:0=6}".format(cnt[x])
    ans[i] = a+b

[print(a) for a in ans]

