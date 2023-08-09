"""from itertools import permutations
l=[23,56,7,89,21,234,122]
perm=permutations(l,3)
print(*perm)
for k in range(0,2):
    temp=l[len(l)-1]
    for i in range(len(l)-1,-1,-1):
        l[i]=l[i-1]
        
    l[0]=temp

print(l)"""
def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
 

div(2,4)
