from LinearCongruential import LinearCongruential


class MixedCongruential(LinearCongruential):

    def __init__(self, initial_seed, a, c, m, num_randoms):
        self._a = a
        self._c = c
        self._initial_seed = initial_seed
        self._current_seed = self._initial_seed
        self._m = m
        self._num_randoms = num_randoms

    def __getFactor(self, num):
        factors = []
        for n in range(1, num):
            if num % n == 0:
                factors.append(n)
        return factors

    def __checkTheoremHullDobell(self):
        c_factors = self.__getFactor(self._c)
        m_factors = self.__getFactor(self._m)
        if not (max(self.__commonElements(c_factors, m_factors)) == 1):
            return False
        condition_2 = False
        m_prime_factors = self.__getPrimes(m_factors)
        print(m_prime_factors)
        for n in m_prime_factors:
            if (self._a - 1) % n == 0:
                condition_2 = True
                break
        if not condition_2:
            return False
        if self._m % 4 == 0:
            if (self._a - 1) % 4 == 0:
                return True
            return False
        return False

    def getResultsList(self):
        self._resetVariables()
        if self.__checkTheoremHullDobell():
            self._calculateLinealCongruential()
            return self._results_list
        return False

    def __commonElements(self, arr1, arr2):
        common = [value for value in arr1 if value in arr2]
        return common

    def __isPrime(self, num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False;
        return True

    def __getPrimes(self, factors):
        prime_nums = []
        for n in factors:
            if self.__isPrime(n):
                prime_nums.append(n)
        return prime_nums





