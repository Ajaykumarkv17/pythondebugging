def findstr(string ,sub_string):
     c=0
     while sub_string in string:
        a=string.find(sub_string)
        string=string[a+1:]
        c+=1
     return c




string="ajaykumarajaykumarajay"
sub_string="ajay"
count=findstr(string,sub_string)
print(count)


