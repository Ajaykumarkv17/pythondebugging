a=10111
temp=a
dec=0
n=0
while(a>0):
  
    temp=a%10
    dec=dec+temp*pow(2,n)
    a=a//10
    n=n+1


print((dec))