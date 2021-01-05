import json

def problem1(obj):
    if type(obj) == type(dict()):
        return sum(map(problem1, obj.values()))
    if type(obj) ==type(list()):
        return sum(map(problem1, obj))
    if type(obj) == type(0):
        return obj
    return 0

def problem2(obj):
    if type(obj) == type(dict()):
        if "red" in obj.values():
            return 0
        return sum(map(problem2, obj.values()))
    if type(obj) ==type(list()):
        return sum(map(problem2, obj))
    if type(obj) == type(0):
        return obj
    return 0

def main():
    data = json.loads(open('input.txt', 'r').read())
    print(problem1(data))
    print(problem2(data))
main()