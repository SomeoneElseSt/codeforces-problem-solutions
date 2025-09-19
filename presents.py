# Input: 
# n = Number of friends
# s = the friends, where the index indicates to whom the friend at the i-th position gave the gift to 

n = int(input())

friends = list(map(int,input().split()))

reversed_friends = []

for i, friend in enumerate(friends, start = 1): 
    if friend == i:
        reversed_friends.append(friend)
    else: 
        # We need to scan the list to find a value where
        # friend == i 
        # ie. the current value is equal to the index (the friend who gave to the friend in that position) and then append its position 
        for position, friend in enumerate(friends, start = 1):
            if friend == i:
                reversed_friends.append(position)

print(' '.join(map(str, reversed_friends)))