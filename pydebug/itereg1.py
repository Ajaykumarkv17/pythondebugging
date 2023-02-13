"""
import itertools  
temp = 0  
for i in itertools.cycle("123"):  
    if temp > 7:  
        break  
    else:  
        print(i,end=' ')  
        temp = temp+1 """
import itertools
from itertools import product 
print(list(itertools.repeat(10,15)))
print(list(product([1, 2], repeat=2))) 
import itertools  
# initializing list  
list1 = [2, 4, 5, 7, 8]  
# using dropwhile() iterator that will print start displaying after condition is false  
print("The output is : ", end="")  
print(list(itertools.dropwhile(lambda x: x % 2 == 0, list1)))  

from itertools import permutations
s='ABC'
print(list(itertools.combinations(s)))