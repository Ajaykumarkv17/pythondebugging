x = input() #Input #1
a = set(map(int, input().split())) #Input #2
y = input() #Input #3
b = set(map(int, input().split())) #Input #4

# Convert the lists back to set
c = set(a.difference(b))
d = set(b.difference(a))

# union of both the above sets in sorted order
e = sorted(c.union(d))
for i in e:
    print(i)