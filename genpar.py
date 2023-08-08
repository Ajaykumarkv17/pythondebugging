def genpar(n,openb,closeb,s,ans):
    if openb==n and closeb==n:
        ans.append(s)
        return 
    
    if openb < n :
        genpar(n,openb+1,closeb,s+'(',ans)
    if closeb < openb:
        genpar(n,openb,closeb+1,s+')',ans)





n=3
ans=[]
s=""
genpar(n,0,0,s,ans)
for s in ans:
    print(s)
