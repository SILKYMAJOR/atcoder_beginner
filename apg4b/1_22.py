from operator import itemgetter

N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]

for line in sorted(num_list, key=itemgetter(1)):
  print(line[0], line[1])

