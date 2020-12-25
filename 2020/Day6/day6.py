def problem1(groups):
    group = []
    temp = []
    count = 0
    for i in groups:
        group.append(i.split(' '))
    for i in range(len(group)):
        currentlySelected = []
        for j in group[i]:
            temp = [char for char in j]
            for k in temp:
                if k not in currentlySelected:
                    currentlySelected.append(k)
        count += len(currentlySelected)
    return count

def problem2(groups):
    group = []
    firstSelection = []
    count = 0
    s1 = set()
    for i in groups:
        group.append(i.split(' '))
    group[-1].remove('')
    for i in group:
        finalList = [char for char in i[0]]
        s1 = set(firstSelection)
        for j in i:
            charList = [char for char in j]
            s2 = set(charList)
            finalList = s2.intersection(finalList)
        count += len(finalList)                
    return count        

def main():
    file = open('input.txt')
    s = file.read()
    tempGroups = s.split('\n\n')
    groups = []
    for i in tempGroups:
        groups.append(i.replace('\n', ' '))
        
    print(f'Answer to Problem 1: {problem1(groups)}')
    print(f'Answer to Problem 2: {problem2(groups)}')


main()