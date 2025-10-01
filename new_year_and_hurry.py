# Input: 
# n = amount of problems, which when expanded is ascending (in order of difficultity)
# k = minutes he has to get to the party 

# Processing: 
# Limak takes 5 * i minutes to solve the i-th problem of n 
# We want to find out, given that we know he has four hours to BOTH get to the party and do problems, given the amount of time it takes him to get to the party - 240 (four hours in min), this is the amount of time he can do problems, so how many problems can he solve in k - 240

n, minutes = map(int, input().split())

FOUR_HOURS = 240

# This is the amount of time he can take to do problems 
diff = FOUR_HOURS - minutes

temp = 0
counter = 0

# Now, we want to know how many problems fit into the given diff 
for problem in range(1, n+1):
    temp += 5 * problem
    if temp > diff:
        break
    else: 
        counter += 1


print(counter)



