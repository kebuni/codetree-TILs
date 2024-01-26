n, price = map(int,input().split())

grid = []
ans = -1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def find_max(size):
    max = -1
    cost = size*size + (size+1)*(size+1)

    for x in range(n):
        for y in range(n):
            temp = 0
            for i in range(-size,size+1):
                for j in range(abs(i)-size , -abs(i)+size+1):
                    if in_range(x+i,y+j):
                        temp = temp + grid[x+i][y+j]
            if temp*price-cost >= 0:
                if temp > max:
                    max = temp

    # print(size, cost, max)
    return max

for i in range(n):
    grid.append(list(map(int,input().split())))

for size in range(n//2*2+1):
    max = find_max(size)
    if max > ans:
        ans = max

print(ans)