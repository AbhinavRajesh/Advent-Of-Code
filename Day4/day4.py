import re

check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def problem1(passport):
    validPass = 0
    for i in range(len(passport)):
        if all(x in passport[i] for x in check):
            validPass += 1
    print(f'Answer of First Part: {validPass}')

def problem2(passport):
    newPassport = []
    testCount = 0
    isValid = True
    validPass = 0
    eyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    allowedHCL = '#0123456789abcdef'
    allowedPID = '0123456789'
    for i in passport:
        newPassport.append(i.replace('\n', ' '))
    for i in range(0, len(newPassport)):
        isValid = True
        q = newPassport[i].split(' ')
        if all(x in passport[i] for x in check):
            testCount += 1
            for j in q:
                testCount +=1
                temp = j.split(':')
                if temp[0] == 'byr':
                    if 1920 <= int(temp[1]) <= 2002:
                        isValid = True
                    else:
                        isValid = False
                        break
                elif temp[0] == 'iyr':
                    if 2010 <= int(temp[1]) <= 2020:
                        isValid = True
                    else:
                        isValid = False
                        break
                elif temp[0] == 'eyr':
                    if 2020 <= int(temp[1]) <= 2030:
                        isValid = True
                    else:
                        isValid = False
                        break
                elif temp[0] == 'hgt':
                    if 'cm' in temp[1]:
                        if 150 <= int(temp[1][:-2]) <= 193:
                            isValid = True
                        else:
                            isValid = False
                            break
                    elif 'in' in temp[1]:                      
                        if 59 <= int(temp[1][:-2]) <= 76:
                            isValid = True
                        else:
                            isValid = False
                            break
                    else:
                        isValid = False
                        break
                elif temp[0] == 'ecl':
                    if temp[1] in eyeColor:
                        isValid = True
                    else:
                        isValid = False
                        break
                elif temp[0] == 'pid':
                    if any(x in allowedPID for x in temp[1]):
                        isValid = True
                    else:
                        isValid = False
                        break
                elif temp[0] == 'hcl':
                    if re.fullmatch(r'#[0-9a-f]{6}',temp[1]):
                        isValid = True
                    else:
                        isValid = False
                else:
                    isValid = False
            if isValid:
                validPass += 1            
    print(f'Answer to second Part: {validPass}')

def main():
    file = open('input.txt', 'r')
    s = file.read()
    l = s.split('\n\n')
    passport = []
    for i in l:
        passport.append(i)
    problem1(passport)
    problem2(passport)

main()