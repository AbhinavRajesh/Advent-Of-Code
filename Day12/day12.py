sin = {0:0, 90:1, 180:0, 270:-1}
cos = {0:1, 90:0, 180:-1, 270:0}

def turn1(prevDirection):
    if prevDirection == 'N':
        return 'E'
    elif prevDirection == 'S':
        return 'W'
    elif prevDirection == 'E':
        return 'S'
    else:
        return 'N'

def turn2(prevDirection):
    if prevDirection == 'N':
        return 'S'
    elif prevDirection == 'S':
        return 'N'
    elif prevDirection == 'E':
        return 'W'
    else:
        return 'E'

def turn3(prevDirection):
    if prevDirection == 'N':
        return 'W'
    elif prevDirection == 'S':
        return 'E'
    elif prevDirection == 'E':
        return 'N'
    else:
        return 'S'

def problem1(lines):
    north = 0
    east = 0
    prevDirection = 'E'
    for i in lines:
        direction = i[:1]
        amount = int(i[1:])
        if direction == 'N':
            north += amount
        elif direction == 'S':
            north -= amount
        elif direction == 'E':
            east += amount
        elif direction == 'W':
            east -= amount
        elif direction == 'F':
            if prevDirection == 'N':
                north += amount
            elif prevDirection == 'S':
                north -= amount
            elif prevDirection == 'E':
                east += amount
            else:
                east -= amount
        else:
            turnTimes = int(amount) / 90
            if direction == 'R':
                if turnTimes == 1:
                    prevDirection = turn1(prevDirection)
                elif turnTimes == 2:
                    prevDirection = turn2(prevDirection)
                elif turnTimes == 3:
                    prevDirection = turn3(prevDirection)       
            else:
                if turnTimes == 1:
                    prevDirection = turn3(prevDirection)
                elif turnTimes == 2:
                    prevDirection = turn2(prevDirection)
                elif turnTimes == 3:
                    prevDirection = turn1(prevDirection)
    
    print(f'Answer to Problem1: {abs(east) + abs(north)}')


def problem2(lines):
    weast = 10
    wnorth = 1
    east = 0
    north = 0
    for i in lines:
        action = i[:1]
        value = int(i[1:])
        if action == 'N':
            wnorth += value
        elif action == 'S':
            wnorth -= value
        elif action == 'E':
            weast += value
        elif action == 'W':
            weast -= value
        elif action == 'F':
            north += wnorth * value
            east += weast * value
        elif action == 'R':
            nwx = weast*cos[-value%360] - wnorth*sin[-value%360]
            nwy = weast*sin[-value%360] + wnorth*cos[-value%360]
            weast = nwx
            wnorth = nwy
        else:
            nwx = weast*cos[value%360] - wnorth*sin[value%360]
            nwy = weast*sin[value%360] + wnorth*cos[value%360]
            weast = nwx
            wnorth = nwy
    print(f'Answer to Problem2: {abs(east) + abs(north)}')

def main():
    file = open('input.txt', 'r').read().split('\n')
    file.pop(-1)
    problem1(file)
    problem2(file)
    

main()