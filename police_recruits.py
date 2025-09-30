# Inputs:
# N = number of events
# events = list, -1 = crime, int > 0 = officers recruited at that time

# Processing:
# Some thoughts off the bat are that, all N up to the first int > 0 should add to the counter.
# The real pattern though is that whenever the event is positive we should keep a track. If then we have a negative event, if the officers is not negative then we should substract one event from the officers. If it is, we should add to the counter 

# 1 -1 1 -1 -1 1 1 1
# officer+ officer officer+ officer crime officer+ officer+ officer+

n = int(input())
events = list(map(int, input().split()))

officers = 0 
counter = 0

for event in events: 
    if event > 0:
        officers =+ event
    else: 
        if officers > 0:
            officers = officers - 1
        else:
            counter += 1

print(counter)