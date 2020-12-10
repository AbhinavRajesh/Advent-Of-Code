def problem1(file):
    jolt1 = 0
    jolt3 = 0
    for i in range(len(file) - 1):
        if file[i+1] - file[i] == 1:
            jolt1 += 1
        elif file[i + 1] - file[i] == 3:
            jolt3 += 1
    print(f'Answer to Problem1: {jolt1* jolt3}')

def findWays(data):
    if len(data) == 0:
        return 0
    if len(data) < 3:
        return 1
    ways = 0
    ways += findWays(data[1:])
    ways += findWays(data[2:])
    ways += findWays(data[3:])
    return ways

def problem2(file):
    start = 0
    prev = 0
    paths = 1
    for i in range(len(file)):
        x = file[i]
        if prev + 3 == x:
            path = findWays(file[start:i])
            paths *= path
            start = i
        prev = file[i]
            
    print(f'Answer to Problem2: {paths}')

def main():
    file = open('input.txt').read().split('\n')
    file.pop(-1)
    for i in range(len(file)):
        file[i] = int(file[i])
    file.append(max(file) + 3)
    file.insert(0, 0)
    for i in range(len(file)):
        for j in range(len(file) - i - 1):
            if file[j] > file[j+1]:
                temp = file[j]
                file[j]= file[j + 1]
                file[j + 1] = temp
    problem1(file)
    problem2(file)


main()