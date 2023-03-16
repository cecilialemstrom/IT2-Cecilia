import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**2

xverdier = np.linspace(0, 10, 11)
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)
plt.show()