# (raw code)
# Part 1


class Grid:
    def __init__(self):
        n = 400
        m = 400
        self.grid = [[0 for col in range(n)] for row in range(m)]
        self.grid_part2 = [[0 for col in range(n)] for row in range(m)]
        self.coordinate_list = {}
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ'
        self.id_list = [bokstav for bokstav in alphabet]
        for bokstav in alphabet:
            self.id_list.append(bokstav + bokstav)
        self.id_number = 0
        self.coordinate_id = self.id_list[self.id_number]
        self.calculated_id_space = {}

    def set_next_id(self):
        self.id_number += 1
        self.coordinate_id = self.id_list[self.id_number]

    def add_coordinates(self, x, y):
        self.coordinate_list.update({self.coordinate_id: (x, y)})
        self.grid[x][y] = self.coordinate_id
        self.set_next_id()

    def print_grid(self):
        for i in range(len(self.grid)):
            print(self.grid[i])

    def calc_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                # Calc each space
                min_distance = 1000
                points = []
                for point in self.coordinate_list:
                    point_x = self.coordinate_list.get(point)[0]
                    point_y = self.coordinate_list.get(point)[1]
                    distance_to_grid_box = calc_distance(point_x, point_y, i, j)
                    if distance_to_grid_box == min_distance:
                        points.append(point)
                    elif distance_to_grid_box < min_distance:
                        points = [point]
                        min_distance = distance_to_grid_box

                if len(points) > 1:
                    self.grid[i][j] = '.'
                elif len(points) == 1:
                    self.grid[i][j] = str(points[0]).lower()

    def calc_id_space(self):
        self.calculated_id_space = {}
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                value = self.grid[i][j]
                is_infinite = False
                # if on edge -> inf?
                if i == 0 or j == 0 or i == (len(self.grid)-2) or j == (len(self.grid[i])-2):
                    is_infinite = True
                if value != 0 or value != '.':
                    point_value = self.calculated_id_space.get(value)
                    if point_value is None:
                        point_value = 0
                    else:
                        point_value, test_inf = self.calculated_id_space.get(value)
                        if test_inf:
                            is_infinite = True
                    point_value += 1
                    self.calculated_id_space.update({value: [point_value, is_infinite]})

    def get_max_space(self):
        self.calc_id_space()
        max_value = 0
        point_tag = []
        for point in self.calculated_id_space:
            point_value, is_infinite = self.calculated_id_space.get(point)
            if not is_infinite:
                if point_value > max_value:
                    max_value = point_value
                    point_tag = [point]
                elif point_value == max_value:
                    point_tag.append(point)
        return [point_tag, max_value]

    def calc_grid_part_2(self):
        manhattan_distance = 10000
        sum_space = 0
        for i in range(len(self.grid_part2)):
            for j in range(len(self.grid_part2[i])):
                total_distance = 0
                okay_point = True
                for point in self.coordinate_list:
                    if okay_point:
                        point_x = self.coordinate_list.get(point)[0]
                        point_y = self.coordinate_list.get(point)[1]
                        total_distance += calc_distance(i, j, point_x, point_y)
                        if total_distance > manhattan_distance:
                            okay_point = False
                if okay_point:
                    sum_space += 1
                self.grid_part2[i][j] = int(okay_point)
        return sum_space

    def print_grid_part_2(self):
        for i in range(len(self.grid_part2)):
            print(self.grid_part2[i])

    def calc_sum_grid_part_2(self):
        sum_space = 0
        for i in range(len(self.grid_part2)):
            for j in range(len(self.grid_part2[i])):
                sum_space += self.grid_part2[i][j]
        print(sum_space)


def calc_distance(c, d, a, b):
    return abs(c - a) + abs(d - b)


file = open("values.txt", "r")
coordinates = file.readlines()

grid = Grid()

for coordinate in coordinates:
    x, y = coordinate.replace('\n', '').split(', ')
    x = int(x)
    y = int(y)
    # print('x=' + str(x) + ', y=' + str(y))
    grid.add_coordinates(x, y)

grid.calc_grid()
#grid.print_grid()
#print(grid.get_max_space())

print(grid.calc_grid_part_2())
grid.print_grid_part_2()
grid.calc_sum_grid_part_2()
