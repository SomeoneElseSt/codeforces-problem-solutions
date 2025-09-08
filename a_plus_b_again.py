cases = int(input())
cases_results = []

for case in cases:
    current_case = list(input())

    current_count = 0
    for i in current_case:
        current_count += i 

cases_results.append(current_count)

print("\n".join(cases_results))
        

