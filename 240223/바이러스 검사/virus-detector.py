N = int(input())

ans = N

rests = list(map(int,input().split()))

manager, employee = map(int,input().split())

for rest in rests:
    if rest - manager <= 0:
        continue
    ans += (rest - manager) // employee
    if (rest - manager) % employee:
        ans += 1

print(ans)