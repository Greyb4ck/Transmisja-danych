import math
import numpy as np
import time 


real = []
imag = []


def DFT(x):
    #return (  x * math.exp**(-i * ( (2*math.pi * k * n)/N  ) ) )
	start_time = time.time()
	n = len(x)           

	for k in range(n):
			sumreal = 0
			sumimag = 0
			for t in range(n): 
				sumreal +=  x[t]*math.cos( (2*math.pi * k * t)/n  )
				sumimag +=  x[t]*math.sin( (-2*math.pi * k * t)/n  )
			real.append(sumreal)
			imag.append(sumimag)
	end_time = time.time()
	print("########################## DFT ##########################",'\n')
	print("Real numbers:\n",real)
	print("Imaginery numbers:\n",imag)
	print("Czas wykonania DFT: ", end_time - start_time)

list = []

for i in range(1 , 128):
	list.append(2**i)


DFT(list)

start_timeFFT = time.time() 
print('\n',"########################## FFT ##########################",'\n',np.fft.fft(list))
end_timeFFT = time.time()

print("Czas wykonania FFT: ", end_timeFFT - start_timeFFT)