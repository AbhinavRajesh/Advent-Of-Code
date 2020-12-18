def getNeighbour(current, point):
    number = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx != '0' or dy != 0 or dz != 0:
                    if [point[0] + dx, point[1] + dy, point[2] + dz] in current:
                        number += 1 
    return number

def getActivePoints(L, fourD=False):
    current = set()
    for y, l in enumerate(L):
        for x, ch in enumerate(l):
            if ch == '#':
                if not fourD:
                    current.add((x, y, 0))
                else:
                    current.add((x, y, 0, 0))
    return current

def problem1(L):
    current = getActivePoints(L)
    for r in range(6):
        new_current = set()
        for x in range(-10 - r, 10 + r):
            for y in range(-10 - r, 10 + r):
                for z in range(-2 - r, 2 + r):
                    nbr = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            for dz in [-1, 0, 1]:
                                if dx != 0 or dy != 0 or dz != 0:
                                    if (x + dx, y + dy, z + dz) in current:
                                        nbr += 1
                    if (x, y, z) not in current and nbr == 3:
                        new_current.add((x, y, z))
                    if (x, y, z) in current and nbr in [2, 3]:
                        new_current.add((x, y ,z))
        current = new_current
    print(f'Answer to Problem1: {len(current)}')

def problem2(L):
    current = getActivePoints(L, True)
    for r in range(6):
        new_current = set()
        for x in range(-10 - r, 10 + r):
            for y in range(-10 - r, 10 + r):
                for z in range(-2 - r, 2 + r):
                    for w in range(-2 - r, 2 + r):
                        nbr = 0
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                for dz in [-1, 0, 1]:
                                    for dw in [-1, 0, 1]:
                                        if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                                            if (x + dx, y + dy, z + dz, w + dw) in current:
                                                nbr += 1
                        if (x, y, z ,w) not in current and nbr == 3:
                            new_current.add((x, y, z, w))
                        if (x, y, z, w) in current and nbr in [2, 3]:
                            new_current.add((x, y ,z, w))
        current = new_current
    print(f'Answer to Problem2: {len(current)}')


def main():
    L = open('input.txt', 'r').read().splitlines()
    problem1(L)
    problem2(L)

main()



    #     new_actives = []
    #     for point in current:
    #         n = getNeighbour(current, point)
    #         if n in [2, 3]:
    #             future_repeat.append(point)
    #         for dx in range(-1, 2):
    #             for dy in range(-1, 2):
    #                 for dz in range(-1, 2):
    #                     if dx != 0 or dy != 0 or dz != 0:
    #                         offset = [point[0] + dx, point[1] + dy, point[2] + dz]
    #                         if offset not in current:
    #                             n = getNeighbour(current, offset)
    #                             if n == 3:
    #                                 future_repeat.append(offset)
    #     future = []
    #     [future.append(x) for x in future_repeat if x not in future]
    #     current = future
    # print(len(future))