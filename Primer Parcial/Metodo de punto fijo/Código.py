def xnew(x):
    return (2*x**2 +3)/5
x0 = 0
x1 = 0
iteraciones = 0
for i in range(100):
    x1 = xnew(x0)
    if abs(x1-x0) < 0.001:
        break
    x0 = x1
    iteraciones += 1
    
print ("La raíz es %.5f"%x1)
print ("Usando %i iteraciones"%iteraciones)

La raíz es 0.99655
Usando 18 iteraciones
