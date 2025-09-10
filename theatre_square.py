import math 

n, m, a = map(int, input().split())

squares_needed = math.ceil(n / a) * math.ceil(m / a)

print(squares_needed)