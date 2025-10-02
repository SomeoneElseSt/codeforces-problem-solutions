# Input: 
# k = the price of the chosen shovel
# r = one coin of r burles 
# Assume unlimited 10 burles

# Processing:
# What is the minimum amount of shovels of k price to buy so that he does not recieve any change. 
# Put differently, when is the last digit of the current accumulate of shovels at price k either 0 or equal to r 

k, r = map(int, input().split())

temp = 0
counter = 0

if int(str(k)[-1]) == r:
    print("1")
    exit()
else:
    for i in range(10):
        counter += 1
        temp += k
        l_digit = int(str(temp)[-1])
        if l_digit == r or l_digit == 0:
            break

print(counter)
            