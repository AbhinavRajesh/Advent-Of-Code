from itertools import permutations

people = []
relations = {}

def parseData(line):
    args = line[0:-1].split()
    n = int(args[3])
    if args[2] == 'lose':
        n *= -1
    subject = args[0]
    if subject not in people:
        people.append(subject)
    neighbor = args[-1]
    relations[(subject, neighbor)] = n

def calculateTotal(order):
    length = len(order)
    happiness = 0
    for n in range(length):
        p1 = order[n]
        p2 = order[(n + 1) % length]
        happiness += relations[(p1, p2)]
        happiness += relations[(p2, p1)]
    return happiness

def problem1(lines):
    for line in lines:
        parseData(line)
    for person in people:
        relations[(person, 'me')] = 0
        relations[('me', person)] = 0
    people.append('me')
    firstPerson = people.pop(0)
    orders = permutations(people)
    happiness = 0
    for order in orders:
        happiness = max(happiness, calculateTotal([firstPerson] + list(order)))
    print(happiness)

def main():
    lines = open('input.txt').read().rstrip().splitlines()
    problem1(lines)

main()