def problem1(busIds, timestamp):
    minsWait = []
    for i in busIds:
        minsWait.append(i - timestamp%i)
    product = busIds[minsWait.index(min(minsWait))] * min(minsWait)
    print(f'Answer to Problem1: {product}')

def problem2(bus_offsets):
    inc = bus_offsets[0][1]
    t = inc
    i = 1
    while True:
        if (t + bus_offsets[i][0]) % bus_offsets[i][1] == 0: 
            t1 = t + inc
            while(t1 + bus_offsets[i][0]) % bus_offsets[i][1] != 0:
                t1 += inc
            if t1 > t:
                inc = t1 - t
            i += 1
        if all((t + j) % i == 0 for j, i in bus_offsets):
            print(f'Answer to Problem2: {t}')
            break
        t += inc

def main():
    timestamp, file = open('input.txt', 'r').read().splitlines()
    ids = file.split(',')
    busIds = []
    for i in ids:
        if i != 'x':
            busIds.append(int(i))
    bus_offsets = [(i, int(b)) for i, b in enumerate(file.split(',')) if b != 'x']
    problem1(busIds, int(timestamp))
    problem2(bus_offsets)
main()