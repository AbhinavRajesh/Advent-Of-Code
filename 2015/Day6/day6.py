def problem1(lines):
    # return lines
    lights = [[0 for x in range(1000)] for y in range(1000)]
    for line in lines:
        if line[1] == 'on':
            startx, starty = line[2].split(',')
            endx, endy = line[-1].split(',')
            for y in range(int(starty), int(endy) + 1):
                for x in range(int(startx), int(endx) + 1):
                    lights[x][y] = 1
        elif line[1] == 'off':
            startx, starty = line[2].split(',')
            endx, endy = line[-1].split(',')
            for y in range(int(starty), int(endy) + 1):
                for x in range(int(startx), int(endx) + 1):
                    lights[x][y] = 0
        else:
            startx, starty = line[1].split(',')
            endx, endy = line[-1].split(',')
            for y in range(int(starty), int(endy) + 1):
                for x in range(int(startx), int(endx) + 1):
                    lights[x][y] = 0 if lights[x][y] == 1 else 1
    count = 0
    for x in range(1000):
        for y in range(1000):
            if lights[x][y] == 1:
                count += 1
    return count

def problem2(lines):
    # return lines
    lights = [[0 for x in range(1000)] for y in range(1000)]
    for line in lines:
        if line[1] == 'on':
            startx, starty = line[2].split(',')
            endx, endy = line[-1].split(',')
            for y in range(int(starty), int(endy) + 1):
                for x in range(int(startx), int(endx) + 1):
                    lights[x][y] += 1
        elif line[1] == 'off':
            startx, starty = line[2].split(',')
            endx, endy = line[-1].split(',')
            for y in range(int(starty), int(endy) + 1):
                for x in range(int(startx), int(endx) + 1):
                    if lights[x][y] > 0:
                        lights[x][y] -= 1
        else:
            startx, starty = line[1].split(',')
            endx, endy = line[-1].split(',')
            for y in range(int(starty), int(endy) + 1):
                for x in range(int(startx), int(endx) + 1):
                    lights[x][y] += 2
    brightness = 0
    for x in range(1000):
        for y in range(1000):
            # if lights[x][y] > 0:
            brightness += lights[x][y]
    return brightness

def main():
    file = open('input.txt').read().splitlines()
    lines = [l.split() for l in file]
    print(problem1(lines))
    print(problem2(lines))
    # for x in range(0):
    #     print(x) 

main()