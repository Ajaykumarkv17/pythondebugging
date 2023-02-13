from tkinter import N


n=6
for  i in range(1,n):
    j=0
    for k in range(0,n):
        
        m=(i+j)%6
        if(m>0):
            print(m,end='')
        j=j+1

    print()