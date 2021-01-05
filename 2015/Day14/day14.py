def problem1(line):
    time = 0
    speed = int(line[1])
    travelTime = int(line[2])
    restTime = int(line[3])
    distance = 0
    while time <= 2503:
        if time + travelTime > 2503:
            distance += speed * (2503 - time)
            break
        distance += speed * travelTime
        time += travelTime
        if time + restTime > 2503:
            break
        time += restTime
    return distance

# def problem2(lines):
    

def main():
    lines = open('input.txt').read().splitlines()
    # testInput = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']
    L = []
    for line in lines:
        temp = []
        temp.append(line.split()[0])
        temp.append(line.split()[3])
        temp.append(line.split()[6])
        temp.append(line.split()[13])
        L.append(temp)    
    print(max([problem1(l) for l in L]))
    # deers = dict()
    # for l in L:
    #     deers['name'] = l[0]
    # print(deers)
    # problem2(L)
main()