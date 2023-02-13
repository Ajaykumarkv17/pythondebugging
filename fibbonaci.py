n=int(input("enter the count"))
a=0
b=1
print(a)
print("\n",b)
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
    print("\n",c)