s = set()

N = int(input())

for i in range(N):
    command, value = input().split()
    value = int(value)

    if command == 'find':
        if value in s:
            print("true")
        else:
            print("false")
    elif command == 'add':
        s.add(value)
    else:
        s.remove(value)