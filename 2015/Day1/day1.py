def readData():
    file = open('input.txt').read()
    file = [x for x in file]
    return file

def problem1(data):
    floor = 0
    for x in data:
        if x == '(':
            floor += 1
        else:
            floor -= 1
    return floor

def problem2(data):
    floor = 0
    turns = 0
    for x in data:
        if floor == -1:
            break
        elif x == '(':
            floor += 1
        else:
            floor -= 1
        turns += 1
    return turns    

def main():
    data = readData()
    print(f'Answer to Problem1: {problem1(data)}')
    print(f'Answer to Problem2: {problem2(data)}')


main()