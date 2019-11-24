_ = int(input())
num_list = list(map(int, input().split()))
num_dict = {}

for i in num_list:
  try:
    num_dict[i] += 1
  except:
    num_dict[i] = 1

max_k = max(num_dict, key=num_dict.get)
print(max_k, num_dict[max_k])

