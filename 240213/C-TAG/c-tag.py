N, M = map(int,input().split())

ans = 0
s = set()

groupA = [input() for i in range(N)]
groupB = [input() for i in range(N)]

def test(i,j,k):
    global ans, s

    s.clear()

    for x in range(N):
        s.add(groupA[x][i:i+1]+groupA[x][j:j+1]+groupA[x][k:k+1])

    for x in range(N):
        elem = groupB[x][i:i+1]+groupB[x][j:j+1]+groupB[x][k:k+1]
        if elem in s:
            return False

    return True

for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            if test(i,j,k): ans+=1

print(ans)