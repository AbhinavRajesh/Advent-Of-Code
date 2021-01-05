from collections import defaultdict
from itertools import permutations

def getPath(towns, locations):
    distance = 0
    for town1, town2 in zip(towns, towns[1:]):
        distance += locations[town1][town2]
    return distance

def main():
    file = open("input.txt").read().splitlines()
    locations = defaultdict(dict)
    for line in file:
        towns, distance = line.split(' = ')
        town1, town2 = towns.split(' to ')
        locations[town1][town2] = int(distance)
        locations[town2][town1] = int(distance)
    print(min(getPath(towns,locations) for towns in permutations(locations)))
    print(max(getPath(towns,locations) for towns in permutations(locations)))


main()
