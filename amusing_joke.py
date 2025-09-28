# Input:
# g_name = Guest name
# h_name = Host name
# Pile of unordered letters 

# Processing
# Print true if the pile can be permuted (ie. its elements can be re-ordered) to make g_name and h_name again
# Without any missing letters or any remainder letters

# Maybe we can use a target and list traversal here. So, while temp != g_name a for loop runs through the pile and appends the first element it finds that matches the first letter, second letter, and so on.
# Delete from the pile the letters already used 
# If a letter is not found, terminate early and print NO
# If after both are built pile is not None, print No
# Else YES

g_name = list(input())
h_name = list(input())
pile = list(input())

joint_names = g_name + h_name 

temp = []
counter = 0
target = joint_names[counter]

while temp != joint_names:
    for char in pile:
        if char == target:
            temp.append(char)
            target = joint_names[counter + 1]

if joint_names or len(temp) != len(joint_names):
    print("NO")
else:
    print("YES")