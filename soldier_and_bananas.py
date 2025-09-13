initial_price, current_cash, desired_bananas = map(int, input().split())

all_bananas = []

for banana in range(1, desired_bananas + 1):
    all_bananas.append(banana * initial_price)

if current_cash > sum(all_bananas):
    print(0)
else:
    print(abs(sum(all_bananas) - current_cash))

