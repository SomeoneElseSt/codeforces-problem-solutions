cases = int(input())
cases_results = []

for case in range(cases):
    current_case = list(input())

    current_count = 0
    for i in current_case:
        current_count += int(i) 
    cases_results.append(current_count)

print("\n".join(map(str, cases_results)))
        

