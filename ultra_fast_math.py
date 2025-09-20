# Input:
# Two lines. Each contains one of the numbers and both are of the same lenght.
# n1, n2 = 0 or 1, 0 < len(n) < 100

n1 = list(map(int, input().strip()))
n2 = list(map(int, input().strip()))

result = []

for num_1, num_2 in zip(n1, n2):
    if num_1 == num_2: 
        result.append("0")
    else:
        result.append("1")

print(''.join(map(str, result)))