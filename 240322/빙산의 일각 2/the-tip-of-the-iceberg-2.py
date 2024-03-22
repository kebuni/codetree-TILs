N = int(input())
arr = [int(input()) for i in range(N)]
ans = 0

def get_cluster_num(h):
    result = 0
    keep = False
    for i in range(N):
        if keep:
            if arr[i] > h:
                continue
            else:
                keep = False
        else:
            if arr[i] > h:
                keep = True
                result += 1
            else:
                continue
    return result


for h in range(min(arr),max(arr)+1):
    ans = max(ans,get_cluster_num(h))
print(ans)