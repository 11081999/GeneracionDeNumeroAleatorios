class LinearCongruential:
    _a = None
    _c = None
    _current_seed = None
    _initial_seed = None
    _m = None
    _num_randoms = None
    _results_list = []

    def __init__(self, initial_seed, a, c, m, num_randoms):
        self._a = a
        self._c = c
        self._initial_seed = initial_seed
        self._current_seed = self._initial_seed
        self._m = m
        self._num_randoms = num_randoms

    def _calculateLinealCongruential(self):
        for i in range(self._num_randoms):
            result = []
            result = result + [i+1, self._current_seed]
            self.__calculateLinealCongruentialRow(result)
            self._results_list.append(result)

    def __calculateLinealCongruentialRow(self,  result):
        rand_num = (self._a * self._current_seed + self._c) % self._m
        result.append(rand_num)
        ri = rand_num / self._m
        self._current_seed = rand_num
        result.append(ri)

    def getResultsList(self):
        self._calculateLinealCongruential()
        return self._results_list



