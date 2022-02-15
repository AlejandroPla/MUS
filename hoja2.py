import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1
'''arr = np.random.uniform(1, -1, 44100)

plt.plot(arr)
plt.show()'''

# Ejercicio 2
arr = np.random.uniform(1, -1, 44100)
t = 44100 - 1
signal = np.sin(2*np.pi)*arr

plt.plot(arr, signal)
plt.show()