
n = int(input())

groups = 1

previous = input()

for magnet in range(n - 1):
    current = input()
    
    if current != previous:
        groups += 1
    
    previous = current

print(groups)
