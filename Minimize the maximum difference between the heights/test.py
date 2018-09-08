import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,10,0.1)
x=[1, 3, 8, 10]
k = 2

plt.scatter(x,x)
plt.plot(t,t,t,t+k,t,t-k)

plt.grid()
plt.show()
