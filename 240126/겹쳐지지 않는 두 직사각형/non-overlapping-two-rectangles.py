n, m = map(int,input().split())

grid = []
ans = -9999999

for i in range(n):
    grid.append(list(map(int,input().split())))

for x1u in range(n):
    for y1u in range(m):
        for x1d in range(x1u,n):
            for y1d in range(y1u,m):
                
                sum1 = 0
                for i in range(x1u,x1d+1):
                    for j in range(y1u,y1d+1):
                        sum1 = sum1 + grid[i][j]

                # right part
                for x2u in range(n):
                    for y2u in range(y1d+1,m):
                        for x2d in range(x2u,n):
                            for y2d in range(y2u,m):

                                sum2 = 0
                                for i in range(x2u,x2d+1):
                                    for j in range(y2u,y2d+1):
                                        sum2 = sum2 + grid[i][j]

                                ans = max(ans,sum1+sum2)

                #down part
                for x2u in range(x1d+1,n):
                    for y2u in range(m):
                        for x2d in range(x2u,n):
                            for y2d in range(y2u,m):

                                sum3 = 0
                                for i in range(x2u,x2d+1):
                                    for j in range(y2u,y2d+1):
                                        sum3 = sum3 + grid[i][j]

                                ans = max(ans,sum1+sum3)


print(ans)