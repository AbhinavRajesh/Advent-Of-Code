import hashlib

def problem(secret, p2=False):
    startsWith = '00000' if not p2 else '000000' 
    i = 1
    while True:
        result = hashlib.md5((secret + str(i)).encode())
        if result.hexdigest().startswith(startsWith):
            break
        i += 1
    return i

def main():
    secret = 'iwrupvqb'
    print(f'Answer to Problem1: {problem(secret)}')
    print(f'Answer to Problem2: {problem(secret, True)}')

main()