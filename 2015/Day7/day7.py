file = open('input.txt').read().splitlines()
calc = dict()
results = dict()
for line in file:
    (ops, res) = line.split('->')
    calc[res.strip()] = ops.strip().split(' ')

# calc2['b'] = 16076
# calc['b'] = 16076


def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass
    
    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
                res =  calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
                res =  calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
                res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
                res =  calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
                res =  calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]

calc2 = dict()
results2 = dict()
for line in file:
    (ops, res) = line.split('->')
    calc2[res.strip()] = ops.strip().split(' ')

results2['b'] = 16076
# calc2['b'] = 16076

def part2(name):
    try:
        return int(name)
    except ValueError:
        pass
    
    if name not in results2:
        # print(calc2[name], name)
        ops = calc2[name]
        if len(ops) == 1:
            res = part2(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
                res =  part2(ops[0]) & part2(ops[2])
            elif op == 'OR':
                res =  part2(ops[0]) | part2(ops[2])
            elif op == 'NOT':
                res = ~part2(ops[1]) & 0xffff
            elif op == 'RSHIFT':
                res =  part2(ops[0]) >> part2(ops[2])
            elif op == 'LSHIFT':
                res =  part2(ops[0]) << part2(ops[2])
        results2[name] = res
    return results2[name]

def main():
    print(calculate('a'))
    print(part2('a'))

main()