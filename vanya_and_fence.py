# Inputs
# n, h = the N of friends, and the height of the fence
# a = the height of each person 

# Rules:
# The width of the person not crouched == 1
# The width of the person crouched == 2
# What is the minimum width of the road that fits N * 2 for all N whom are > h, and N * 1 for all N whom are < h

# Processing: 
# Iterate over a; a will need to be made into a list.
# If a > h, the road requires + 2 width
# else, the road requires + 1 width 


n, h = map(int,input().split())

a = list(map(int,input().split()))

width_counter = 0

for height in a:
    if height > h:
        width_counter += 2
    else:
        width_counter += 1

print(width_counter)



