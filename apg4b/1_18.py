num, game = map(int, input().split())

result = []

for i in range(num):
    row = []
    for j in range(num):
        row.append("-")
    result.append(row)

for g in range(game):
    a, b = map(int, input().split())
    result[a-1][b-1] = "o"
    result[b-1][a-1] = "x"

for i in result:
    print(*i, sep=' ')

