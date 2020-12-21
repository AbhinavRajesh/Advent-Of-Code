def check(values, fields):
    firstRange = range(values[0][0], values[0][1] + 1)
    secondRange = range(values[1][0], values[1][1] + 1)
    return all(field in firstRange or field in secondRange for field in fields)

def problem1(lines, rules):
    minRange = min([i[0] for rule in rules.values() for i in rule])
    maxRange = max([i[1] for rule in rules.values() for i in rule])
    invalid = 0
    for line in lines[25:]:
        fields = [int(i) for i in line.split(',')]
        for field in fields:
            if field not in range(minRange, maxRange):
                invalid += field
    print(f'Answer to Problem1: {invalid}')

def problem2(lines, rules):
    minRange = min([i[0] for rule in rules.values() for i in rule])
    maxRange = max([i[1] for rule in rules.values() for i in rule])
    newList = []
    possible = {}
    for line in lines[25:]:
        fields = [int(i) for i in line.split(',')]
        if all([field in range(minRange, maxRange + 1) for field in fields]):
            newList.append(fields)
    for j in range(len(newList[0])):
        possibleRules = []
        fields = [newList[i][j] for i in range(len(newList))]
        for rule, value in rules.items():
            if check(value, fields):
                possibleRules.append(rule)
        possible[j] = possibleRules
    ordered = sorted([(len(val), key) for key, val in possible.items()])
    orderedCol = [x[1] for x in ordered]
    confirmed = {}
    for j in orderedCol:
        possibleRules = possible[j]
        for field in confirmed.keys():
            possibleRules.remove(field)
        confirmed[possibleRules[0]] = j
    ticket = [int(x) for x in lines[22].split(',')]
    product = 1
    for key, value in confirmed.items():
        if key.startswith('departure'):
            product *= ticket[value]
    print(f'Answer to Problem2: {product}')

def main():
    file = open('input.txt')
    lines = [x.rstrip() for x in file.readlines()]
    rules = {}
    for rule in lines[:20]:
        fieldName = rule.split(': ')[0]
        firstRange = rule.split(': ')[1].split(' or ')[0]
        secondRange = rule.split(': ')[1].split(' or ')[1]
        firstMin = int(firstRange.split('-')[0])
        firstMax = int(firstRange.split('-')[1])
        secondMin = int(secondRange.split('-')[0])
        secondMax = int(secondRange.split('-')[1])
        rules[fieldName] = [(firstMin, firstMax), (secondMin, secondMax)]
    problem1(lines, rules)
    problem2(lines, rules)

main()