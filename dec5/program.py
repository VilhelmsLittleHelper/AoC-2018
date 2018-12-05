# (raw code)
# Part 1
file = open("values.txt", "r")
line = file.readlines()[0]

print(line)
print(len(line))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

removed = True
oldSize = len(line)

while removed:
    removed = False
    for letter in alphabet:
        line = line.replace(letter + letter.capitalize(), '').replace(letter.capitalize() + letter, '')
        if len(line) < oldSize:
            removed = True

        oldSize = len(line)

print(line)
print(len(line))

# Part 2

stash = line
bestLetter = None
bestScore = 100000

for letter in alphabet:
    test = stash
    removed = True
    oldTestSize = len(test)
    test = test.replace(letter, '').replace(letter.capitalize(), '')
    while removed:
        removed = False
        for l in alphabet:
            test = test.replace(l + l.capitalize(), '').replace(l.capitalize() + l, '')
            if len(test) < oldTestSize:
                removed = True

            oldTestSize = len(test)

    if len(test) < bestScore:
        bestScore = len(test)
        bestLetter = letter

    print(letter)
    print(len(test))

print(bestLetter)
print(bestScore)
