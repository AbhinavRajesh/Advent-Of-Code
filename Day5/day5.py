import math

def split(word):
    return [char for char in word]

def getRow(row):
    upper = 127
    lower = 0
    for j in row:
        if j == 'F':
            upper -= math.ceil((upper - lower)/2)
        else:
            lower += math.ceil((upper - lower)/2)
    return upper

def getColumn(column):
    upper = 7
    lower = 0
    for j in column:
        if j == 'L':
            upper -= math.ceil((upper - lower)/2)
        else:
            lower += math.ceil((upper - lower)/2)
    return upper

def getId(line):
    return getRow(line[:-3]) * 8 + getColumn(line[7:])

def main():
    file = open('input.txt')
    s = file.read()
    l = s.split('\n')
    l.pop(-1)
    l2 = []
    highest = 0
    for i in l:
        temp = getId(i)
        if highest < temp:
            highest = temp       
    print(f'Answer to Problem 1: {highest}')
    ids = [i for i in range(highest+1)]
    noToPop = 0
    for i in l:
        ids.remove(getId(i))
    for i in ids:
        if ((i + 1) in ids) or ((i -1) in ids):
            noToPop += 1 
    for i in range(0, noToPop):
        ids.pop(0)
    print(f'Answer to Problem 2: {ids[0]}')
main()