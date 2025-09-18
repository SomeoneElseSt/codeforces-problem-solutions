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
# We can use Gauss's sum for this

n = int(input()) 

n_halved = n // 2

def gauss_sum_even(n):
    return 

def gauss_sum_odd(n):
    return 

print(gauss_sum_even(n_halved) - gauss_sum_odd(n_halved))

# Some innefficient implementation
# for i in range(1, n + 1):

#     if switched == False:
#         result -= i
#         switched = True
#     elif switched == True:
#         result += i
#         switched = False
# print(result)