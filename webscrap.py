

from bs4 import BeautifulSoup
import requests
url ='http://www.simplilearn.com'
res=requests.get(url)
webpage=res.content
s=BeautifulSoup(webpage,'html.parser')
res.close()
a=s.contents
print(a)
print (s.prettify)
b= s.findPrevious
print(b)