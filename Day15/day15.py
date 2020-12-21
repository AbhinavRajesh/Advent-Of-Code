puzzle_input = (1,2,16,19,18,0)

def main(digit):
    said = {n: i for i, n in enumerate(puzzle_input[:-1])}
    last_number = puzzle_input[-1]
    for i in range(len(puzzle_input), digit):
        try:
            last_turn = said[last_number]
        except KeyError:
            number = 0
        else:
            number = i - last_turn - 1
        said[last_number] = i - 1
        last_number = number
    return number

print(f'Answer to Problem1: {main(2020)}')
print(f'Answer to Problem2: {main(30000000)}')