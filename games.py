n = int(input())

teams_list = []
for team in range(1, n+1):
    teams_list.append(list(map(int, input().split())))

counter = 0
h1, a1 = 0, 0

for team in teams_list:
    if a1 == team[0]:
        counter += 1
    h1, a1 = team[0], team[1]

print(counter)

    

