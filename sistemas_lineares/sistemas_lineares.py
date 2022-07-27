
import numpy as np
import copy
#matriz = np.array([[1,0,0,0,1],[0,1,0,0,1],[0,0,1,0,1],[0,0,2,2,1]],dtype = 'f')
#matriz = np.array([[2,4,6,1],[1,3,5,0],[7,11,13,1]],dtype = 'f')
matriz = np.array([[1,0,0,1],[0,0,1,3],[0,2,0,2]],dtype = 'f')

for i in range(len(matriz)) :


    if matriz[i][i] == 0 :

        aux = copy.deepcopy(matriz[i])

        matriz[i] = matriz[i+1]

        matriz[i+1] = aux

        matriz[i] = matriz[i]/matriz[i][i]



    else:
        matriz[i] = matriz[i]/matriz[i][i]




    for j in range(len(matriz)):
        if i == j :
            continue
        else:
            matriz[j] = matriz[j] - matriz[j][i] * matriz[i]


if str(matriz[0][0]) == 'nan':
    print('matriz singular')
else :
    print(matriz)
