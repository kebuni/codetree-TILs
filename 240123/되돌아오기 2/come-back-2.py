import sys

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

x, y = 0, 0
ans = -1
time = 0
direction = 0
commands = sys.stdin.readline()

for command in commands:
    if command == 'F':
        x = x + dxs[direction]
        y = y + dys[direction]
    elif command == 'R':
        direction = (direction + 1) % 4
    else:
        direction = (direction + 3) % 4
    
    time = time + 1

    if x == 0 and y == 0:
        ans = time
        break

print(ans)