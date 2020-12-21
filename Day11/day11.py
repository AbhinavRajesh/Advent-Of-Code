def getValue(board, i, j):
    if (i < 0 or j < 0 or i >= len(board) or j >= len(board[0])):
        return ''
    return board[i][j]

def compare(board1, board2):
    for i in range(len(board1)):
        for j in range(len(board1[0])):
            if ( board1[i][j] != board2[i][j]):
                return False
    return True

# def copy(lines):
#     temp = list()
#     for i in lines:
#         for j in i:
#             temp.append(j)
#     return temp

def copy(lines):
    temp = list()
    for i in range(len(lines)):
        temp.append(list())
        for j in range(len(lines[i])):
            temp[i].append(lines[i][j])
    return temp

def returnOccupied(board):
    count = 0
    for i in board:
        for j in i:
            if j == '#':
                count += 1
    return count

def occupiedSeatsVisible(array2d, i, j):
    around = ['?','?','?',
              '?',    '?',
              '?','?','?']
    radius = 1
    while around.count('?') > 0:
        if (around[0] == '?'): # top left
            t = getValue(array2d, i-radius, j-radius)
            if t in ['#','L','']: around[0] = t
        if (around[1] == '?'): # top
            t = getValue(array2d, i-radius, j)
            if t in ['#','L','']: around[1] = t
        if (around[2] == '?'): # top right
            t = getValue(array2d, i-radius, j+radius)
            if t in ['#','L','']: around[2] = t
        if (around[3] == '?'): # left
            t = getValue(array2d, i,        j-radius)
            if t in ['#','L','']: around[3] = t
        if (around[4] == '?'): # right
            t = getValue(array2d, i,        j+radius)
            if t in ['#','L','']: around[4] = t
        if (around[5] == '?'): # bottom left
            t = getValue(array2d, i+radius, j-radius)
            if t in ['#','L','']: around[5] = t
        if (around[6] == '?'): # bottom
            t = getValue(array2d, i+radius, j)
            if t in ['#','L','']: around[6] = t
        if (around[7] == '?'): # bottom right
            t = getValue(array2d, i+radius, j+radius)
            if t in ['#','L','']: around[7] = t
        # increase search radius
        radius += 1
    return around

def part2(lines):
    modified = True
    cycles = 0
    while modified:
        cycles += 1
        linesNext = copy(lines)
        for i in range(len(linesNext)):
            for j in range(len(linesNext[0])):
                if (lines[i][j] in ['L','#']):
                    t = occupiedSeatsVisible(lines,i,j)
                    if (t.count('#') == 0):
                        linesNext[i][j] = '#'
                    elif (t.count('#') >= 5 and lines[i][j] in ['L','#']):
                        linesNext[i][j] = 'L'
        #printArray(cycles, lines)
        modified = not compare(lines, linesNext)
        lines = copy(linesNext)
    print('after',cycles,'rounds',returnOccupied(lines),'seats are in use')

def main():
    file = open('input.txt', 'r').read().split('\n')
    file.pop(-1)
    for i in range(len(file)):
        l = [char for char in file[i]]
        file[i] = l
    board = copy(file)
    same = True
    after = copy(board)
    while same:
        after = copy(board)
        for i in range(len(file)):
            for j in range(len(file[0])):
                if (board[i][j] in ['L', '#']):
                    t = [getValue(board, i - 1, j - 1), getValue(board, i - 1, j), getValue(board, i - 1, j + 1), 
                        getValue(board, i, j - 1),                                  getValue(board, i, j + 1), 
                        getValue(board, i + 1, j - 1), getValue(board, i + 1, j), getValue(board, i + 1, j + 1)]
                    if t.count('#') == 0:
                        after[i][j] = '#'
                    elif t.count('#') >= 4:
                        after[i][j] = 'L'
        same = not compare(board, after)
        board = copy(after)

    count = returnOccupied(board)
    print(count)
    part2(file)
main()