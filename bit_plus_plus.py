x = 0
lines = []

lines_lenght = int(input())

for _ in range(lines_lenght):
    line = input()
    lines.append(line)

for line in lines:
    if "+" in line:
        x += 1
    elif "-" in line:
        x -= 1

print(x)

 

