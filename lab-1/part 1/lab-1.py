import matplotlib.pyplot as plt

def f(x):
    return x*x
x=[]
 
for i in range(0,50):
    x.append(i/10)

y=[]

for i in range(0, len(x)):
    y.append(f(x[i]))

plt.plot(x, y)
plt.show()