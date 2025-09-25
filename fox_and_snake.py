# Input:
# n, m = n, the number of rows that the snake occupies. m, the number of # asterisks in each row that the snake occupies

# Processing: 
# If we know the number of lines that have full asterisks, we can append sequentially all those lines to a list snake, changing the join line in-between. 
# Snake must be a sequence of lists within the bigger list so that the join operation adds new lines per each new snake line 
 
# We know all s_line lines are the odd numbered rows, while the even numbered rows are j_line, so all we need to do is make a for loop that appends s_line to all odd numbers, and alternates between j_line_r and j_line_l on all even numbers 

n, m = map(int,input().split())

s_line = ("".join(['#'] * m ))
j_line = ("".join(['.'] * (m - 1))) # Leave space for '#' at start or end

j_line_r = "".join([j_line, "#"])
j_line_l = "".join(["#", j_line])

snake = []
swap = False

for line in range(1,n+1):
    if line % 2 != 0: # Odd, snake line
        snake.extend(s_line)
    elif swap == False: # Not odd, start at j_line_r
        snake.extend(j_line_r)
        swap = True
    elif swap == True: # Swaps order
        snake.extend(j_line_l)
        swap = False

print(snake)
print("\n".join(map(str, snake)))