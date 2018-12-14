# (raw code)
# Part 1


class Elf:
    def __init__(self, elf):
        self.index = elf - 1
        self.elf = elf

    def set_new_index(self, current_value, length_of_list):
        self.index = (self.index + current_value + 1) % length_of_list


class Board:
    def __init__(self):
        self.elves = [Elf(1), Elf(2)]
        self.list = [3, 7]
        self.number_of_recipes = 9

    def step(self):
        new_row = self.list.copy()
        new_recipe = new_row[self.elves[0].index] + new_row[self.elves[1].index]
        if new_recipe >= 10:
            new_row.append(1)
            new_recipe += -10
        new_row.append(new_recipe)
        self.elves[0].set_new_index(new_row[self.elves[0].index], len(new_row))
        self.elves[1].set_new_index(new_row[self.elves[1].index], len(new_row))
        self.list = new_row

    def print_board(self):
        for row in self.list:
            print(row)

    def check_stop(self):
        #print(len(self.list[-1]))
        #test = self.number_of_recipes + 10
        #print(test)
        if len(self.list) >= self.number_of_recipes + 10:
            if self.elves[0].index == self.number_of_recipes - 1:
                return False
        return True



board = Board()
board.number_of_recipes = 18

#for i in range(20):
#    board.step()

run_program = True
while run_program:
    board.step()
    run_program = board.check_stop()
#board.print_board()


#board.list[-1].pop(-1)
#answer = []
#for i in range(10):
#    test = board.list[-1].pop(-1)
#    answer.insert(0, test)

answer = board.list[board.number_of_recipes:(board.number_of_recipes+10)]

print(answer)

#board.print_board()
