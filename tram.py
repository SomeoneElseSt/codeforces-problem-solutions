n = int(input())

current_passengers = 0
max_passengers = 0

for station in range(n):
    passengers_exit, passengers_enter = map(int, input().split())
    
    # Update current passenger count: subtract those who exit, add those who enter
    current_passengers = current_passengers - passengers_exit + passengers_enter
    
    # Update maximum if current count is higher
    if current_passengers > max_passengers:
        max_passengers = current_passengers

print(max_passengers)