def part1(commands):
    horizontal = depth = 0
    for command_line in commands:
        command, offset = command_line.split(" ")
        if command == "forward":
            horizontal += int(offset)
        elif command == "down":
            depth += int(offset)
        elif command == "up":
            depth -= int(offset)
    print(f"Part1: {depth*horizontal}")

def part2(commands):
    horizontal = depth = aim = 0
    for command_line in commands:
        command, offset = command_line.split(" ")
        if command == "forward":
            horizontal += int(offset)
            depth += aim * int(offset)
        elif command == "down":
            aim += int(offset)
        elif command == "up":
            aim -= int(offset)
    print(f"Part2: {depth*horizontal}")

def main():
    file = open("input.txt").readlines()
    commands = [x.replace("\n", "") for x in file]
    part1(commands)
    part2(commands)


if __name__ == "__main__":
    main()