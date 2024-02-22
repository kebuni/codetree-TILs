ans = set()
COLOR1 = 'W'
COLOR2 = 'B'


R, C = map(int,input().split())
grid = [list(input().split()) for _ in range(R)]

if grid[0][0] == 'B':
    COLOR1 = 'B'
    COLOR2 = 'W'
    
for i1 in range(1,R):
    for j1 in range(1,C):

        if grid[i1][j1] == COLOR2:

            for i2 in range(i1+1,R):
                for j2 in range(j1+1,C):

                    if grid[i2][j2] == COLOR1:

                        for i3 in range(i2+1,R):
                            for j3 in range(j2+1,C):

                                if grid[R-1][C-1] == COLOR2:
                                    #print(i1,j1,i2,j2)
                                    ans.add((i1,j1,i2,j2))
print(len(ans))