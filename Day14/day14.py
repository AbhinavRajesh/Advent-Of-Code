import math

def problem1(lines):
    mask = ''
    memDict = {}
    for line in lines:
        token = line.strip().split()
        if line.startswith('mask'):
            mask = token[2]
        else:
            memAddr, value = int(token[0][4:-1]), int(token[2])
            output = ''
            for i in range(36):
                elem = mask[35 - i]
                if elem == 'X':
                    elem = str(value % 2)
                output = elem + output
                value = value // 2
            memDict[memAddr] = output 
    sum = 0
    for key in memDict:
        sum += int(memDict[key], 2)
    print(f'Answer to Problem1: {sum}')

def problem2(lines):
    mask = ''
    memDict = {}
    for line in lines:
        token = line.strip().split()
        if line.startswith('mask'):
            mask = token[2]
        else:
            memAddr, value = int(token[0][4:-1]), int(token[2])
            output = ''
            floating = []
            for i in range(36):
                elem = mask[35 - i]
                if elem == '0':
                    elem = str(memAddr % 2)
                elif elem == 'X':
                    floating.append(35 - i)
                output = elem + output
                memAddr = memAddr // 2
            for i in range(0,int(math.pow(2,len(floating)))):
                for index in floating:
                    output = output[:index] + str(i%2) + output[index+1:]
                    i = i//2
                memDict[int(output)] = value
    sum = 0
    for key in memDict:
        sum += memDict[key]
    print(f'Answer to Problem2: {sum}')

def main(): 
    file = open('input.txt', 'r').read().splitlines()
    problem1(file)
    problem2(file)


main()