N = int(input())
num_list = [64, 32, 16, 8, 4, 2, 1]

for i in num_list:
  if N>=i:
    print(i)
    exit(0)

print(0)

