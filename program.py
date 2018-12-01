def day1():
    day1part1()
    day1part2()

day1()


def day1part1():
    freq = 0

    file = open("values.txt", "r")
    values = file.readlines()

    for value in values:
        number = int(value.replace('\n', ''))
        freq = freq + number

    print(freq)


def day1part2():
    freq = 0

    file = open("values.txt", "r")
    values = file.readlines()

    vector = []
    searching = True

    while searching:
        for value in values:
            if freq in vector:
                searching = False
                print(freq)
                break

            if not searching:
                break

            vector.append(freq)
            number = int(value.replace('\n', ''))
            freq = freq + number
