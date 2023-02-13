
import numpy as np
from scipy import linalg
testqn=np.array([[1,1],[4,9]])
print(testqn)
testans=np.array([30,150])
print(testans)
a=linalg.solve(testqn,testans)
print(a)