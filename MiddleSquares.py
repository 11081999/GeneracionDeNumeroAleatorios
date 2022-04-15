
class MiddleSquares:
    __current_seed = None
    __num_randoms = None
    __results_list = []
    __initial_seed = None

    def __init__(self, seed, num_randoms):
        self.__initial_seed = seed
        self.__current_seed = self.__initial_seed
        self.__num_randoms = num_randoms

    def getResultsList(self):
        self.__calculateMiddleSquares()
        return self.__results_list

    def __calculateMiddleSquares(self):
        for i in range(self.__num_randoms):
            result=[]
            result = result + [i+1, self.__current_seed]
            self.__calculateMiddSquaresRow(self.__current_seed, result)
            self.__results_list.append(result)


    def __calculateMiddSquaresRow(self, seed, result):
        generator = pow(seed, 2)
        result.append(generator)
        self.__current_seed = self.__splitSeed(str(generator))
        result.append(self.__current_seed)

        ri = self.__current_seed/ 10000
        result.append(ri)


    def __splitSeed(self, seed):
        if len(seed) < 8:
            while len(seed) < 8:
                seed = "0" + seed
                # print(seed)
        split_seed = int(seed[2:6])
        return split_seed
