# Input:
# N = Number of Levels
# X = The level indices of the levels that X can pass
# Y = The level indices of the levels that Y can pass

# Rule:
# X can only pass p levels. Y can only pass q levels. 

# Processing:
# First we'll want to use a set to dedub the input for both lists 
# We'll also want to make a list in a range from 1 to N

# Then we can compare using all in python if all the elements in the N list are also in the joined list of X, Y

# Output: 
# If they can pass all the levels, print "I become the guy." else print "Oh, my keyboard!"

n = int(input())

x = list(map(int,input().split()))
y = list(map(int,input().split()))

nums = set(x[1:] + y [1:])

result = "I become the guy." if len(nums) == n else "Oh, my keyboard!"

print(result)