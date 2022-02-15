import numpy as np
import matplotlib.pyplot as plt

def ejercicio1():
    arr = np.random.uniform(1, -1, 44100)

    plt.plot(arr)
    plt.show()

def ejercicio2():
    arr = np.random.uniform(1, -1, 44100)
    t = 44100 - 1
    signal = np.sin(2*np.pi)*arr

    plt.plot(arr, signal)
    plt.show()

#ejercicio1()
#ejercicio2()
#ejercicio3()
#ejercicio4()
#ejercicio5()
#ejercicio6()