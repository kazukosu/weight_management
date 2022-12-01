import matplotlib.pyplot as plt
import numpy as np

dummy_list=[[141127, 100], [141355, 142], [142027, 161], [171436, 132]]

weight = np.array(dummy_list)[:,1]
date = np.array(dummy_list)[:,0]
print(weight)
print(date)

plt.plot(date,weight)
plt.show()