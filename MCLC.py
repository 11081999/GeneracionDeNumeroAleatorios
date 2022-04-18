import math
import array


class MCLC:

    __x = []
    __mod = []
    __initial_value = []
    __result = []
    __num_randoms = 0
    __mod_w = 0
    __per = 0

    def __init__(self, num_randoms, x, mod, initial_value, mod_w):
        self.__num_randoms = num_randoms
        self.__x = x
        self.__mod = mod
        self.__initial_value = initial_value
        self.__mod_w = mod_w

    def calculNum(self, j, k):
        res = (self.__x[k]*self.__result[j-1][k]) % (self.__mod[k])
        return res

    def calculP(self):
        p = ((self.__mod[0]-1)*(self.__mod[1]-1))/2
        return p

    def calculateAllResults(self):
        for j in range(self.__num_randoms):
            if j == 0:
                self.__result.append(self.__initial_value)
                continue

            tabIntermediaire = []

            for k in range(2):
                tabIntermediaire.append(self.calculNum(j, k))
                w = (tabIntermediaire[0] - tabIntermediaire[1]) % self.__mod_w
                print("tab inter: ", str(tabIntermediaire))
                tabIntermediaire.append(w)

            self.__result.append(tabIntermediaire)
