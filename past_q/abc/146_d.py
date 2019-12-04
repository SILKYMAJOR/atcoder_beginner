import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
child_list = [[] for i in range(n)]

for i in range(n-1):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    child_list[a].append([b,i])

ans = [None]*(n-1)


def rec(node, parent_color_id):
    default_color_id = 1
    color_id = default_color_id

    for child_node, no in child_list[node]:
        if parent_color_id == color_id:
            color_id += 1
        ans[no] = color_id
        rec(child_node, color_id)
        color_id += 1


rec(0, 0)
print(max(ans))
print(*ans, sep="\n")

