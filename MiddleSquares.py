class MiddleSquares:
    __current_seed = None
    __initial_seed = None
    __num_randoms = None
    __results_list = []

    def __init__(self, initial_seed, num_randoms):
        self.__initial_seed = initial_seed
        self.__current_seed = self.__initial_seed
        self.__num_randoms = num_randoms

    def getResultsList(self):
        self.__calculateMiddleSquares()
        return self.__results_list

    def __calculateMiddleSquares(self):
        for i in range(self.__num_randoms):
            result = []
            result = result + [i+1, self.__current_seed]
            self.__calculateMiddSquaresRow(result)
            self.__results_list.append(result)

    def __calculateMiddSquaresRow(self, result):
        generator = pow(self.__current_seed, 2)

        self.__current_seed = self.__splitSeed(str(generator), result)
        result.append(self.__current_seed)
        ri = self.__current_seed / 10000
        result.append(ri)

    def __splitSeed(self, seed, result):
        if len(seed) < 8:
            while len(seed) < 8:
                #print("Seed: " + str(seed))
                seed = "0" + seed
        split_seed = int(seed[2:6])
        print("Seed: " + str(seed))
        result.append(seed)
        return split_seed