n=5
for i in range(0,n):
    for j in range(0,i):
        print(" ",end='')
    for k in range(2*i,n*2-1):
        print("*",end='')
    print()