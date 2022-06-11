import math
import matplotlib.pyplot as plt

#Zadanie 3 funkcja 6
Tc= 10 #czas trwania sygnału 
fs = 8000 #czestotliwosc próbkowania
N = Tc * fs #liczba próbek 
fi = 1

def f_x(x):
    return math.sin(2*math.pi * fs * Tc * math.cos(3*math.pi * Tc) + Tc * fi)

def f_y(x):
    return (-Tc/2) * math.sin(20*Tc**3 - 18*Tc**2)

def f_z(x):
    return math.cos(5* math.pi * Tc) * math.sin(12 * math.pi * Tc**2)

def f_v(x):
    return (Tc - 3 / 3) * math.sin((12 - Tc)* math.pi * Tc**2)


prop=[]
fun_y=[]


for i in range(0, N):
    Tc = i/fs

    if Tc >=0 and Tc<1.8:
        fun_y.append(f_y(Tc))
        prop.append(Tc)

    if Tc >=1.8 and Tc<3:
        fun_y.append(f_z(Tc))
        prop.append(Tc)

    if Tc >=3 and Tc<4.5:
        fun_y.append(f_v(Tc))
        prop.append(Tc)



plt.plot(prop, fun_y)
plt.show()
