N = int(input())

dic = {}

for i in range(N):
    word = input()
    word = list(word)
    word.sort()
    word = str(word)
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

ans = -1
for key in dic:
    ans = max(ans,dic[key])

print(ans)