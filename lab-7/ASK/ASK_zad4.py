import math
import numpy as np
from matplotlib import pyplot as plt
import random

bina = []
bn = []
def string2bits(s=''):
    for x in s:
        bina.append(bin(ord(x))[2:])
    bits = ''
    for i in range(0,len(bina)):
        bits += bina[i]
    return [int(i) for i in str(bits)]
def ASK_koh(Valy,A,kim,h):
    sum = 0
    tim = 0
    cl = []
    p = []
    x_t = []
    for i in range(0,len(za)):
        
        #fal.append( (A * math.sin(2*math.pi * fn * (tb+math.pi) )))
        x_t.append( Valy[i] * Valy[i]) 
        sum += x_t[i]
        p.append(sum)
        tim += 1/fs
        if tim > kim:
            tim = 0
            sum = 0
    for i in range(0,len(p)):
        if p[i] > h:
            cl.append(0)
        else:
            cl.append(1)

    
    return p , x_t, cl #, tim_c
def PSK_koh(Valy,A,kim,W):
    sum = 0
    sum1 = 0
    tim = 0
    c_p = []
    p = []
    x_t = []
    for i in range(0,len(zp)):
        x_t.append(Valy[i] * A * math.sin(2 * math.pi * ((W + 1) / kim) * (i / fn)))
        sum += x_t[i]
        p.append(sum)
        tim += 1/fs
        if tim > kim:
            tim = 0
            sum = 0

    for i in range(0,len(p)):
        
        if p[i] < 0:
            c_p.append(1)
        else:
            c_p.append(0)

    return p , x_t, c_p

def FSK_koh(Valy,A,kim,W):
    sum = 0
    sum1 = 0
    tim = 0
    c_p = []
    p = []
    x_t = []
    x_t1 = []
    for i in range(0,len(zf)):
        x_t.append(Valy[i] * A * math.sin(2 * math.pi * ((W + 1) / kim) * tim))
        x_t1.append(Valy[i] * A * math.sin(2 * math.pi * ((W + 2) / kim) * tim))
        sum += x_t[i]
        sum1 += x_t1[i]
        p.append(-sum + sum1)
        tim += 1/fs
        if tim > kim:
            tim = 0
            sum = 0
            sum1 = 0
    for i in range(0,len(p)):
        
        if p[i] > 0:
            c_p.append(1)
        else:
            c_p.append(0)

    return p , x_t, c_p
def haming_coder_1511(code):
    table_words = np.array([[0, 0,0,1],
                            [0, 0,1,0],
                                        [0, 0,1,1],
                            [0, 1,0,0],
                                        [0, 1,0,1],
                                        [0, 1,1,0],
                                        [0, 1,1,1],
                            [1, 0,0,0],
                                        [1, 0,0,1],
                                        [1, 0,1,0],
                                        [1, 0,1,1],
                                        [1, 1,0,0],
                                        [1, 1,0,1],
                                        [1, 1,1,0],
                                        [1, 1,1,1]])

    #print(table_words)
    tablica_p = np.zeros((11,4))
    #print(tablica_p)
    #print(table_words[13][3])
    c=0
    for j in range(0,4):
        for i in range(0,15):
            #if i != 0:
            #   if i != 1:
            #        if i != 3:
            #            if i != 7: 
            if i != 0 and i != 1 and i != 3 and i != 7: 
                            tablica_p[c][j]=table_words[i][j]
                            c += 1
        c=0

    I_k=np.eye(11)
    G = np.hstack(( tablica_p ,I_k))
    
    c = np.dot(code, G)%2
    return c
def haming_decoder_1511(code):
    table_words = np.array([[0, 0,0,1],
                            [0, 0,1,0],
                                        [0, 0,1,1],
                            [0, 1,0,0],
                                        [0, 1,0,1],
                                        [0, 1,1,0],
                                        [0, 1,1,1],
                            [1, 0,0,0],
                                        [1, 0,0,1],
                                        [1, 0,1,0],
                                        [1, 0,1,1],
                                        [1, 1,0,0],
                                        [1, 1,0,1],
                                        [1, 1,1,0],
                                        [1, 1,1,1]])

    #print(table_words)
    tablica_p = np.zeros((11,4))
    #print(tablica_p)
    #print(table_words[13][3])
    c=0
    for j in range(0,4):
        for i in range(0,15):
            #if i != 0:
            #   if i != 1:
            #        if i != 3:
            #            if i != 7: 
            if i != 0 and i != 1 and i != 3 and i != 7: 
                            tablica_p[c][j]=table_words[i][j]
                            c += 1
        c=0


        #np.transpose(H)
        #np.transpose(tablica_p)
    I_nk=np.eye(4)
    H = np.hstack((I_nk, np.transpose(tablica_p) ))
    #print(code)
    s = np.dot(code, np.transpose(H)) % 2
    S = 0
    #flag = True

    S = int(s[0] * 1 + s[1] * 2 + s[2] * 4 + s[3] * 8)
    #print(S)
    if S > 0:
        code[S-1] = not code[S-1]
        S = int(s[0] * 1) + int(s[1] * 2) + int(s[2] * 4) + int(s[3] * 8)
        if S > 0:
            print("false")

    code = code[4:]    
    return code
