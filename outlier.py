"""
from pyexpat import features
from sklearn.datasets import load_diabetes
dataset=load_diabetes()

a=dataset.data
print(a)
print(dataset['feature_names'])
import numpy as np
import pandas as pd
df=pd.DataFrame(data=np.c_[dataset['data'],dataset['target']],columns=dataset['feature_names']+['target'])
print(df)
c=df.isnull().any()
print(c)

import matplotlib.pyplot as plt
for column in df:
    plt.figure()
    df.boxplot([column])
"""

import pandas as pd
import numpy as np     
df=pd.Series(np.arange(0,51))
print(df.tail())

