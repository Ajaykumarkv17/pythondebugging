
def emailcheck(email):
    import re
    return re.match(r'[a-zA-Z0-9-_]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$',email)
email="ajaykumar7@gmail.com"

print(emailcheck(email))
