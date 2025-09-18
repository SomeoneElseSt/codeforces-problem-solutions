# Input:
# n = 1 <= n <= 10^25

# Sequence:
# - + - + 

# Processing 
# We need to take the i-th element, and with the right operator modify it with the i-th + 1 element, keeping track of the result  

# The above was not efficient for a bigger N
# The problem really is = sum(even numbers up to N // 2) - sum(odd numbers up to N // 2)
# So so long as I can get two lists each of n // 2 one even and one odd, this is trivial. Or two variables
# The question is how to get them in O(1) or some other Theta-bound 
# We can use a Gauss's sum over the sequence for this
# Post solution note: A gauss worked here because the sequence is alternating, so it just had to be packed into pairs of two 


n = int(input()) 

if n % 2 == 0:
    r = n // 2
else: 
    r = -(n + 1) // 2
    
print(r)

# Some innefficient implementation
# for i in range(1, n + 1):

#     if switched == False:
#         result -= i
#         switched = True
#     elif switched == True:
#         result += i
#         switched = False
# print(result)