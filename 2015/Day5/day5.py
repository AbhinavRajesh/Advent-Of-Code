def problem1(lines):
    notAllowed = ['ab', 'cd', 'pq', 'xy']
    count = 0
    for line in lines:
        valid = False
        if any(char in line for char in notAllowed):
            continue
        vowelCount = 0
        for x in 'aeiou':
            vowelCount += line.count(x)
        if vowelCount >= 3:
            for i in range(len(line) - 1):
                if line[i] == line[i + 1]:
                    valid = True
        if valid:
            count += 1
    return count

def problem2(lines):
    count = 0
    for line in lines:
        xyxFound = False
        found = False
        for l in range(1, len(line) - 1):
            # XYX Pallindrome
            if line[l - 1] == line[l + 1]:
                xyxFound = True
            if xyxFound:
                for i in range(len(line) - 1):
                    temp = line[i] + line[i + 1]
                    for j in range(i + 2, len(line) - 1):
                        if temp == (line[j] + line[j + 1]):
                            found = True
            if found:
                count += 1
                break
    return count

def main():
    file = open('input.txt').read().splitlines()
    print(f'Answer to Problem1: {problem1(file)}')
    print(f'Answer to Problem2: {problem2(file)}')
main()