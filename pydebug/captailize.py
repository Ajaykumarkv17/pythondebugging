def convert(s):
    v=""    
    for  word in s.split():
   
        v=v+"".join(word.capitalize())
    
    return v
      
s="hello world"
a=convert(s)
print(a)



