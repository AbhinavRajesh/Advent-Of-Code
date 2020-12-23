def problem1(cups):
    for _ in range(100):
        picked = cups[1:4]
        dest = cups[0] - 1
        if dest == 0:
            dest = 9
        while dest in picked:
            dest -= 1
            if dest == 0:
                dest = 9
        without = cups[:1] + cups[4:]
        destIndex = without.index(dest)
        without = without[:destIndex + 1] + picked + without[destIndex + 1:]
        cups = without[1:] + without[:1]
    return cups


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def part2(cups):
    lookup = {}

    prev = None
    for i in range(len(cups) - 1, -1, -1):
        new = Node(cups[i])
        new.next = prev
        lookup[cups[i]] = new
        prev = new
    
    for i in range(1000000, 9, -1):
        new = Node(i)
        new.next = prev
        lookup[i] = new
        prev = new
    
    lookup[cups[-1]].next = lookup[10]

    cur = lookup[cups[0]]

    for _ in range(10000000):
        pick1 = cur.next
        pick2 = pick1.next
        pick3 = pick2.next
        cur.next = pick3.next
        picked = { cur.val, pick1.val, pick2.val, pick3.val}
        cur_val = cur.val
        while cur_val in picked:
            cur_val -= 1
            if cur_val == 0:
                cur_val = 1000000
        targetLoc = lookup[cur_val]
        afterTarget = targetLoc.next

        targetLoc.next = pick1
        pick3.next = afterTarget

        cur = cur.next
    
    cup1 = lookup[1]
    pick1 = cup1.next
    pick2 = pick1.next

    return pick1.val * pick2.val



def main():
    data = '135468729'
    data = [int(x) for x in data]
    data = problem1(data)
    print(f"Answer to Problem1: {''.join(str(x) for x in (data[data.index(1) + 1:] + data[:data.index(1)]))}")
    data = '135468729'
    data = [int(x) for x in data]
    print(f'Answer to Problem2: {part2(data)}')
main()