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
    r_pointer = len(line) - 1
    l_pointer = len(line) - 2

    for pair in range(len(line)):
        r_pointer -= 1
        l_pointer -= 1
        
        if line[l_pointer] == "B" and line[r_pointer] == "G":
            line[l_pointer], line[r_pointer] = line[r_pointer], line[l_pointer] 

print(str(line))


        