def Tobit(fk,kim,t):
    tim = 0
    bit_0 = 0
    bit_1 = 0
    for i in range(0,len(fk)-1):
        tim += 1/fs
        if tim > kim:
            tim = 0
            if bit_0 > bit_1:
                bits_zad.append(0)
            else:
                bits_zad.append(1)
            bit_0 = 0
            bit_1 = 0
        if fk[i] == 0:
            bit_0 += 1
        else:
            bit_1 += 1
    if bit_0 > bit_1:
       bits_zad.append(0)
    else:
       bits_zad.append(1)   
    return bits_zad
def AddNoise(array, alpha):
    noise = np.random.normal(0, 30, len(array))
    new_arr = array[:]
    for i in range(len(array)):
        new_arr[i] = array[i] + noise[i] * alpha
    #if new_arr == array:
    #    print('fck u')
    return new_arr
def Beta_t(array, beta):
    for t in range(len(array)):
        array[t] = array[t] * math.e**(-beta)*t

    return array


s = "a"
c = []
error = 0

b = [0,0, 0, 1, 1, 0, 1, 1, 0, 0, 1]
#print(b)
b = haming_coder_1511(b)
#print(b)   
b = b.astype(int)
for i in range (len(b)):
    c.append(b[i])

b = c
Check_B = b
print('tutaj')
#
print(b)
#print(c)

#b = string2bits(s)
#print(b)
#Flag = True
#print(b)

#if len(b) != 11:
#    b=np.resize(b,(1,11))
#    print(b)



Alfa = []
BER = 0
BER_c = []
#################################
fal = []
p = []
BER_Z = []
zf = []
tc = 7
fs=8000
tb = tc / (len(b))
a1 = 1
a2 = 2
w = 2
fn = w / tb
fn1 = (w+1) / tb
fn2 = (w+2) / tb
n = round(tc*fs)
nb = round( n / len(b) )
c = []
c_p = []
tim_c = []
t = []
b_new = []
bits_zad = []
rand_gen = []
za = []
zp = []
zf = []
index = 0
dex = 0

def z_a(d,i):
    if d != 0:
        return a1 * math.sin(2*math.pi * fn * t[i])
    else:
        return a2 * math.sin(2*math.pi * fn * t[i])
def z_p(d,i):
    if d != 0:
        return math.sin(2*math.pi * fn * t[i])
    else:
        return math.sin(2*math.pi * fn * t[i] + math.pi)
def z_f(d,i):
    if d != 0:
        return math.sin(2*math.pi * fn1 * t[i])
    else:
        return math.sin(2*math.pi * fn2 * t[i])

######################################## Kanał Transmisyjny 


for i in b:
    for j in range(0,nb):
        t.append(index)
        #rand_gen.append(random.random())
        za.append(z_a(b[i],dex)  ) # white noise + random.random()
        zp.append(z_p(b[i],dex))
        zf.append(z_f(b[i],dex))
        dex += 1
        index += 1 / fs
Beta_c=[]

for Beta in range (0,10):
    number = Beta
    
    BER_Z.append([])
    Beta_c.append(Beta)

    for alfo in range (0,10):
        za_n = Beta_t(za,Beta*0.01)
        za_n = AddNoise(za_n,alfo*0.01)
        
        #za_n = AddNoise(za,0.9)
        #za_n = Beta_t(zf,9)
        print('Beta',alfo*0.1)

        #plt.title("ask_z")
        #plt.plot(t,za_n)
        #plt.show()

        #plt.title("fsk")
        #plt.plot(t,zp)
        #plt.show()


    
        piu , xxrt , citu  = ASK_koh(za_n,2,tb,2500)
        #piu , xxrt , citu  = ASK_koh(za_n,2,tb,1)
        #print(len(citu))

        #plt.title("ask")
        #plt.plot(t,citu)
        #plt.show()

        b_new = Tobit(citu,tb,t)

        print(b_new)
        print(Check_B)


        for i in range (0, len(b_new)):
            if b_new[i] != Check_B[i]:
                error += 1
                print("error")
        
    
        Alfa.append(alfo)
        BER = error/len(Check_B)
        BER_c.append(BER)
        za_n = []
        citu *= 0
        b_new *= 0
        error = 0
    print(Beta)
    BER_Z[Beta].append(BER)

print(BER_Z)
        #print(b_new)
    
print("out")
############################################

#plt.title("BER")
#plt.plot(Alfa,BER_c)
#plt.show()

plt.figure()
ax = plt.axes(projection='3d')
X,Y = np.meshgrid(Alfa, Beta_c)
Z = np.array(BER_Z)
ax.plot_surface(X, Y, Z, cmap='gist_earth', edgecolor='none')

plt.title("BER")

plt.show()

print("out")


#print(b)

b = haming_decoder_1511(b)
#print(b)

print(error)
