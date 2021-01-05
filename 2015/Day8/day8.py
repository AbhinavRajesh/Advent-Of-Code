def problem1(lines):
    char_number, size_of_char = 0, 0
    for line in lines:
        char_number += len(line)
        size_of_char += len(eval(line))
    print(char_number - size_of_char)

def ecodedFile(lines):
    newFile = []
    for line in lines:
        # L = [x for x in line]
        # if '\\' in L:
        #     i = L.index('\\')
        #     L.pop(i)
        #     L.insert(i, '\\\\')
        # if '"' in L:
        #     print(L.index('"'))
        #     break
        #     L.insert()
        # newLine = ''.join(str(x) for x in L)
        newLine = ''
        for x in line:
            if x == '\\':
                newLine += '\\\\'
            elif x == '"':
                newLine += "\\\""
            else:
                newLine += x
        newLine = '"' + newLine + '"'
        newFile.append(newLine)
    return newFile

def main():
    file = open('input.txt').read().splitlines()
    problem1(file)
    newFile = ecodedFile(file)
    problem1(newFile)

main()