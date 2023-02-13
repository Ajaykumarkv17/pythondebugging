def convert(n):  
    decimal=n  
    octal=[]
    while(decimal>0):
        r=decimal%8
        octal.append(r) 
        decimal=decimal//8
    
    for j in reversed(octal):
       print(j)
    return reversed(octal) 
 
decimal=int(input("enter the number"))
for i in range(decimal):
    a=[convert(i)]




