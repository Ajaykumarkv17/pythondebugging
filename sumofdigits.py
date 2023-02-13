sums=0
n=int(input("enter the number"))
while(n!=0):
    a= int(n%10)
    sums=sums+a   
    n=n/10
print(sums) 