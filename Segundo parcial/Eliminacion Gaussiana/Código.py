#4x1 +x2 -x3 = 0
#2x1 + 5x2 +2x3 =3
#x1 + 2x2 +4x3 = 11
def createMatriz(m,n,v):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
           C[i].append(v)
    return C

MA = createMatriz(3,4,0)
MA[0] = [4,1,-1,0]
MA[1] = [2,5,2,3]
MA[2] = [1,2,4,11]

MAm = 3
MAn = 4
for i in range(MAm):
    pivote = MA[i][i]
    if pivote ==0: #intercambio renglones
        for j in range(i+1,MAm):
            pivote = MA[j][i]
            if pivote != 0:
                T = MA[i]
                MA[i] = MA[j]
                MA[j] = T
                break
    for k in range(MAn):
        MA[i][k]=(1/pivote)*MA[i][k]
    for j in range(i+1,MAm):
        c = -1*MA[j][i]
        T = createMatriz(1,MAn,0)
        for k in range(MAn):
            T[0][k] = c*MA[i][k]
        for k in range(MAn):
            MA[j][k] += T[0][k]
print("EG",MA)

B = createMatriz(3,1,0)
for i in range(MAm-1,-1,-1):
    B[i][0] = MA[i][MAn-1]
    for j in range(MAn-2,-1,-1):
        if i == j:
            break 
        B[i][0] -= MA[i][j] * B[j][0]
print(B)

EG [[1.0, 0.25, -0.25, 0.0], [0.0, 1.0, 0.5555555555555556, 0.6666666666666666], [0.0, 0.0, 1.0, 3.0000000000000004]]
[[1.0000000000000002], [-1.0000000000000004], [3.0000000000000004]]
