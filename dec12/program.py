# (raw code)
# Part 1

from collections import deque


def change_value(something):
    if something == '#':
        return 1
    return 0


class Grid:
    def __init__(self):
        self.size = size = 40
        self.grid = [[0 for col in range(size)] for row in range(21)]
        self.values = []
        self.initial_state = None
        self.scoot = 3
        self.generation = 1
        self.gen = 21
        self.most_left = 0

    def add_input(self, value):
        self.values.append(value)

    def add_initial_state(self, value):
        self.initial_state = value
        self.size = len(value)
        self.grid = [[0 for col in range(self.size)] for row in range(self.gen)]

    def change_number_of_gen(self, gens):
        self.gen = gens
        self.grid = [[0 for col in range(self.size)] for row in range(self.gen)]

    def print_table(self):
        gen = 0
        for row in self.grid:
            #row = row[7:]
            #print(gen)
            print(row)
            gen += 1

    def calc_initial_state(self):
        row = [0, 0, 0, 0]
        for i in range(len(self.initial_state)):
            if i < len(self.initial_state):
                row.append(change_value(self.initial_state[i]))
        row.append(0)
        row.append(0)
        self.grid = []
        self.grid.append(row)
        self.most_left = -4

    def do_generation(self):
        row = []
        for plant in range(len(self.grid[-1])):
            for event in self.values:
                if plant > 1 and plant < (len(self.grid[-1]) -3):
                    #self.grid[self.generation][plant] = self.grid[self.generation - 1][plant]  # TODO: Change back, add to row instead of change value of a row
                    if (change_value(event[2]) == self.grid[self.generation - 1][plant]) or (change_value(event[2]) == self.grid[self.generation - 1][plant]):
                        if change_value(event[1]) == self.grid[self.generation - 1][plant - 1] and\
                                        change_value(event[0]) == self.grid[self.generation - 1][plant - 2] and\
                                        change_value(event[3]) == self.grid[self.generation - 1][(plant + 1) % self.size] and\
                                        change_value(event[4]) == self.grid[self.generation - 1][(plant + 2) % self.size]:
                            self.grid[self.generation][plant] = change_value(event[-1])

        self.generation += 1

    def calc_answer(self):
        answer = 0
        plants = deque(self.grid.pop())
        #plants.rotate(-(self.scoot - 3))
        print('.....')
        print(plants)
        i = -3
        for plant in plants:
            answer += plant * i
            i += 1
        print(answer)


# For test
grid = Grid()
grid.add_initial_state('#..#.#..##......###...###')
grid.calc_initial_state()
inputs = ['...## => #'
,'..#.. => #'
,'.#... => #'
,'.#.#. => #'
,'.#.## => #'
,'.##.. => #'
,'.#### => #'
,'#.#.# => #'
,'#.### => #'
,'##.#. => #'
,'##.## => #'
,'###.. => #'
,'###.# => #'
,'####. => #']

for value in inputs:
    grid.add_input(value)

for g in range(20):
    grid.do_generation()
grid.print_table()

grid.calc_answer()

grid = Grid()
grid.add_initial_state('#..#.#..##......###...###')
grid.calc_initial_state()
inputs = ['...## => #'
,'..#.. => #'
,'.#... => #'
,'.#.#. => #'
,'.#.## => #'
,'.##.. => #'
,'.#### => #'
,'#.#.# => #'
,'#.### => #'
,'##.#. => #'
,'##.## => #'
,'###.. => #'
,'###.# => #'
,'####. => #']

for value in inputs:
    grid.add_input(value)

for g in range(20):
    grid.do_generation()
#grid.print_table()

grid.calc_answer()

# For real

grid = Grid()
grid.add_initial_state('##.#.####..#####..#.....##....#.#######..#.#...........#......##...##.#...####..##.#..##.....#..####')
print(len(grid.initial_state))
grid.calc_initial_state()
inputs = [
'#..#. => #'
,'.###. => .'
,'..##. => .'
,'....# => .'
,'#...# => .'
,'.#.#. => .'
,'#.#.# => #'
,'#.... => .'
,'#.#.. => #'
,'###.# => .'
,'.#... => #'
,'#.### => .'
,'.#.## => #'
,'..#.. => #'
,'.#### => .'
,'..### => #'
,'...#. => .'
,'##.#. => #'
,'##.## => #'
,'.##.# => #'
,'###.. => .'
,'..#.# => .'
,'...## => #'
,'##... => #'
,'##### => .'
,'#.##. => .'
,'.#..# => #'
,'##..# => .'
,'..... => .'
,'####. => #'
,'#..## => .'
,'.##.. => #'
]

for value in inputs:
    grid.add_input(value)

for g in range(20):
    grid.do_generation()
#grid.print_table()

grid.calc_answer()

