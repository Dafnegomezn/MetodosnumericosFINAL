El sistema de ecuaciones de Newton-Raphson es un sistema no lineal en el que tengo 2 ecuaciones una se define por u(x,y) y otra por v(x,y), y se buscan los valores de x1 y y1, tengo los valores de x0, y0 y se hacen las operaciones de esta forma:
[x1 y1] = [x0 y0] - matriz inversa de [derivada parcial de u con x, derivada parcial de u con y][derivada parcial de v con x,        derivada parcial de v con y]* [u(x0,y0)][v(x0,y0]

