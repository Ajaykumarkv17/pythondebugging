
import matplotlib.pyplot as plt
cause='hsuuus','jsiuwy','juswsygy','kiayw87std','jwshswy'

percintile=[45,66,12,33,44]

plt.figure(figsize=(10,10))

explode =(0.05,0.10,0,0,0,0)
plt.pie(percintile,labels=cause,explode=explode,autopct='%1.1f%%',startangle=70)

plt.axis('equal')
plt.title('state-2012:leading causes')
plt.show()
