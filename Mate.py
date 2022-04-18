# import library
#import numpy as np
#pip install --user scipy
#from scipy.stats import ks_2samp
#from scipy import stats
#import statsmodels.api as sm
#from scipy.stats import chi2_contingency
#from scipy import stats
#from scipy.stats import chisquare

import math
from scipy.stats import ksone

def chi(Xi):
    """
    Xi = [22.9, 32.4, 26.2, 27.9, 28.9, 26.2, 28, 29.6, 28.4, 32,
          29, 32.1, 28.1, 27.9, 29.4, 29.6, 28.4, 27.8, 31.5, 23.2,
          26, 27, 31.9, 33.6, 25.5, 25.7, 30.1, 33, 28.6, 34.6,
          30.9, 30.9, 33.3, 33.5, 35.2, 37.8, 25.8, 28.1, 26.2, 29.3,
          28.7, 24.8, 28.5, 30.1, 24.3, 29.6, 33, 32.4, 32.1, 29.7]


    Xi = [8.223, 2.230, 2.920, 0.761, 1.064, 0.836, 3.810, 0.968, 4.490,
          0.186, 2.634, 1.624, 0.333, 1.514, 2.782, 4.778, 1.507, 4.025,
          1.064, 3.246, 0.406, 2.343, 0.538, 5.088, 5.587, 0.517, 1.458,
          0.234, 1.401, 0.685, 2.330, 0.774, 3.323, 0.294, 1.725, 2.563,
          0.023, 3.334, 3.491, 1.267, 0.511, 0.225, 2.325, 2.921, 1.702,
          6.426, 3.214, 7.514, 0.334, 1.849]
    """

    #Xi = [0.05, 0.14, 0.44, 0.81, 0.93]
    Xi = sorted(Xi)

    #print(Xi)

    N= len(Xi)
    rango= Xi[N-1] - Xi[0]
    k= math.floor(1 + 3.322*math.log10(N))
    intervalo= rango / k

    #print("N: " + str(N))
    #print("rango: " + str(rango))
    #print("K: " + str(k))
    #print("intervalo: " + str(intervalo))

    #print("________________")

    #En que parte empieza la calse(?)-----!
    clase= [Xi[0]]
    for i in range(0, k):
        clase.append(clase[i]+intervalo)

    tableClass = [[0 for i in range(3)] for j in range(k)]
    for i in range(0, k):
        tableClass[i][0] = clase[i]
        tableClass[i][1] = clase[i+1]

        NoElements= 0
        for j in range(0, N):
            if (tableClass[i][0] <= Xi[j]) and (Xi[j] <= tableClass[i][1]):
                #print(Xi[j])
                NoElements+= 1
        tableClass[i][2] = NoElements

    #print(tableClass)
    #print("________________")

    loop = True
    z= 0
    while loop:

        #print("__________")
        #print(z, tableClass[z][0], tableClass[z][1], tableClass[z][2])

        if tableClass[z][2] < 5:
            if z < len(tableClass)-1:
                # Limite inferior
                tableClass[z + 1][0] = tableClass[z][0]
                # Valor
                tableClass[z + 1][2] += tableClass[z][2]
            else:
                # Limitesuperior
                tableClass[z - 1][1] = tableClass[z][1]
                # Valor
                tableClass[z - 1][2] += tableClass[z][2]

            tableClass.pop(z)
            z= 0

        if z == len(tableClass)-1:
            loop = False
        z += 1

    #print("________________")
    #print(tableClass)
    k = len(tableClass)

    tabla = [[0 for i in range(7)] for j in range(k)]
    for i in range(0, k):

        #Index
        tabla[i][0] = (i+1)
        #limite Inferior
        tabla[i][1] = tableClass[i][0]
        #LimiteSuperior
        tabla[i][2] = tableClass[i][1]
        #Numero de elementos
        tabla[i][3] = tableClass[i][2]
        #Probabilidad
        tabla[i][4] = (tabla[i][2] - tabla[i][1]) / (Xi[N-1] - Xi[0])
        #Fe esperado
        tabla[i][5] = tabla[i][4] * N
        #(Fo - Fe)^2 / Fe
        tabla[i][6] = pow(tabla[i][3] - tabla[i][5], 2) / tabla[i][5]

    #print("________________")
    #print(tabla)
    #print(len(tabla))
    sumRes= [0, 0, 0, 0]


    for i in range(3, 7):
        column = i
        sumRes[i-3]= sum(row[column] for row in tabla)

    #print(sumRes)

    pp = 7.81

    if sumRes[3] < pp:
        test = True
    else:
        test = False

    res = [test, tabla]
    print("CHI SQR: "+ str(res[1]))
    return res

def ks_critical_value(n_trials, alpha):
    return ksone.ppf(1 - alpha / 2, n_trials)

def kolmogrov(Xi):
    """
    Xi = [22.9, 32.4, 26.2, 27.9, 28.9, 26.2, 28, 29.6, 28.4, 32,
           29, 32.1, 28.1, 27.9, 29.4, 29.6, 28.4, 27.8, 31.5, 23.2,
           26, 27, 31.9, 33.6, 25.5, 25.7, 30.1, 33, 28.6, 34.6,
           30.9, 30.9, 33.3, 33.5, 35.2, 37.8, 25.8, 28.1, 26.2, 29.3,
           28.7, 24.8, 28.5, 30.1, 24.3, 29.6, 33, 32.4, 32.1, 29.7]

    """
    #Xi = [0.05, 0.14, 0.44, 0.81, 0.93]
    a= 0.05
    Xi = sorted(Xi)
    N= len(Xi)
    IN= []
    INxi= []
    XimimN = []

    tabla= [[0 for i in range(5)] for j in range(N)]

    for i in range(0, N):
        #print("ITERATION " + str(i + 1))
        #print("Xi "+ str(Xi[i]))

        IN.append((i+1) / N)
        #print("i/N : " + str(IN[i]))

        INxi.append(abs(Xi[i] - IN[i]))
        #print("INxi : " + str(INxi[i]))

        XimimN.append(abs(Xi[i] - (((i+1) - 1) / N)))
        #print("Xi : " + str(Xi[i]))
        #print("i : " + str(i))
        #print("N : " + str(N))
        #print("XimimN : " + str(XimimN[i]))

    for i in range(0, N):
        tabla[i][0] = (i+1)
        tabla[i][1] = Xi[i]
        tabla[i][2] = IN[i]
        tabla[i][3] = INxi[i]
        tabla[i][4] = XimimN[i]

    Dp= max(INxi)
    Dm= max(XimimN)
    D= max([Dp, Dm])

    #print("D+ : " + str(Dp))
    #print("D- : " + str(Dm))
    #print("D : " + str(D))

    ks= ks_critical_value(N, a)

    if D < ks:
        test= True
    else:
        test= False

    res = [test, tabla]
    print("KOLMOGROV SQR: "+ str(res[1]))
    return res