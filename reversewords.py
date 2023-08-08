def reversewords(a):
       s=a.split(" ")
       s.reverse()
       return " ".join(s)

print(reversewords("hello iam python"))