a=36
b=60
hcf=0
for i in range(1,a or b):
    if(a%i==0 and b%i==0):
        hcf=i

print(hcf)
