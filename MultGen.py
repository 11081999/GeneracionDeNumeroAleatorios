import math
import array

class MultGen:
    __a = 0
    __MOD = 0
    __semilla = 0
    __resultRandom = []
    __resultRI = []
    __num_randoms = 0

    def __init__(self, num_randoms, semilla):
        self.__num_randoms = num_randoms
        self.__semilla = semilla

    def initValue(self):
        self.__a = int(input("a : \n"))
        self.__MOD = int(input("MOD : \n"))
        if self.__a < 0:
            self.initValue()
        if self.__MOD < 0 or self.__MOD <= self.__a or self.__MOD <= self.__semilla:
            self.initValue

    def calculateAllResults(self):
        for i in range(self.__num_randoms):
            self.__semilla = self.calculateOneResult()

    def calculateOneResult(self):
        random = 0
        randomRI = 0
        random = (self.__a*self.__semilla) % (self.__MOD)
        self.__resultRandom.append(random)

        randomRI = random / self.__MOD
        self.__resultRI.append(randomRI)

        return