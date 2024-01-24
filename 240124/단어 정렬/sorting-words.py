n = int(input())
words = []
for i in range(n):
    words.append(input())
words.sort()

for word in words:
    print(word)