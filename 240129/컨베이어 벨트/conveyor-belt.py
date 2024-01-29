n, k = map(int,input().split())

grid = []

grid = grid + list(map(int,input().split()))
grid = grid + list(map(int,input().split()))

temp = grid[2*n-k:]

for i in range(2*n-1,k-1,-1):
    grid[i] = grid[i-k]

for i in range(k):
    grid[i] = temp[i]

for i in range(n):
    print(grid[i],end=' ')
print()
for i in range(n,2*n):
    print(grid[i],end=' ')