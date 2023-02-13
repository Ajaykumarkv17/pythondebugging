#%%

from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from matplotlib import style

boston_real= load_boston()
x=boston_real.data
print(x)
y=boston_real.target
style,('gggplot')
plt.figure(figsize=(7,7))
plt.hist(y,bins=30)
plt.xlabel("price in 1000")
plt.ylabel("number of houses")

# %%
