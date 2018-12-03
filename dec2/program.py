# Part1
twiceCount = 0
threeCount = 0

file = open("values.txt", "r")
values = file.readlines()
boxCodes = []


for value in values:
    # Clean \n
    boxCode = value.replace('\n', '')
    boxCodes.append(boxCode)  # For next part
    twoTimes = False
    threeTimes = False

    for letter in boxCode:
        if boxCode.count(letter) == 3:
            threeTimes = True
        elif boxCode.count(letter) == 2:
            twoTimes = True

        if twoTimes and threeTimes:
            break

    twiceCount += twoTimes
    threeCount += threeTimes

checksum = threeCount * twiceCount

print(checksum)

# Part2

maxErrors = 100
code1 = []
code2 = []

for code in boxCodes:
    for compare in boxCodes:  # Compare each line with all other lines?

        if compare != code:
            errors = 0
            badMatch = False

            for i in range(len(code)):
                if compare[i] != code[i]:
                    errors += 1

                    if errors > maxErrors:
                        badMatch = True
                        break

            if not badMatch and errors != maxErrors:
                if errors == 0:
                    print('0?')
                    print(compare)
                    print(code)
                maxErrors = errors
                code1 = [code]
                code2 = [compare]
            elif not badMatch:
                if code1 is not None:
                    code1 = [code]
                    code2 = [compare]
                else:
                    code1.append(code)
                    code2.append(compare)

print(maxErrors)
print(code1)
print(code2)
print('------')

finalString = ''
string1 = code1[0]
string2 = code2[0]

for i in range(len(string1)):
    if string1[i] == string2[i]:
        finalString += string1[i]

print(finalString)
