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
        # i == friends
        # ie. the current index (enumerate) is equal to a value in the list 
        for j in friends:
            if i == friend: 
                reversed_friends.append(friends.index(friend))

print(' '.join(map(str, reversed_friends)))