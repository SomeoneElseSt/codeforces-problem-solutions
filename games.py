# Input: 
# n = number of matches 
# h, a = number pairs of games

# Processing: 
# Two sets of numbers: 
# Home Team, Guest Team 
# If 

n = int(input())

counter = 0
h1, a1 = 0, 0


for team in range(1, n+1):
    h2, a2 = map(int, input().split())

    if a1 == h2:
        counter += 1

    h1, a1 = h2, a2

print(counter)





