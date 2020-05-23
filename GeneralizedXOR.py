import numpy as np
import matplotlib.pyplot as plt


x0 = np.random.uniform(-1, 1, 1000)
x1 = np.random.uniform(-1, 1, 1000)

y = np.zeros(len(x0))
y[x0*x1 > 0] = 1

plt.scatter(x0, x1, c = y)
plt.show()
