#Método de Euler
#y' - e^x = 0 y(0)=1 y(5)=?
# dy/dx = e^x

import math
import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return math.sin(x) + math.log(y)

def euler(y0,x,h,f):
    y = []
    y.append(y0)
    for i in range(1,len(x)):
        y.append( y[i-1] + h*f(x[i-1],y[i-1]) )
    return y
n = 20
a = 0.13
b = 0.14
h = abs(a-b)/(n-1)
print(h)
x = np.linspace(a,b,n)
print(x)
y = euler(1,x,h,f)

plt.plot(x,y,'g')
#plt.plot(x,[math.exp(xi) for xi in x],'b')
plt.grid()


0.0005263157894736846
[0.13       0.13052632 0.13105263 0.13157895 0.13210526 0.13263158
 0.13315789 0.13368421 0.13421053 0.13473684 0.13526316 0.13578947
 0.13631579 0.13684211 0.13736842 0.13789474 0.13842105 0.13894737
 0.13947368 0.14      ]
