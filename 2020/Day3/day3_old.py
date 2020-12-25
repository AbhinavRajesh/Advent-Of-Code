def main():
    file = open('input.txt', 'r')
    s = file.read()
    l = s.split('\n')
    posX = 0
    posY = 0
    slope2Count = 0
    while True:
        if posX == 30:
            posX = -1
        elif posX == 29:
            posX = -2
        elif posX == 28:
            posX = -3
        posX += 3
        posY += 1
        if l[posY][posX] == '#':
            slope2Count += 1
        if posY == 322:
            break
    print(f'Problem 1 answer: {slope2Count}')
    slope1Count = 0
    slope3Count = 0
    slope4Count = 0
    slope5Count = 0
    posX = 0
    posY = 0
    while True:    
        if posX == 30:
            posX = -1
        posX += 1
        posY += 1
        if l[posY][posX] == '#':
            slope1Count += 1
        if posY == 322:
            break
    posX = 0
    posY = 0
    while True:    
        if posX == 30:
            posX = -1
        elif posX == 29:
            posX = -2
        elif posX == 28:
            posX = -3
        elif posX == 27:
            posX = -4
        elif posX == 26:
            posX = -5
        posX += 5
        posY += 1
        if l[posY][posX] == '#':
            slope3Count += 1
        if posY == 322:
            break
    posX = 0
    posY = 0
    while True:    
        if posX == 30:
            posX = -1
        elif posX == 29:
            posX = -2
        elif posX == 28:
            posX = -3
        elif posX == 27:
            posX = -4
        elif posX == 26:
            posX = -5
        elif posX == 25:
            posX = -6
        elif posX == 24:
            posX = -7
        posX += 7
        posY += 1
        if l[posY][posX] == '#':
            slope4Count += 1
        if posY == 322:
            break
    posX = 0
    posY = 0
    while True:    
        if posX == 30:
            posX = -1
        posX += 1
        posY += 2
        if l[posY][posX] == '#':
            slope5Count += 1
        if posY == 322:
            break
    print(f'Problem 2 Answer: {slope1Count * slope2Count * slope3Count * slope4Count * slope5Count}')


main()