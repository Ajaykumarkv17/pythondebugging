from operator import indexOf


s="8763gftqt5gfs5"
sum=0
for i in s:
    if ord(i)>=48 and ord(i)<=57:
        sum=sum+int(i)
print((sum))
