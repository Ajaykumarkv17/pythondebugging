l=[1,0,0,0,9,8,0,3,0,2,7]
al=[]
n=len(l)
print(n)
for j in l:
    if(j==0):
        al.append(j)
        l.remove(j)

print(l)
print(al)
