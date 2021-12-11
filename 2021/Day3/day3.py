
def part1(bits):
    occurence = {}
    gamma = epsilon = ""
    for bit in bits:
        bit_array = [x for x in bit]
        for i in range(len(bit_array)):
            try:
                if bit_array[i] == "1":
                    occurence[i][1] += 1
                else:
                    occurence[i][0] += 1
            except KeyError:
                occurence[i] = {
                    0: 1 if bit_array[i] == "1" else 0, 
                    1: 1 if bit_array[i] == "0" else 0, 
                }
    
    for occurence in occurence.values():
        if occurence[0] > occurence[1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    print(f"Part1: {int(gamma, 2) * int(epsilon, 2)}")

def part2(all_bits):
    o2 = all_bits
    for i in range(len(o2[0])):
        ones = []
        zeroes = []
        for bit in o2:
            if bit[i] == "1":
                ones.append(bit)
            else:
                zeroes.append(bit)
        o2 = ones if len(ones) >= len(zeroes) else zeroes
    co2 = all_bits
    for i in range(len(co2[0])):
        ones = []
        zeroes = []
        for bit in co2:
            if bit[i] == "1":
                ones.append(bit)
            else:
                zeroes.append(bit)
        if len(zeroes) == 0:
            co2 = ones
            print(ones, zeroes)
            break
        elif len(ones) == 0:
            co2 = zeroes
            print(ones, zeroes)
            break
        co2 = ones if len(ones) < len(zeroes) else zeroes
    print(f"Part2: {int(o2[0], 2) * int(co2[0], 2)}")
        
    
def main():
    file = open("input.txt").readlines();
    bits = [x.replace("\n", "") for x in file]
    part1(bits)
    part2(bits)

if __name__ == "__main__":
    main()