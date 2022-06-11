import math
import numpy as np
import time 
import matplotlib.pyplot as plt

Tc = 1
fs = 2000
N = fs*Tc
fi = 1
h1 = 2
h2 = 4
h3 = 8


real = []
imag = []
retkom = []

def DFT(x):
    #return (  x * math.exp**(-i * ( (2*math.pi * k * n)/N  ) ) )
	n = len(x)           

	for k in range(n):
			sumreal = 0
			sumimag = 0
			for t in range(n): 
				sumreal +=  x[t]*math.cos( (2*math.pi * k * t)/n  )
				sumimag +=  x[t]*math.sin( (-2*math.pi * k * t)/n  )
			real.append(sumreal)
			imag.append(sumimag)
			retkom.append((sumreal , sumimag))
	print('dft')
	#print("Real numbers:\n",real)
	#print("Imaginery numbers:\n",imag)
	return[real , imag]


######################################### 4
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



dft_b1 = DFT(fun_b1)
dft_b2 = DFT(fun_b2)
dft_b3 = DFT(fun_b3)

##################################################### 4




result_b1 = []
result_b2 = []
result_b3 = []


for i in range(0,len(fun_b1)):

    result_b1.append(math.sqrt(dft_b1[0][i]**2 + dft_b1[1][i]**2))
    
for i in range(0,len(fun_b2)):
    result_b2.append(math.sqrt(dft_b2[0][i]**2 + dft_b2[1][i]**2))

for i in range(0,len(fun_b3)):
    result_b3.append(math.sqrt(dft_b3[0][i]**2 + dft_b3[1][i]**2))



plt.plot(range(len(result_b1)), result_b1)
plt.show()
plt.plot(range(len(result_b2)), result_b2)
plt.show()
plt.plot(range(len(result_b3)), result_b3)
plt.show()


result_dok_b1 = []
result_dok_b2 = []
result_dok_b3 = []
for i in range(round(len(fun_b1)/2)):
    result_dok_b1.append(10*math.log10(result_b1[i]))

for i in range(round(len(fun_b2)/2)):
    result_dok_b2.append(10*math.log10(result_b2[i]))

for i in range(round(len(fun_b3)/2)):
    result_dok_b3.append(10*math.log10(result_b3[i]))

freq_b1=[]
freq_b2=[]
freq_b3=[]

for i in range(round(len(fun_b1)/2)):
    freq_b1.append(i*(fs/N))

for i in range(round(len(fun_b2)/2)):
    freq_b2.append(i*(fs/N))


for i in range(round(len(fun_b3)/2)):
    freq_b3.append(i*(fs/N))


#plt.plot(freq_b1, result_dok_b1)
#plt.show()
#plt.plot(freq_b2, result_dok_b2)
#plt.show()
#plt.plot(freq_b3, result_dok_b3)
#plt.show()

