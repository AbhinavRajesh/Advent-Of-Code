import string
ALPHABET = string.ascii_lowercase
password = "hepxcrrq"

def rule1(password):
    for i in range(len(password) - 2):
        if password[i:i + 3] in ALPHABET:
            return True
    return False

def rule2(password):
    return all((c not in password for c in 'iol'))

def rule3(password):
    nrep = 0
    i = 0
    while i < (len(password) - 1):
        if password[i] == password[i + 1]:
            nrep += 1
            i += 1
        i += 1
    return nrep > 1

def shift(password):
    data = list(password)
    for i in range(len(data) - 1, -1, -1):
        data[i] = chr((ord(data[i]) - ord('a') + 1) % 26 + ord('a'))
        if data[i] != 'a':
            break
    return ''.join(data)

def next_password(current_password):
    rules = [ rule1, rule2, rule3 ]
    password = shift(current_password)
    while not all((t(password) for t in rules)):
        password = shift(password)
    return password

password = next_password(password)
print(password)
password = next_password(password)
print(password)
