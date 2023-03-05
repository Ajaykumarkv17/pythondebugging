from collections import defaultdict

n,m=map(int,input().split())

d=defaultdict(list)

for i in range(n):
    d[input()].append(str(i+1))

for j in range(m):
    key=input()
    if key in d:
        print(" ".join(d[key]))
    else:
        print(-1)
