from tempfile import tempdir


rev=0
temp=0
n=int(input("enter the number"))
temp=n
while(n>0):
    a= int(n%10)
    rev=rev*10+a  
    n=n//10
    print(rev) 
if(temp==rev):
    print("the number is palindrome")
else:
   print("the number is not palindrome")
