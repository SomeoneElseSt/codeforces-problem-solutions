k = int(input())
l = int(input())
m = int(input())
n = int(input())

d = int(input())

counter = 0

for i in range(1, d + 1):
    if any(i % divisor == 0 for divisor in (k, l, m, n)):
        counter += 1
    
print(counter)