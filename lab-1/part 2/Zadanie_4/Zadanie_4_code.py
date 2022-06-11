import math
import matplotlib.pyplot as plt

#
Tc= 1 #czas trwania sygnału 
fs = 22050 #czestotliwosc próbkowania
N = Tc * fs #liczba próbek 
fi = 1
h1 = 2
h2 = 4
h3 = 8
#Zadanie 4
#Wybrana funkcja nr 10

def b_k(h):
    return ( math.sin(math.pi * Tc * ( h**2 * math.sin(h))) ) / ( 7 * h )

def b_1(h):
    sum_b1 = 0
    for k in range(1 , h1+1):
       b1 = b_k(k)
       sum_b1 += b1
    
    return  sum_b1


def b_2(h):
    sum_b2 = 0
    for k in range(1 , h2+1):
       b2 = b_k(k)
       sum_b2 += b2
    
    return  sum_b2


def b_3(h):
    sum_b3 = 0
    for k in range(1 , h3+1):
       b3 = b_k(k)
       sum_b3 += b3
    
    return  sum_b3



prop_1=[]
prop_2=[]
prop_3=[]
fun_b1=[]
fun_b2=[]
fun_b3=[]


for i in range(0, N+1):
    Tc = i/fs

    fun_b1.append(b_1(Tc))
    prop_1.append(Tc)


    fun_b2.append(b_2(Tc))
    prop_2.append(Tc)

    fun_b3.append(b_3(Tc))
    prop_3.append(Tc)

    

    

plt.plot(prop_1, fun_b1)
plt.show()

plt.plot(prop_2, fun_b2)
plt.show()

plt.plot(prop_3, fun_b3)
plt.show()

