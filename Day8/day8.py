found = False

def problem1(data):
    commandsRan = set()
    acc = 0
    i = 0
    while True:
        if i in commandsRan:
            return acc
        else:
            commandsRan.add(i)
            operation, argument = data[i].split(' ')
            number = argument[1:]
            if operation == 'acc':
                acc += int(argument)
                i += 1
            elif operation == 'jmp':
                i += int(argument)
            elif operation == 'nop':
                i += 1
            else:
                print(data[i])
            if i >= len(data):
                global found
                found = True
                return acc

def problem2(data):
    test = 0
    for i in range(len(data)):
        newData = data.copy()
        if newData[i].startswith('jmp'):
            newData[i] = newData[i].replace('jmp', 'nop')
            problem1(newData)
        elif newData[i].startswith('nop'):
            newData[i] = newData[i].replace('nop', 'jmp')
            problem1(newData)
        if found:
            print(f'Answer to Problem2: {problem1(newData)}')
            break
        test += 1

def main():
    file = open('input.txt').read().split('\n')
    file.pop(-1)
    print(f'Answer To Problem1: {problem1(file)}')
    problem2(file)

main()