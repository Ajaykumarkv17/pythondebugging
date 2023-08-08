l=[10,20,100,10,20,30]
d={}
n=len(l)
for i in range(n):
    if(l[i] in d.keys()):
        d[l[i]]=d[l[i]]+1
    else:
        d[l[i]]=1
    
print(d)
