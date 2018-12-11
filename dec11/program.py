# (raw code)
# Part 1


class Grid:
    def __init__(self):
        size = 300
        self.grid = [[0 for col in range(size)] for row in range(size)]
        self.serial = 0

    def enter_serial(self, serial):
        self.serial = serial
        self.calc_grid()

    def calc_grid(self):
        x_values = range(300)
        y_values = range(300)
        for y in y_values:
            for x in x_values:
                self.grid[x][y] = self.calc_point(x, y)

    def calc_point(self, x, y):
        rack_id = 10 + x
        power_level = rack_id * y
        adding_serial = power_level + self.serial
        multiplying_rack_id = adding_serial * rack_id
        if len(str(multiplying_rack_id)) < 3:
            hundred_value = 0
        else:
            hundred_value = int(str(multiplying_rack_id)[-3])
        answer = hundred_value - 5
        return answer

    def calc_power_grid(self):
        x_values = range(298)
        y_values = range(298)
        max_power = 0
        best_x = 0
        best_y = 0
        times = 0
        for y in y_values:
            for x in x_values:
                focus_grid_sum = 0
                for y_2 in range(3):
                    for x_2 in range(3):
                        focus_grid_sum += self.grid[x + x_2][y + y_2]
                if focus_grid_sum > max_power:
                    max_power = focus_grid_sum
                    best_x = x
                    best_y = y
                    times = 0
                elif focus_grid_sum == max_power:
                    times += 1

        if times > 0:
            print('*******')
            print('*******')
            print('*******')

        return [max_power, best_x, best_y]

    def do_test(self):
        save_serial = self.serial
        serials = [18, 42]
        answers = [29, 30]

        for i in range(len(serials)):
            self.enter_serial(serials[i])
            values = self.calc_power_grid()
            print('value=' + str(values[0]) + ':equal=' + str(answers[i]))
            print(values)
            self.print_power_grid_at(values[1], values[2])

        # test 2
        serials = [8, 57, 39, 71]
        points = [(3, 5), (122, 79), (217, 196), (101, 153)]
        answers = [4, -5, 0, 4]
        for i in range(len(serials)):
            self.enter_serial(serials[i])
            print('Powercell=' + str(self.grid[points[i][0]][points[i][1]]) + ', answer=' + str(answers[i]))

        self.serial = save_serial

    def print_power_grid_at(self, x, y):
        print_grid = [[0 for col in range(5)] for row in range(5)]
        for y_2 in range(-1, 4):
            for x_2 in range(-1, 4):
                fuel_cell = self.grid[x + x_2][y + y_2]
                print_grid[y_2 + 1][x_2 + 1] = fuel_cell

        for row in print_grid:
            row_value = ''
            for column in row:
                row_value += ',' + str(column)
            print(row_value)

grid = Grid()
grid.enter_serial(9798)
grid.calc_grid()
result = grid.calc_power_grid()
print(result)
print(grid.grid[result[1]][result[2]])
grid.print_power_grid_at(result[1], result[2])
print('doing tests')
grid.do_test()
