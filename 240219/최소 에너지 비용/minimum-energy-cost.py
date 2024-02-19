N = int(input())

dist = list(map(int,input().split()))
energy = list(map(int,input().split()))

min_energy = []
ans = 0

minimum = energy[0]

for i in range(N):
    minimum = min(minimum,energy[i])
    min_energy.append(minimum)

for i in range(N-1):
    ans += min_energy[i]*dist[i]

print(ans)