
def part1(depths):
    increased = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i+1]:
            increased += 1
    print(f"Part1: {increased}")

def part2(depths):
    increased = 0
    for i in range(2, len(depths) - 1):
        if depths[i-2] + depths[i-1] + depths[i] < depths[i-1] + depths[i] + depths[i+1]:
            increased += 1
    print(f"Part2: {increased}")

def main():
    file = open("input.txt", "r").readlines()
    depths = [int(x) for x in file]
    part1(depths)
    part2(depths)

if __name__ == "__main__":
    main()