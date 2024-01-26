n, m = map(int, input().split())

grid = []
ans = -1

def all_pos(i,j,k,l):
    for x in range(i,k+1):
        for y in range(j,l+1):
            if grid[x][y] <= 0:
                return False
    return True

for i in range(n):
    grid.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):

        # 시작점이 양수
        if grid[i][j] > 0:
            for k in range(i,n):
                for l in range(j,m):
                    if grid[k][l] >= 0:
                        if all_pos(i,j,k,l):
                            #print(i,j,k,l)
                            ans = max(ans,(k-i+1)*(l-j+1))

print(ans)