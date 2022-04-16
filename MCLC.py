import math
import array


class MCLC:

    __x = []
    __mod = []
    __initial_value = []
    __result = []
    __num_reglas = 0
    __num_randoms = 0

    def __init__(self, num_randoms, num_reglas):
        self.__num_randoms = num_randoms
        self.__num_reglas = num_reglas

    def initValue(self):
        for i in range(self.__num_reglas):
            x = 0
            mod = 0

            x = int(input("x : \n"))
            mod = int(input("mod : \n"))
            intial_value = int(input("intial value: \n"))
            self.__x.append(x)
            self.__mod.append(mod)
            self.__initial_value.append(intial_value)
            print("next rule:\n")

    def calculNum(self, j, k):
        res = (self.__x[k]*self.__result[j-1][k]) % (self.__mod[k])
        return res

    def calculateAllResults(self):
        for j in range(self.__num_randoms):
            if j == 0:
                self.__result.append(self.__initial_value)  # init tab result
                continue

            tabIntermediaire = []

            for k in range(self.__num_reglas):
                tabIntermediaire.append(self.calculNum(j, k))

            self.__result.append(tabIntermediaire)
