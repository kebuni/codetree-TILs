from collections import deque
ans = 0
#####################

#####################

N, K = map(int,input().split())
group_list = [set() for i in range(N+1)]
group_invitation_list = [set() for i in range(K)]
invited = [False for i in range(N+1)]
check_list = deque()

for g in range(K):
    line = list(map(int,input().split()))
    group_num = line[0]
    for i in range(1,group_num+1):
        group_list[line[i]].add(g)
        group_invitation_list[g].add(line[i])

#print(group_list)
check_list.append(1)
invited[1] = True
        
while check_list:

    x = check_list.popleft()
    ans += 1

    for group in group_list[x]:
        
        group_invitation_list[group].remove(x)
        if len(group_invitation_list[group])==1:
            p_num = list(group_invitation_list[group])[0]
            if not invited[p_num]:
                invited[p_num] = True
                check_list.append(p_num)

print(ans)