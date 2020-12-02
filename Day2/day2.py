def splitChar(item):
    temp = [char for char in item]
    return temp[0]

def main():
    l =[]
    q = []
    count = 0
    file = open("input.txt", "r")
    s = file.read()
    l = s.split('\n')
    l=[i for i in l if i!='']
    for i in l:
        temp = i.split(' ')
        q.append(temp)
    for i in q:
        i[1] = splitChar(i[1])
        temp = i[0].split('-')
        num1 = temp[0]
        num2 = temp[1]
        occurence = i[2].count(i[1])
        if occurence <= int(num2) and occurence >= int(num1):
            count += 1
    print(f'First Part count: {count}')
    count = 0
    for i in q:
        temp = i[0].split('-')
        num1 = int(temp[0]) - 1
        num2 = int(temp[1]) - 1
        if len(i[2]) > num1:
            if i[2][num1] == i[1]:
                if len(i[2]) > num2:
                    if i[2][num2] != i[1]:
                        count+=1
                else:
                    count+=1
            elif i[2][num1] != i[1]:
                if len(i[2]) > num2:
                    if i[2][num2] == i[1]:
                        count+=1
    print(f'Second Part count: {count}')
main()