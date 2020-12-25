def readData():
    file = open('input.txt').read().splitlines()
    file = [int(x) for x in file]
    return file[0], file[1]

def findLoop(doorPub):
    value = 1
    loop = 0
    while value != doorPub:
        value *= 7
        value %= 20201227
        loop += 1
    return loop 

def findKey(cardPub, loop):
    value = 1
    for _ in range(loop):
        value *= cardPub
        value %= 20201227
    return value
        


def part1(cardPub, doorPub):
    loop = findLoop(doorPub)
    return findKey(cardPub, loop)

def main():
    doorPub, cardPub = readData()
    print(f'Answer to Problem1: {part1(cardPub, doorPub)}')
    print('Answer To Problem2: Merry Christmas')

main()