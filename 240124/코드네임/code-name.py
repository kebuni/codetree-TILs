agents = []

for i in range(5):
    name, score = input().split()
    agents.append((name, int(score)))

min_score = 1000

for i in range(5):
    cur_name, cur_score = agents[i]
    if cur_score < min_score:
        min_name = cur_name
        min_score = cur_score

print(min_name,min_score,end=' ')