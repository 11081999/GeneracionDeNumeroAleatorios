
class MultiplicativeCongruential:
    __a = None
    __m = None
    __current_seed = None
    __initial_seed = None
    __num_randoms = None
    __results_list = []

    def __init__(self, initial_seed, a, m, num_randoms):
        self.__a = a
        self.__initial_seed = initial_seed
        self.__current_seed = initial_seed
        self.__m = m
        self.__num_randoms = num_randoms

    def __checkConditions(self):
        if not (self.__initial_seed >= 0 and self.__a >= 0 and self.__m >= 0):
            return False
        if not (type(self.__initial_seed) == int and type(self.__a) == int and type(self.__m) == int):
            return False
        if not(self.__m > self.__a and self.__m > self.__initial_seed):
            return False
        return True

    def getResultsList(self):
        if self.__checkConditions():
            self.__calculateMultiplicativeCongruential()
            return self.__results_list
        return False

    def __calculateMultiplicativeCongruential(self):
        for i in range(self.__num_randoms):
            result = []
            rand = (self.__a * self.__current_seed ) % self.__m
            result = result + [i+1, self.__current_seed, rand]
            self.__results_list.append(result)
            self.__current_seed = rand




