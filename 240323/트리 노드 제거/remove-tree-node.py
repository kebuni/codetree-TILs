N = int(input())

edge = [[] for i in range(N)]
root = -1
parents = list(map(int, input().split()))
for node, parent in enumerate(parents):
    if parent == -1:
        root = node
    else:
        edge[parent].append(node)

deleted = int(input())

#################################

def traverse(cur):
    #print("cur:",cur)
    global ans
    if cur == deleted:
        return

    is_leaf = True
    for next in edge[cur]:

        if next == deleted:
            continue

        is_leaf = False

        traverse(next)

    if is_leaf:
        #print("cur is leaf")
        ans += 1

    return


#################################
ans = 0
traverse(root)
print(ans)