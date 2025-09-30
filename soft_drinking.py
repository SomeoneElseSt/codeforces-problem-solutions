"""
 Inputs:
n = the number of friends
k = the # of bottles
l = the ml of the drink in each bottle
c = the # of limes
d = the # of slices they made with c
p = the grams of salt they have

For each friend, to make a toast they require nl of the drink and np grams of salt

Processing:

List all the constraints, pick smallest one and divide it by the number of people.
"""

n, k, l, c, d, p, nl, np = map(int, input().split())

constraint_m = k * l // n
constraint_l = c * d
constraint_s = p // np

print(min(constraint_m, constraint_l, constraint_s) // n)
