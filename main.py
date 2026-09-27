import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4])
y = x**2
plt.plot(x, y)
x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]
plt.plot(x1, y1, '-.')
plt.show()


plt.xlim(5, 25)
plt.ylim(5, 25)
plt.show


x = np.arange(1, 11, 1)
y1 = (2*x) + 1
y2 = (2*x**2) + 2
plt.plot(x, y1, 'g', linewidth=3, label='y=2x+1')
plt.plot(x, y2, 'r', linewidth=3, label='y=2x^2+2')
plt.legend()
plt.show()