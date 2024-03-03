N = int(input())

grid = [list(map(int,input().split())) for _ in range(N)]
selected = []
ans = -1

#####################

def choose(n):
    if n == 2:
        if is_possible():
            global ans
            ans = max(ans,num_coin())
        return

    for x in range(N):
        for y in range(N-2):
            selected.append((x,y))
            choose(n+1)
            selected.pop()

    return

def is_possible():
    s = set()
    x, y = selected[0]
    for i in range(3):
        s.add((x,y+i))
    x, y = selected[1]
    for i in range(3):
        if (x,y+i) in s:
            return False
    return True

def num_coin():
    sum = 0
    for x, y in selected:
        sum += grid[x][y]
        sum += grid[x][y+1]
        sum += grid[x][y+2]
    return sum

#####################

choose(0)
print(ans)