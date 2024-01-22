x, y = 0, 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
direction = 0

commands = input()

for command in commands:
    if command == 'R':
        direction = (direction + 1) % 4
    elif command == 'L':
        direction = (direction + 3) % 4
    else :
        x = x + dx[direction]
        y = y + dy[direction]
        
print(x, y, end=' ')