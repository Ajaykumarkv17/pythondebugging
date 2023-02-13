octal=int(input("enter the octal number"))
decimal=0
n=0
while(octal>0):
    temp=octal%10
    decimal+=temp*pow(8,n)
    octal=octal//10
    n=n+1
print(int(decimal))

