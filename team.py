problems = []
solved_problems = 0

lines_lenght = int(input())

for _ in range(lines_lenght):
    line = input().strip()
    problems.append(line)

for line in problems:
    if sum(map(int, line.split())) >= 2:
        solved_problems += 1

print(solved_problems)


