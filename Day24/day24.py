file = open('input.txt').read().splitlines()

DIRECTIONS = { 'e': [2, 0], 'se': [1, -1], 'sw': [-1, -1], 
               'w': [-2, 0], 'nw': [-1, 1], 'ne': [1, 1]}


def readData(file):
    paths = []
    for line in file:
        instructions = []
        curr = ""
        for i in line:
            if curr + i in DIRECTIONS.keys():
                instructions.append(curr + i)
                curr = ""
            else:
                curr = i
        paths.append(instructions)
    return paths 
            
def initBoard(paths):
    flipped = set()
    for path in paths:
        coords = [0, 0]
        for inst in path:
            curr = DIRECTIONS[inst]
            for i in range(len(coords)):
                coords[i] += curr[i]
        tuped = tuple(coords)
        if tuped not in flipped:
            flipped.add(tuped)
        else:
            flipped.remove(tuped)
    return flipped

def part1(data):
    return len(initBoard(data))

def part2(data):
    blacks = initBoard(data)
    for _ in range(100):
        neighbour = {}
        for tile in blacks:
            if tile not in neighbour:
                neighbour[tile] = 0
            for token in DIRECTIONS.keys():
                curr = list(tile)
                for j in range(len(curr)):
                    curr[j] += DIRECTIONS[token][j]
                curr = tuple(curr)
                if curr not in neighbour.keys():
                    neighbour[curr] = 1
                else:
                    neighbour[curr] += 1
        newBlacks = set()
        for tile in neighbour:
            if ( tile in blacks and neighbour[tile] in [1, 2]) or (tile not in blacks and neighbour[tile] == 2):
                newBlacks.add(tile) 
        blacks = newBlacks
    return len(blacks)

def main():
    print(f'Answer to Problem1: {part1(readData(file))}')
    print(f'Answer to Problem2: {part2(readData(file))}')

main()