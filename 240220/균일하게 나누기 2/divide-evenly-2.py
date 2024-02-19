N = int(input())

x_limit = 0
y_limit = 0
xy_list = []

for i in range(N):
    x, y = map(int,input().split())
    xy_list.append((x,y))
    x_limit = max(x_limit,x)
    y_limit = max(y_limit,y)

x_list = [0 for i in range((x_limit+1)//2)]
y_list = [0 for i in range((y_limit+1)//2)]
x_split_l = [0 for i in range((x_limit+1)//2+1)]
x_split_r = [0 for i in range((x_limit+1)//2+1)]
y_split_l = [0 for i in range((y_limit+1)//2+1)]
y_split_r = [0 for i in range((y_limit+1)//2+1)]

for x, y in xy_list:
    x_list[x//2] += 1
    y_list[y//2] += 1

#print(x_list)
#print(y_list)

x_split_l = [0] + x_list
for i in range(1,len(x_split_l)):
    x_split_l[i] = x_split_l[i] + x_split_l[i-1]
#print(x_split_l)

x_split_r = x_list + [0]
for i in range(len(x_split_r)-2,-1,-1):
    x_split_r[i] = x_split_r[i] + x_split_r[i+1]
#print(x_split_r)

y_split_l = [0] + y_list
for i in range(1,len(y_split_l)):
    y_split_l[i] = y_split_l[i] + y_split_l[i-1]
#print(y_split_l)

y_split_r = y_list + [0]
for i in range(len(y_split_r)-2,-1,-1):
    y_split_r[i] = y_split_r[i] + y_split_r[i+1]
#print(y_split_r)

x_diff_min = 987654321
y_diff_min = 987654321
x_diff_idx = -1
y_diff_dix = -1
for i in range(len(x_split_l)):
    if abs(x_split_l[i] - x_split_r[i]) < x_diff_min:
        x_diff_min = abs(x_split_l[i] - x_split_r[i])
        x_diff_idx = i

#print(x_diff_min)
#print(x_diff_idx)

for i in range(len(y_split_l)):
    if abs(y_split_l[i] - y_split_r[i]) < y_diff_min:
        y_diff_min = abs(y_split_l[i] - y_split_r[i])
        y_diff_idx = i

#print(y_diff_min)
#print(y_diff_idx)

x_diff_idx *= 2
y_diff_idx *= 2
#print(x_diff_idx,y_diff_idx)

q1, q2, q3, q4 = 0, 0, 0, 0
for x,y in xy_list:
    #print("x,y: ",x,y)
    if x > x_diff_idx and y > y_diff_idx:
        q1 += 1
    elif x > x_diff_idx and y < y_diff_idx:
        q2 += 1
    elif x < x_diff_idx and y > y_diff_idx:
        q3 += 1
    else:
        q4 += 1

#print(q1,q2,q3,q4)
print(max(q1,q2,q3,q4))