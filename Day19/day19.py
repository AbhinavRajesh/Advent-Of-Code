with open("input.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

    rulesData = data[:data.index("")]
    msgs = data[data.index("") + 1:]

rules = {}
for line in rulesData:
    line = line.split(": ")
    ruleNum = int(line[0])
    options = []
    optionStr = line[1].split(" | ")
    for option in optionStr:
        options.append(option.split())
    rules[ruleNum] = options

strRules = {}

# Part 1

def problem1(num):
    ruleOptions = rules[num] 
  
    if ['"a"'] in ruleOptions:
        return ['a']
    if ['"b"'] in ruleOptions:
        return ['b']
    if num in strRules:
        return strRules[num]
    final = []
    for option in ruleOptions:
        strOps = []
        for rule in option:
            subOps = problem1(int(rule))

            if len(strOps) == 0:
                strOps = subOps.copy()
            else:
                combined = []
                for s in subOps:
                    for op in strOps:
                        combined.append(op + s)
                strOps = combined.copy()
        final += strOps
        strRules[num] = final
    return final

allPossibilities = problem1(0)  
allSet = set()

for a in allPossibilities:
    allSet.add(a)

count = 0
for msg in msgs:
    if msg in allSet:
        count += 1
print(f'Answer to Problem1: {count}')

# Part 2

def problem2():
    r42 = strRules[42]
    r31 = strRules[31]
    chunkSize = len(r42[0])
    count = 0
    for msg in msgs:
        chunks42 = [False for _ in range(len(msg) // chunkSize)] 
        chunks31 = [False for _ in range(len(msg) // chunkSize)]
        currChunk = 0
        for i in range(0, len(msg), chunkSize):
            if msg[i:i + chunkSize] in r42:
                chunks42[currChunk] = True
            if msg[i:i + chunkSize] in r31:
                chunks31[currChunk] = True
            currChunk += 1 
        count42, count31 = 0, 0
        currChunk = 0
        if chunks42[currChunk] == True:
            count42 += 1
            currChunk += 1
            while currChunk < len(chunks42) and chunks42[currChunk]:
                count42 += 1
                currChunk += 1
            while currChunk < len(chunks31) and chunks31[currChunk]:
                count31 += 1
                currChunk += 1
            if currChunk== len(chunks31) and 0 < count31 < count42:
                count += 1
    return count
            

ans2 = problem2()
print(f'Answer to Problem2: {ans2}')