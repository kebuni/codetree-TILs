import sys
sys.setrecursionlimit(100000)

N = int(input())

parent = list(map(int,input().split()))
is_leaf = [True for i in range(N)]
target = int(input())
is_child_of_target = [False for i in range(N)]

# print(target)

for node in range(N):
    # print("node:",node)
    cur = node
    if cur == target:
        # print(node, "is son of target")
        is_child_of_target[node] = True
    while cur != -1:
        cur = parent[cur]
        if cur != -1:
            # print(cur, "is not leaf")
            is_leaf[cur] = False
        if cur == target:
            # print(node,"is son of target")
            is_child_of_target[node] = True

# print(is_leaf)
# print(is_child_of_target)
ans = 0
for i in range(N):
    if not is_child_of_target[i] and is_leaf[i]:
        ans += 1
print(ans)