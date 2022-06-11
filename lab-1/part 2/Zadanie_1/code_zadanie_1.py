import math
import matplotlib.pyplot as plt

#
Tc= 2 #czas trwania sygnału 
fs = 80 #czestotliwosc próbkowania
N = Tc * fs #liczba próbek 
fi = 1


#Zadanie 1
#Wybrana funkcja nr 5

def f(x):
    return math.sin(2*math.pi * fs * Tc * math.cos(3*math.pi * Tc) + Tc * fi)

x=[]
y=[]


for i in range(0, N):
    Tc = i/fs

    x.append(Tc)
    y.append(f(Tc))

plt.plot(x, y)
plt.show()
