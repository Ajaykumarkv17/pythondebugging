li=[20,50,4,10,40,15,30]
#sample output
#35
n=len(li)

maxdiff=li[0]
for i in range(1,n):
    for j in range(i+1,n):
        if li[j]>li[i]:
            diff=li[j]-li[i]
            if(maxdiff<diff):
                maxdiff=diff
        #else:
         #   continue

print(maxdiff)
