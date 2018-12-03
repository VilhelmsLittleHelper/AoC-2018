# Part 1
file = open("values.txt", "r")
values = file.readlines()

n = 1000
m = 1000
space = [[0 for col in range(n)] for row in range(m)]

count = 0

for value in values:
    # Clean \n and parse value
    clean = value.replace('\n', '')

    indexValue = int(clean.split('@')[0].replace('#', ''))
    vertInd = int(clean.split('@')[1].split(':')[0].split(',')[0])
    horiInd = int(clean.split('@')[1].split(':')[0].split(',')[1])

    vertiLength = int(clean.split('@')[1].split(':')[1].split('x')[0])
    horiLength = int(clean.split('@')[1].split(':')[1].split('x')[1])

    for i in range(vertInd, vertInd + vertiLength):
        for j in range(horiInd, horiInd + horiLength):
            if space[i][j] != 0 and space[i][j] != -1:
                space[i][j] = -1
                count = count + 1
            elif space[i][j] == 0:
                space[i][j] = indexValue
print(count)

# Part 2
for value in values:
    # Clean \n and parse value
    clean = value.replace('\n', '')

    indexValue = int(clean.split('@')[0].replace('#', ''))
    vertInd = int(clean.split('@')[1].split(':')[0].split(',')[0])
    horiInd = int(clean.split('@')[1].split(':')[0].split(',')[1])

    vertiLength = int(clean.split('@')[1].split(':')[1].split('x')[0])
    horiLength = int(clean.split('@')[1].split(':')[1].split('x')[1])

    testValue = True
    for i in range(vertInd, vertInd + vertiLength):
        for j in range(horiInd, horiInd + horiLength):
            if space[i][j] != indexValue:
                testValue = False

    if testValue:
        print(indexValue)
