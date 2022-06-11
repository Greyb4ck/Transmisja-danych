import math
from matplotlib import pyplot as plt

bina = []
bn = []
def string2bits(s=''):
    for x in s:
        bina.append(bin(ord(x))[2:])
    bits = ''
    for i in range(0,len(bina)):
        bits += bina[i]
    return [int(i) for i in str(bits)]

s = "Ob"

b = string2bits(s)
print(b)


x_t = []
x_t1 =[]
fal = []
p = []


tc = 7
fs=8000
tb = tc / (len(b))
a1 = 1
a2 = 2
w = 1
fn = w / tb
fn1 = (w+1) / tb
fn2 = (w+2) / tb
n = round(tc*fs)
nb = round( n / len(b) )
c = []
c_p = []
tim_c = []
t = []
bits_zad = []
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



for i in b:
    for j in range(0,nb):
        t.append(index)
        za.append(z_a(b[i],dex))
        zp.append(z_p(b[i],dex))
        zf.append(z_f(b[i],dex))
        dex += 1
        index += 1 / fs

def ASK_koh(Valx,Valy,A,kim,h):
    sum = 0
    tim = 0
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
            c.append(1)
        else:
            c.append(0)

    return p , x_t, c #, tim_c



def PSK_koh(Valy,A,kim,W):
    sum = 0
    sum1 = 0
    tim = 0

    for i in range(0,len(zp)):
        x_t.append(Valy[i] * A * math.sin(2 * math.pi * ((W + 1) / kim) * (i / fn)))
        sum += x_t[i]
        p.append(sum)
        tim += 1/fs
        if tim > kim:
            tim = 0
            sum = 0

    for i in range(0,len(p)):
        
        if p[i] > 0:
            c_p.append(1)
        else:
            c_p.append(0)

    return p , x_t, c_p


def FSK_koh(Valy,A,kim,W):
    sum = 0
    sum1 = 0
    tim = 0
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
               
def Tobit(fk,kim,t):
    tim = 0
    bit_0 = 0
    bit_1 = 0
    for i in range(0,len(fk)):
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
    print(bits_zad)



#piu , xxrt , citu  = ASK_koh(zf,za,2,tb,2500)


#plt.suptitle("PSK")

#plt.subplot(4,1,1)
#plt.plot(t, za)

#plt.subplot(4,1,2)
#plt.plot(t, xxrt)

#plt.subplot(4,1,3)
#plt.plot(t, piu)

#plt.subplot(4,1,4)
#plt.plot(t, citu)
#plt.show()

#plt.title("ask")
#plt.plot(t,citu)
#plt.show()

#Tobit(citu,tb,t)

#piu_PSK , xxrt_PSK , citu_PSK = PSK_koh(zp,2,tb,w)

#plt.suptitle("PSK")

#plt.subplot(4,1,1)
#plt.plot(t, zp)

#plt.subplot(4,1,2)
#plt.plot(t, xxrt_PSK)

#plt.subplot(4,1,3)
#plt.plot(t, piu_PSK)

#plt.subplot(4,1,4)
#plt.plot(t, citu_PSK)
#plt.show()

#plt.title("PSK")
#plt.plot(t,citu_PSK)
#plt.show()

#Tobit(citu_PSK,tb,t)

#piu_FSK , xxrt_FSK , citu_FSK = FSK_koh(zf,2,tb,w)

#plt.suptitle("FSK")

#plt.subplot(4,1,1)
#plt.plot(t, zp)

#plt.subplot(4,1,2)
#plt.plot(t, xxrt_FSK)

#plt.subplot(4,1,3)
#plt.plot(t, piu_FSK)

#plt.subplot(4,1,4)
#plt.plot(t, citu_FSK)
#plt.show()

#plt.title("FSK")
#plt.plot(t,citu_FSK)
#plt.show()

#Tobit(citu_FSK,tb,t)
