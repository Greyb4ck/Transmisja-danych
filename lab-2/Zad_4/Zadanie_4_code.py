import math
import numpy as np
import time 


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
        #retkom.append((sumreal , sumimag))
    print('dft')
    #print("Real numbers:\n",real)
    #print("Imaginery numbers:\n",imag)
    return[real , imag]



#zadanie 1

##########################################################


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




#zadanie 2

##########################################################

#Tc= 2 #czas trwania sygnału 
#fs = 80 #czestotliwosc próbkowania
#N = Tc * fs #liczba próbek 
#fi = 1


#Zadanie 2
#Wybrana funkcja nr 2

#def f_x(x):
#    return math.sin(2*math.pi * fs * Tc * math.cos(3*math.pi * Tc) + Tc * fi)

#def f_y(x):
#    return ( f_x(Tc) * Tc**3)/3

#def f_z(x):
#    return 1.92 * (math.cos(3 * math.pi * Tc/2) + math.cos(f_y(Tc)**2)/(8 * f_x(Tc) + 3) * Tc )

#def f_v(x):
#    return (f_y(Tc) * f_z(Tc)/ (f_x(Tc) + 2 )  * math.cos(7.2 * math.pi * Tc) + math.sin(math.pi * Tc**2))



#prop=[]
#fun_y=[]
#fun_z=[]
#fun_v=[]


#for i in range(0, N):
#    Tc = i/fs

#    prop.append(i)
#    fun_y.append(f_y(Tc))
#    fun_z.append(f_z(Tc))
#    fun_v.append(f_v(Tc))


#zadanie 3

##########################################################


#Tc= 1 #czas trwania sygnału 
#fs = 2000 #czestotliwosc próbkowania
#N = Tc * fs #liczba próbek 
#fi = 1

#def f_x(x):
#    return math.sin(2*math.pi * fs * Tc * math.cos(3*math.pi * Tc) + Tc * fi)

#def f_y(x):
#    return (-Tc/2) * math.sin(20*Tc**3 - 18*Tc**2)

#def f_z(x):
#    return math.cos(5* math.pi * Tc) * math.sin(12 * math.pi * Tc**2)

#def f_v(x):
#    return (Tc - 3 / 3) * math.sin((12 - Tc)* math.pi * Tc**2)


#prop=[]
#fun_y=[]


#for i in range(0, N):
#    Tc = i/fs

#    if Tc >=0 and Tc<1.8:
#        fun_y.append(f_y(Tc))
#        prop.append(Tc)

#    if Tc >=1.8 and Tc<3:
#        fun_y.append(f_z(Tc))
#        prop.append(Tc)

#    if Tc >=3 and Tc<4.5:
#        fun_y.append(f_v(Tc))
#        prop.append(Tc)


##########################################################

#zadanie 4

##########################################################
#Tc= 1 #czas trwania sygnału 
#fs = 2000 #czestotliwosc próbkowania
#N = Tc * fs #liczba próbek 
#fi = 1
#h1 = 2
#h2 = 4
#h3 = 8
##Zadanie 4
##Wybrana funkcja nr 10

#def b_k(h):
#    return ( math.sin(math.pi * Tc * ( h**2 * math.sin(h))) ) / ( 7 * h )

#def b_1(h):
#    sum_b1 = 0
#    for k in range(1 , h1+1):
#       b1 = b_k(k)
#       sum_b1 += b1
    
#    return  sum_b1


#def b_2(h):
#    sum_b2 = 0
#    for k in range(1 , h2+1):
#       b2 = b_k(k)
#       sum_b2 += b2
    
#    return  sum_b2


#def b_3(h):
#    sum_b3 = 0
#    for k in range(1 , h3+1):
#       b3 = b_k(k)
#       sum_b3 += b3
    
#    return  sum_b3



#prop_1=[]
#prop_2=[]
#prop_3=[]
#fun_b1=[]
#fun_b2=[]
#fun_b3=[]


#for i in range(0, N+1):
#    Tc = i/fs

#    fun_b1.append(b_1(Tc))
#    prop_1.append(Tc)


#    fun_b2.append(b_2(Tc))
#    prop_2.append(Tc)

#    fun_b3.append(b_3(Tc))
#    prop_3.append(Tc)

#########################################################




# czasy dla zad 4

#start_time = time.time()
#b1_forT=DFT(fun_b1)
#b2_forT=DFT(fun_b2)
#b3_forT=DFT(fun_b3)
#end_time = time.time()
#print("Czas wykonania DFT: ", end_time - start_time)

#start_timeFFT = time.time() 
#print('\n',"########################## FFT ##########################",'\n',np.fft.fft(fun_b1))
#print('\n',"########################## FFT ##########################",'\n',np.fft.fft(fun_b2))
#print('\n',"########################## FFT ##########################",'\n',np.fft.fft(fun_b3))
#end_timeFFT = time.time()

#print("Czas wykonania FFT: ", end_timeFFT - start_timeFFT)


# czasy dla zad 3

#start_time = time.time()
#b1_forT=DFT(fun_y)
#end_time = time.time()
#print("Czas wykonania DFT: ", end_time - start_time)

#start_timeFFT = time.time() 
#print('\n',"########################## FFT ##########################",'\n',np.fft.fft(fun_y))

#end_timeFFT = time.time()

#print("Czas wykonania FFT: ", end_timeFFT - start_timeFFT)




# czasy dla zad 2


#start_time = time.time()
#b1_forT=DFT(fun_y)
#b2_forT=DFT(fun_z)
#b3_forT=DFT(fun_v)
#end_time = time.time()
#print("Czas wykonania DFT: ", end_time - start_time)

#start_timeFFT = time.time() 
#print('\n',"########################## FFT ##########################",'\n',np.fft.fft(fun_y))
#print('\n',"########################## FFT ##########################",'\n',np.fft.fft(fun_z))
#print('\n',"########################## FFT ##########################",'\n',np.fft.fft(fun_v))
#end_timeFFT = time.time()

#print("Czas wykonania FFT: ", end_timeFFT - start_timeFFT)

# czasy dla zad 1

start_time = time.time()
b1_forT=DFT(y)
end_time = time.time()
print("Czas wykonania DFT: ", end_time - start_time)

start_timeFFT = time.time() 
print('\n',"########################## FFT ##########################",'\n',np.fft.fft(y))

end_timeFFT = time.time()

print("Czas wykonania FFT: ", end_timeFFT - start_timeFFT)