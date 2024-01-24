n, k, prefix = input().split()
n = int(n)
k = int(k)

def is_prefix(word,prefix):
    if len(word) < len(prefix):
        return False
    
    for i in range(len(prefix)):
        if prefix[i] != word[i]:
            return False

    return True

words = []

for i in range(n):
    word = input()
    if is_prefix(word,prefix):
        words.append(word)

words.sort()

print(words[k-1])