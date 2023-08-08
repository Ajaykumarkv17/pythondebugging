"""print(1//2*3)
x=input()
y=input()
print(x+y)
x = int(input())
y = int(input())
 
x = x / y
print(x)
y = y / x
 
print(y)
x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)



while True:
    print("I'm stuck inside a loop.")
i = 1
j = not not i

print(j)
my_list = []  # Creating an empty list.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)

vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_one) # outputs: ['bicycle', 'motor']
for i in range(1):
    print("#")
else:
    print("#")

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")
z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])
my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)
my_lit = [i for i in range(-1, 2)]
print(my_lit)
t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)
my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list)

x = 1
x = x == x
print(x).
def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)

introduction("ajay","kumafr")

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)


def f(x):
    if x == 0:
      return 0
    return x + f(x - 1)


print(f(3))

def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)


dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
   dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
   k = dictionary[i]
   print(k[0])# Insert your code here.



def func(a, b):
   return a ** a


print(func(2))
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)




def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))


def fun(x, y, z):
    return x + 2 * y + 3 * z


print(fun(0, z=1, y=3))


my_list =  ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'


print(my_list(my_list))


def fun(x):
    global y
    y = x * x
    return y


fun(2)
print(y)



def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return


print(fun(fun(2)) + 1)
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)
dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
 
for k in range(len(dictionary)):
    v = dictionary[v]
    print(v)
 

my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
def function_1(a):
    return None
 
 
def function_2(a):
    return function_1(a) * function_1(a)
 
 
print(function_2(2))



def func(a, b):
    return b ** a
 
 
print(func(b=2, 2))
print("a", "b", "c", sep="sep")
y = input()
x = input()
print(x + y)"""
print("Hello, World!")






 




