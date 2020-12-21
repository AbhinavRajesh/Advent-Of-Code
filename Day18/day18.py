L = open('input.txt', 'r').read().split('\n')[:-1]

def getProblems():
    problems = []
    for l in L:
        problem = []
        for ch in l:
            if ch != ' ':
                problem += [ch]
        problems += [problem]
    return problems

def braces(problem):
    br = 0
    for i in range(len(problem)):
        if problem[i] == '(': 
            br += 1
        elif problem[i] == ')':
            br -= 1
        if br == 0:
            return problem2(problem[1:i])[0], i + 1

def problem1(problem):
    if problem[0] != '(':
        r = int(problem[0])
    else:
        r = 0
    i = 0
    while i < len(problem) - 1:
        if problem[i] == '(':
            a, b = problem1(problem[i + 1:])
            r = a
            i += b + 1
        elif problem[i] == '+':
            if problem[i + 1] != '(':
                r += int(problem[i+1])
                i += 1
            else: 
                a, b = problem1(problem[i + 2:])
                r += a
                i += b + 2
        elif problem[i] == '*':
            if problem[i+1] != '(':
                r *= int(problem[i + 1])
                i += 1
            else:
                a, b = problem1(problem[i+2:])
                r *= a
                i += b + 2
        elif problem[i] == ')':
            i += 1
            return r, i
        else:
            i += 1
    return r, i

def problem2(problem):
    if problem[0] != '(':
        r = int(problem[0])
    else:
        r = 0
    i = 0
    while i < len(problem) - 1:
        if problem[i] == '(':
            a, b = braces(problem)
            r = a
            i += b
        elif problem[i] == '+':
            if problem[i + 1] != '(':
                r += int(problem[i+1])
                i += 1
            else: 
                a, b = braces(problem[i + 1:])
                r += a
                i += b + 1
        elif problem[i] == '*':
            a, b = problem2(problem[i+1:])
            r *= a
            i += b + 1
        elif problem[i] == ')':
            i += 1
            return r, i
        else:
            i += 1
    return r, i

def main():
    problems = getProblems()
    ans1 = ans2 = 0

    for problem in problems:
        ans1 += problem1(problem)[0]
    print(f'Answer to Problem1: {ans1}')
    for problem in problems:
        ans2 += problem2(problem)[0]
    print(f'Answer to Problem2: {ans2}')
main()