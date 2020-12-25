def readData():
    file = open('input.txt').read().splitlines()
    file = [l for x in file for l in x]
    return file

def problem1(lines):
    coords = [0, 0]
    drops = set()
    drops.add(tuple(coords))
    for l in lines:
        if l == '^':
            coords[1] += 1
        elif l == "<":
            coords[0] -= 1
        elif l == ">":
            coords[0] += 1
        else:
            coords[1] -= 1
        if tuple(coords) not in drops:
            drops.add(tuple(coords))
    return len(drops)

def problem2(data):
    santa = [0, 0]
    robo = [0, 0]
    drops = set()
    drops.add((0, 0))
    santaTurn = True
    for l in data:
        if santaTurn:
            if l == '^':
                santa[1] += 1
            elif l == "<":
                santa[0] -= 1
            elif l == ">":
                santa[0] += 1
            else:
                santa[1] -= 1
            if tuple(santa) not in drops:
                drops.add(tuple(santa))
            santaTurn = False
        else:
            if l == '^':
                robo[1] += 1
            elif l == "<":
                robo[0] -= 1
            elif l == ">":
                robo[0] += 1
            else:
                robo[1] -= 1
            if tuple(robo) not in drops:
                drops.add(tuple(robo))
            santaTurn = True
    return len(drops)

def main():
    data = readData()
    # test1 = ['^', 'v', '^', 'v', '^', 'v', '^', 'v', '^', 'v']
    # test2 = ['^', '>', 'v', '<']
    # print(problem1(test2))
    print(problem1(data))
    print(problem2(data))


main()