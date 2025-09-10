import math 

line = "664"
line = list(line)

n, m, a = int(line[0]), int(line[1]), int(line[2])

squares_needed = math.ceil(n / a) * math.ceil(m / a)

print(squares_needed)