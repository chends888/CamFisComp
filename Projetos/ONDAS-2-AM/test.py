import numpy as np
data = np.array([1,1,1,1,1])

carry = np.array([1,0,1,0,1])

data = data*carry
print(data)