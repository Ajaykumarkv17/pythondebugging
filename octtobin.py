octal=int(input("enter the number"))
decimal=0
n=0
while(octal>0):
    
    r=octal%10;
    decimal=decimal+r*pow(8,n)
    octal=octal//10
    n=n+1
print(int(decimal))
binary=[]
while(decimal!=0):
    r=decimal%2
    binary.append(r)
    decimal=decimal//2

for i in reversed(binary):
    print(i,end=" ")
