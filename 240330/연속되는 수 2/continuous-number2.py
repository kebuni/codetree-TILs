N = int(input())
arr = [int(input()) for i in range(N)]

def find_last_index(i,cur):
    idx = i
    for j in range(i+1,N):
        if arr[j] == cur:
            idx = j
        else:
            break
    return idx

ans = 0
for i in range(N):
    cur = arr[i]
    j = find_last_index(i,cur)
    ans = max(ans, j-i+1)
    i = j+1

print(ans)