import math
import matplotlib.pyplot as plt

#
Tc= 2 #czas trwania sygnału 
fs = 80 #czestotliwosc próbkowania
N = Tc * fs #liczba próbek 
fi = 1


#Zadanie 2
#Wybrana funkcja nr 2

def f_x(x):
    return math.sin(2*math.pi * fs * Tc * math.cos(3*math.pi * Tc) + Tc * fi)

def f_y(x):
    return ( f_x(Tc) * Tc**3)/3

def f_z(x):
    return 1.92 * (math.cos(3 * math.pi * Tc/2) + math.cos(f_y(Tc)**2)/(8 * f_x(Tc) + 3) * Tc )

def f_v(x):
    return (f_y(Tc) * f_z(Tc)/ (f_x(Tc) + 2 )  * math.cos(7.2 * math.pi * Tc) + math.sin(math.pi * Tc**2))



prop=[]
fun_y=[]
fun_z=[]
fun_v=[]


for i in range(0, N):
    Tc = i/fs

    prop.append(i)
    fun_y.append(f_y(Tc))
    fun_z.append(f_z(Tc))
    fun_v.append(f_v(Tc))



plt.plot(prop, fun_y)
plt.show()

plt.plot(prop, fun_z)
plt.show()

plt.plot(prop, fun_v)
plt.show()