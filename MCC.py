import math

seed = int(input("Seed: \n"))
numRadnom= int(input("Number of Randoms: \n"))

results = []
seeds = [seed, 0]

def splitSeed(n):

    seed = pow(n[0], 2)
    seed = str(seed)
    print(seed)

    if len(seed) < 8:
        while len(seed) < 8:
            seed = "0" + seed
            #print(seed)

    splitSeed = int(seed[2:6])
    ri = splitSeed / 10000

    return [splitSeed, ri]


for i in range(numRadnom):

    seeds = splitSeed(seeds)

    results.append(seeds)

print(results)