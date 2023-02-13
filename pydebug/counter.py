from collections import Counter

l=list(map(int,input().split()))
c=Counter(l)
out=0
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(a in c.keys() and c[a]>0):
        out=out+b
        c[a]-=1
        
print(out)
    