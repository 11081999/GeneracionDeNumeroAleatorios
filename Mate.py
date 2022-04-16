# import library
import numpy as np
import math

#pip install --user scipy
from scipy.stats import ks_2samp
from scipy import stats


def chi():
    Xi = [22.9, 32.4, 26.2, 27.9, 28.9, 26.2, 28, 29.6, 28.4, 32,
          29, 32.1, 28.1, 27.9, 29.4, 29.6, 28.4, 27.8, 31.5, 23.2,
          26, 27, 31.9, 33.6, 25.5, 25.7, 30.1, 33, 28.6, 34.6,
          30.9, 30.9, 33.3, 33.5, 35.2, 37.8, 25.8, 28.1, 26.2, 29.3,
          28.7, 24.8, 28.5, 30.1, 24.3, 29.6, 33, 32.4, 32.1, 29.7]
    Xi = sorted(Xi)
    N= len(Xi)
    rango= Xi[N-1] - Xi[0]
    k= 4
    intervalo= rango / k
    alfa= 1 / (sum(Xi) / len(Xi))
    tabla = [[0 for i in range(6)] for j in range(k)]

    clase= [math.floor(Xi[0])]
    for i in range(0, k):
        clase.append(clase[i]+intervalo)

    for i in range(0, k):
        tabla[i][0] = (i+1)
        tabla[i][1] = clase[i]
        tabla[i][2] = clase[i+1]

        NoElements= 0
        for j in range(0, N):
            if (tabla[i][1] < Xi[j]) and (Xi[j] <= tabla[i][2]):
                NoElements+= 1
            tabla[i][3] = NoElements

        #Fei esperado
        tabla[i][4] = 50 / k

        tabla[i][5] = pow(tabla[i][3] - tabla[i][4], 2) / tabla[i][4]

    test = False
    res = [test, tabla]
    print(res)


chi()



def kolmogrov():
    Xi = [22.9, 32.4, 26.2, 27.9, 28.9, 26.2, 28, 29.6, 28.4, 32,
          29, 32.1, 28.1, 27.9, 29.4, 29.6, 28.4, 27.8, 31.5, 23.2,
          26, 27, 31.9, 33.6, 25.5, 25.7, 30.1, 33, 28.6, 34.6,
          30.9, 30.9, 33.3, 33.5, 35.2, 37.8, 25.8, 28.1, 26.2, 29.3,
          28.7, 24.8, 28.5, 30.1, 24.3, 29.6, 33, 32.4, 32.1, 29.7]
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

        XimimN.append(Xi[i] - ((i - 1) / N))
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

    #n = 50
    alpha= 0.05

    ks= 0.18841

    """
    def normal(a, b):
        return 1 / (a-b)

    ks = stats.kstest(Xi, cdf=normal, args=(weight1, mean1, stdv2, mean2, stdv2))
    print("sample1 p-value =", ks)
    """

    if D < ks:
        test= True
    else:
        test= False



    res = [test, tabla]

    print(res)

#def mcc(seed, numRadnom):
def mcc():
    seed = int(input("Seed: \n"))
    numRadnom= int(input("Number of Randoms: \n"))

    results = []
    seeds = [seed, 0]

    def splitSeed(n):

        seed = pow(n[0], 2)
        seed = str(seed)
        print(seed)

        if len(seed) < 8:
            while len(seed) < 8:
                seed = "0" + seed
                #print(seed)

        splitSeed = int(seed[2:6])
        ri = splitSeed / 10000

        return [splitSeed, ri]


    for i in range(numRadnom):
        seeds = splitSeed(seeds)
        results.append(seeds)

    return results