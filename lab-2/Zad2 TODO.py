import math
import numpy as np
import time 
import matplotlib.pyplot as plt

Tc = 1
fs = 2000
N = fs*Tc

real = []
imag = []


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
	print('dft')
	#print("Real numbers:\n",real)
	#print("Imaginery numbers:\n",imag)
	return[real , imag]


list = []

for i in range(0 , N):
	z = i/fs
	list.append(math.sin(2*math.pi * 450 * z))


result = []

dft = DFT(list)
for i in range(0,len(list)):

	
	result.append(math.sqrt(dft[0][i]**2 + dft[1][i]**2))


plt.plot(range(len(result)), result)
plt.show()

