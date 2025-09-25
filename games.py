n = int(input())
teams_list = []
counter = 0

for i in range(n):
    h, a = map(int, input().split())
    teams_list.append([h, a])

for i in range(n):
    for j in range(n):
        if i != j:
            if teams_list[i][0] == teams_list[j][1]:
                counter += 1

print(counter)