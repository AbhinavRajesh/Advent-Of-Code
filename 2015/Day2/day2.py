def readData():
    file = open('input.txt').read().splitlines()
    return file

def problem1(lines):
    wrapper = 0
    for line in lines:
        line = line.split('x')
        dimensions = [int(x) for x in line]
        dimensions.sort()
        wrapper += 2 * (dimensions[0] * dimensions[1] + dimensions[0] * dimensions[2] + dimensions[1] * dimensions[2]) + dimensions[0] * dimensions[1] 
    return wrapper

def problem2(lines):
    ribbon = 0
    for line in lines:
        line = line.split('x')
        dimensions = [int(x) for x in line]
        dimensions.sort()
        ribbon += 2 * (dimensions[0] + dimensions[1]) + dimensions[0] * dimensions[1] * dimensions[2]
    return ribbon

def main():
    data = readData() 
    print(f'Answer to Problem1: {problem1(data)}')
    print(f'Answer to Problem2: {problem2(data)}')

main()