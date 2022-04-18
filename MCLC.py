import math
import array
from operator import mod

X = []
MOD = []
firstValue = []
RESULT = []
numReglas = 2
numRandom = 0

while numReglas < 2:
    numReglas = int(input("num reglas: \n"))
    numRandom = int(input("num random: \n"))


def calculNum(j, k, X, MOD, RESULT):
    res = (X[k]*RESULT[j-1][k]) % (MOD[k])
    return res


def mclcInit(numReglas, numRandom):

    # init reglas y value
    print("number of rules:", numReglas, "\n")
    print("number of random:", numRandom, "\n")

    print("init first rule:\n")
    for i in range(numReglas):

        x = int(input("x : \n"))
        mod = int(input("mod : \n"))
        firstRandom = int(input("firstRandom: \n"))
        X.append(x)
        MOD.append(mod)
        firstValue.append(firstRandom)
        print("next rule:\n")

    mclcAlgo(numReglas, numRandom, X, MOD, firstValue)


def mclcAlgo(numReglas, numRandom, X, MOD, firstValue):

    for j in range(numRandom):
        if j == 0:
            RESULT.append(firstValue)  # init tab result
            continue

        tabIntermediaire = []

        for k in range(numReglas):
            tabIntermediaire.append(calculNum(j, k, X, MOD, RESULT))

        RESULT.append(tabIntermediaire)


mclcInit(numReglas, numRandom)
print("RESULT FINAL", str(RESULT))
