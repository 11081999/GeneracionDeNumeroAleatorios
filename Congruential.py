
class Congruential:

    __a = None
    __c = None
    __current_seed = None
    __initial_seed = None
    __m = None
    __num_randoms = None
    __results_list = []

    def __init__(self, initial_seed, a, c, m, num_randoms):
        self.__a = a
        self.__c = c
        self.__initial_seed = initial_seed
        self.__current_seed = self.__initial_seed
        self.__m = m
        self.__num_randoms = num_randoms

    def getResultsList(self):
        self.__calculateCongruential()
        return self.__results_list

    def __calculateCongruential(self):
        for i in range(self.__num_randoms):
            result = []
            result = result + [i+1, self.__current_seed]
            self.__calculateCongruentialRow(result)
            self.__results_list.append(result)

    def __calculateCongruentialRow(self,  result):
        rand_num = (self.__a * self.__current_seed + self.__c) % self.__m
        result.append(rand_num)
        ri = rand_num / self.__m
        self.__current_seed = rand_num
        result.append(ri)
