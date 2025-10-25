# Take the maximum t
# Add up the diff between t - each num

n = int(input())

r = 0
c = list(map(int,input().split()))

t = max(c)
c.remove(t)

for j in c:
    r += t - j         

print(r)

