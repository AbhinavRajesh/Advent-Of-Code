def problem1(data):
    i = 0
    j = 25
    while True:
        found = 0
        preamble = []
        for x in range(i, j):
            preamble.append(data[x])
        for k in preamble:
            if found == 1:
                break
            else: 
                for l in preamble:
                    if k == l:
                        continue
                    elif int(k) + int(l) == int(data[j]):
                        found = 1
                        break
        if found == 0:
            return data[j]
            break
        else: 
            i += 1
            j += 1
    
def problem2(data, number):
    testSet = []
    for j in range(len(data)):
        data[j] = int(data[j])
    for n in range(2, len(data)):
        for i in range(len(data) - n):
            testSet = data[i : i + n]
            if sum(testSet) == int(number):
                return min(testSet) + max(testSet)
    

def main():
    file = open('input.txt', 'r').read().split('\n')
    invalidNumber = problem1(file)
    file.pop(-1)
    print(f'Answer to Problem 1: {invalidNumber}')
    print(f'Answer to Problem 2: {problem2(file, invalidNumber)}')
    # print(file)


main()