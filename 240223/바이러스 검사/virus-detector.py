N = int(input())

ans = N

rests = list(map(int,input().split()))

manager, employee = map(int,input().split())

for rest in rests:
    ans += (rest - manager) // employee
    if (rest - manager) % employee:
        ans += 1

print(ans)