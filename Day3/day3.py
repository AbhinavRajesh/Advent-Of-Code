
def slopeCount(l, addX, addY):
    count = 0
    posX = 0
    posY = 0
    while(posY < 322):
        posX += addX
        posX = posX % len(l[0])
        posY += addY
        if l[posY][posX] == '#':
            count +=1 
    return count


def main():
    file = open('input.txt', 'r')
    s = file.read()
    l = s.split('\n')
    print(f'Answer Of First Problem: {slopeCount(l, 3, 1)}')
    print(f'Answer of Second Problem: {slopeCount(l, 1, 1) * slopeCount(l, 3, 1) * slopeCount(l, 5, 1) * slopeCount(l, 7, 1) * slopeCount(l, 1, 2)}')

main()