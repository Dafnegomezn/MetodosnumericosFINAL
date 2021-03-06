#2x1 + 4x2 -x3 = -5
#x1 + x2 -3x3 = -9
#4x1 + x2 +2x3 = 9

def createMatriz(m,n,v):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
           C[i].append(v)
    return C

U = createMatriz(3,3,0)
U[0] = [2,4,-1]
U[1] = [1,1,-3]
U[2] = [4,1,2]

L = createMatriz(3,3,0)
L[0] = [1,0,0]
L[1] = [0,1,0]
L[2] = [0,0,1]

C = createMatriz(3,1,0)
C[0] = [-5]
C[1] = [-9]
C[2] = [9]

for i in range(3):
    if U[i][i] == 0:
        print("La matriz no tiene LU")
#Si algun elemento de toda la diagonal es 0, no se puede realizar con LU
        break
    for j in range(i+1,3):
        c = -1*U[j][i]/U[i][i]
        L[j][i] = -1*c
        for k in range(3):
            U[j][k] += c*U[i][k]
print(U)
print(L)

# LZ = C
Z = createMatriz(3,1,0)
for i in range(3):
    Z[i][0] = C[i][0]
    for j in range(3):
        if i == j:
            break
        Z[i][0] -= L[i][j]*Z[j][0]
print(Z)

#UB = Z 
B = createMatriz(3,1,0)
for i in range(2,-1,-1):
    B[i][0] = Z[i][0]
    for j in range(2,-1,-1):
        if i == j:
            break
        B[i][0] -= U[i][j] * B[j][0]
    B[i][0] = B[i][0]/U[i][i]
print(B)

[[2, 4, -1], [0.0, -1.0, -2.5], [0.0, 0.0, 21.5]]
[[1, 0, 0], [0.5, 1, 0], [2.0, 7.0, 1]]
[[-5], [-6.5], [64.5]]
[[1.0], [-1.0], [3.0]]
