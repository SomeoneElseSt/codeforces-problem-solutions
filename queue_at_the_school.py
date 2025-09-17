# Input: 
# n, t = The N of children in the queue, The T time for which the order has got to be calculated 
# s = The initial arrangement of the children where B = boy and G = Girl 

# Processing: 
# Per each T, the boys and girls basically swap positions backwards, so if the original arrangement was BG, at the next T it will be GB
# Per each time t, in all cases where a character G is + 1 of a character B, these will be swapped.  

# G <<- 
# B ->>

n, t = map(int, input().split())
line = list(input())

for times in range(t):

    to_swap = []
    for i in range(len(line) - 1):
        if line[i] == "B" and line[i + 1] == "G":
            to_swap.append(i)

    for i in to_swap:
        line[i], line[i + 1] = line[i + 1], line[i]
            
print(''.join(line))