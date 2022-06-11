import math
import numpy as np
import matplotlib.pyplot as plt

Tc = 1
fs = 8000
Fm = 10
Fn = 200
kA = 0.5
Kp = 0.4
Kf = 0.5
N = Tc * fs

def m_t(t):
	return math.sin(2*math.pi * Fm * t)

def z_A(t):
	return (kA * m_t(t) + 1) * math.cos(2*math.pi * Fn * t)

def z_P(t):
	return math.cos(2*math.pi * Fn * t + Kp * m_t(t))

def z_F(t):
	return math.cos(2*math.pi * Fn * t + Kf/Fm * m_t(t))

x = []
zA = []
zP = []
zF = []

for i in range(0, N):
	x.append(i)
	zA.append(z_A(i/fs))
	zP.append(z_P(i/fs))
	zF.append(z_F(i/fs))

plt.plot(x, zA)
plt.show()

plt.plot(x, zP)
plt.show()

plt.plot(x, zF)
plt.show()