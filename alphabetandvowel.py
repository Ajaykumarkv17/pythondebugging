from ctypes.wintypes import CHAR


a=['a','e','i','o','u']
n=len(a)
b=(input("enter the character"))
count=0
for i in range(n):
    if( b==a[i]):
        count=count+1
        break
if(count==0):
    print("it is consonant")
else:
    print("it is vowel")