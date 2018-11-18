#Gauss- Seidel
#4x1 +x2 -x3 = 0
#2x1 + 5x2 +2x3 =3
#x1 + 2x2 +4x3 = 11

def getx1(x2,x3):
    return (x3-x2)/4

def getx2(x1,x):
    return (3-2*x3-2*x1)/5

def getx3(x1,x2):
    return (11-x1-2*x2)/4

x1 = 0
x2 = 0
x3 = 0
E = 0.01
for i in range(100):
    xi1 = getx1(x2,x3)
    xi2 = getx2(xi1,x3)
    xi3 = getx3(xi1,xi2)
    Ex1 = abs(x1-xi1)
    Ex2 = abs(x2-xi2)
    Ex3 = abs(x3-xi3)
    x1 = xi1
    x2 = xi2
    x3 = xi3
    if Ex1 < E and Ex2 < E and Ex3 < E:
        break
        
print ("La solución es:", x1, x2, x3)

La solución es: 0.9995586294555664 -0.9998283878173828 3.0000245365447995
