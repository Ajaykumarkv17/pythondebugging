import pandas as pd

oly={'hostcity':['london','newyork','spain','china'],'year':[2012,2013,2008,2009],'noofparticipatingcountries':[209,345,678,333]}
df=pd.DataFrame(oly)
print(df)


oly2={'paris':{2011:345},'delhi':{2019:567}}
df2=pd.DataFrame(oly2)
print(df2)
df3=df.hostcity
print(df3)
df4=df2.paris
print(df4)