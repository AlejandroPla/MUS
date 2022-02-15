import numpy as np
import matplotlib.pyplot as plt
SRATE = 44100
BUF_SIZE = 1024

def ejercicio1():
    arr = np.random.uniform(1, -1, 44100)

    plt.plot(arr)
    plt.show()

def ejercicio2():
    size = 44100
    arr = np.linspace(0, size, size)
    t = 0
    for i in range(size - 1):
        arr[i] = np.sin(2*np.pi) * t
        t = t + 1
   
    plt.plot(arr)
    plt.xlabel('Angle [rad]')
    plt.ylabel('sin(x)')
    plt.axis('tight')
    plt.show()
    '''x = np.linspace(-np.pi, np.pi, 201)
    plt.plot(x, np.sin(x))
    plt.xlabel('Angle [rad]')
    plt.ylabel('sin(x)')
    plt.axis('tight')
    plt.show()'''

def dibujaOnda(muestra):
    x = np.linspace(0, len(muestra) / SRATE, num=len(muestra))
    y = muestra
    plt.plot(x, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Intensidad')
    plt.axis('tight')
    plt.show()

def osc(f, d:float, fase = 0):
    #calcular el eje x
    x = np.linspace(0, d, SRATE * d)
    lmbd = 1 / f
    # calcular el seno
    y = np.sin((2*np.pi * x) / lmbd + fase)
    return y

def square(f, d):
    # calcular el seno
    y = osc(f, d)
    # Cuadrado
    y = np.where(np.sign(y) >= 0, 1, -1)
    return y


def triangle(f, d):
    # Calcular el seno
    y = osc(f, d)

    # Triangulo
    y = 2 / np.pi * np.arcsin(y)
    return y

def saw(f, d):
    # Calcular el eje X 
    x = np.linspace(0, d, SRATE * d)
    lamda = 1 / f

    # Diente de sierra
    tanTerm = np.tan((2 * np.pi * x) / (2 * lamda))
    y = 2 / np.pi * np.arctan(tanTerm)
    return y

def ejercicio3():
    #muestra = osc(1, 1)
    #muestra = square(1, 1)
    #muestra = triangle(1, 1)
    muestra = saw(1, 1)
    dibujaOnda(muestra)

def vol(sample, factor):
    sample = sample * factor
    return sample

def modulaVol(sample, frec):
    sample = sample * frec
    return sample

def ejercicio4():
    muestra = osc(1, 1)
    frec = osc(1, 1)
    muestra = modulaVol(muestra, frec)
    dibujaOnda(muestra)

def fadeOut(sample, t):
    fadedSamples = (int)(len(sample) - SRATE * t)
    fadeLevels = np.flip(np.arange(0.0, 1.0, step= 1 / fadedSamples))
    sample[-fadedSamples:] *= fadeLevels
    return sample

def fadeIn(sample, t):
    fadedSamples = (int)(SRATE * t)
    fadeLevels = np.arange(0.0, 1.0, step= 1 / fadedSamples)
    sample[:fadedSamples] *= fadeLevels
    return sample

def ejercicio5():
    muestra = osc(1, 1)
    #muestra = fadeOut(muestra, 0.1)
    muestra = fadeIn(muestra, 0.58)
    dibujaOnda(muestra)

class Osc:
    def __init__(self, frec):
        self.frec = frec
        self.fase = 0
    
    def next(self):
        dur = (BUF_SIZE / SRATE)
        seno = osc(self.frec, dur, self.fase)
        self.fase += (BUF_SIZE / SRATE) * self.frec * 2 * np.pi
        return seno

def ejercicio6():
    oscilador = Osc(1)
    muestra = oscilador.next()
    for i in range(80):
        muestra = np.concatenate((muestra, oscilador.next()), axis=None)

    dibujaOnda(muestra)

#ejercicio1()
ejercicio2()
#ejercicio3()
#ejercicio4()
#ejercicio5()
#ejercicio6()