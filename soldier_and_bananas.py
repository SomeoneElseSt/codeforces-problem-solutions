# 
# w = bananas
# k = price of banana, doubles at each  iter 
# n = dollars



# k = The cost of the first banana
# n = the initial dollar amount the soldier has 
# w = the the number of bananas he wants 

# Processing: 
# Iterate over w to find out the total banana cost, by for looping the original k var and adding to a var each time, doubling this var 
# Then, return the difference of n - total_cost


initial_price, current_cash, desired_bananas = map(int, input().split())

all_bananas = []

for banana in range(1, desired_bananas + 1):
    all_bananas.append(banana * initial_price)
    
print(sum(all_bananas) - current_cash)

