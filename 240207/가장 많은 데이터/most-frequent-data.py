dic = {}

N = int(input())

ans = 0

for _ in range(N):
    word = input()
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

for elem in dic:
    ans = max(ans,dic[elem])

print(ans)