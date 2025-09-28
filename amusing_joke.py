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

if len(pile) > len(joint_names):
    print("NO")
    exit()

if all([pile.count(c) == joint_names.count(c) for c in set(joint_names + pile)]):
    print("YES")
else:
    print("NO")
