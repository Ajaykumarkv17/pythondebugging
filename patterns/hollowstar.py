rows=4
col=4
for i in range(1,rows+1):
    for j in range(1,col+1):
        if((i==1 or i==col) or (j==1 or j==col)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()