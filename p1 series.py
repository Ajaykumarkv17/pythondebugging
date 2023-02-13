
import numpy as np
import pandas as pd
print(pd.__file__)
np_country=np.array([['hello','norway'],['uygswyw6ts','uhswyt']])
s_country=pd.DataFrame(np_country)
print(s_country)
s=pd.Series(list('abcdef'))
print(s)
scalar_series=pd.Series(5,index=['a','c','b','v','g'])
print(scalar_series)
first_vector_series=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(first_vector_series)
sec=pd.Series([10,20,30,40],index=['a','c','d','b'])
first_vector_series+=sec
print(first_vector_series)
