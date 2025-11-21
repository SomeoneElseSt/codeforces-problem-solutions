"""
Solution to ASCII Art Contest from Codeforces
"""

lst = list(map(int, input().split()))

mx_score = max(lst)
lst.remove(mx_score)

mn_score = min(lst)
lst.remove(mn_score)

if mx_score - mn_score >= 10:
    print("check again")
else:
    print(f"final {lst[0]}")
