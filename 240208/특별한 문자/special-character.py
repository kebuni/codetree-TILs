word = input()

dic = {}

for char in word:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1

ans = False

for key in dic:
    if dic[key] == 1:
        print(key)
        ans = True
        break

if ans==False:
    print("None")