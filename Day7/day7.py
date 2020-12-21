import re

cols = dict()

def contains(c):
    if c == 'shiny gold':
        return True
    else:
        for x in cols[c]:
            if contains(x):
                return True
    return False

def inside(c):
    if len(cols[c]) == 0:
        return 1
    else:
        sum = 1
        for x in cols[c]:
            sum += int(cols[c][x]) * inside(x)
        return sum

def main():
    data = [x.rstrip() for x in open("input.txt").readlines()]
    for i in data:
        s = i.split(' ')
        c = f'{s[0]} {s[1]}'
        x = 2
        cols[c] = dict()
        while x < len(s):
            if re.match('[0-9]+', s[x]):
                nc = f'{s[x + 1]} {s[x + 2]}'
                cols[c][nc] = s[x]
            x += 1
    count = 0
    for c in cols:
        if contains(c):
            count += 1
            
    print(f'Problem 1 Answer: {count - 1}')
    print(f'Problem 2 Answer: { inside("shiny gold") - 1 }')
main()