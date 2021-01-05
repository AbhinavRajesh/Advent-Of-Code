INPUT_STR = '3113322113'

# 132123222113

def problem1(string):
    L = [x for x in string]
    finalStr = ''
    i = 0
    while i <= len(L) - 1:
        length = 1
        for j in range(i + 1, len(L)):
            if L[i] != L[j]:
                break
            length += 1
        finalStr += str(length) + str(L[i])
        i += length
    return finalStr

def main():
    inputStr = INPUT_STR
    for _ in range(40):
        inputStr = problem1(inputStr)
    print(f'Answer to Problem1: {len(inputStr)}')
    inputStr = INPUT_STR
    for _ in range(50):
        inputStr = problem1(inputStr)
    print(f'Answer to Problem2: {len(inputStr)}')


main()