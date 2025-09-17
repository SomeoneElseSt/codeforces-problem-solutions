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

    for i in range(len(line) - 1, 0, -1):
        r_pointer = line[i]
        l_pointer = line[i - 1]

        if l_pointer == "B" and r_pointer == "G":
            line[i -1], line[i] = line[i], line[i -1]    
        
print(''.join(line))