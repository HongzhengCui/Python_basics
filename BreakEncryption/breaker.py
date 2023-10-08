import sys

def breaker(filename):
    f = open(filename, "r")
    line = f.readline()
    line = line.strip()
    line = ''.join(line.split())

    letter = []

    for char in line:
        if char.isalpha():
            letter.append(char)
    return letter

def most(s):
    cnum = {}
    for char in s:
        if char in cnum:
            cnum[char] += 1
        else:
            cnum[char] = 1
    
    mostc = max(cnum, key=cnum.get)
    return mostc

def key(c):
    key = (ord(c) - ord('e')) % 26
    return key

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python breaker.py <input_filename>")
        sys.exit(1)

    input_filename = sys.argv[1]

    try:
        letter = breaker(input_filename)
        mostc = most(letter)
        key = key(mostc)
        print(key)
    except SystemExit:
        sys.exit(1)