# (raw code)
# Part 1


def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])


class Mine:
    def __init__(self):
        self.map_without_carts = []
        self.map_with_carts = []
        self.carts = []
        self.time = 0
        self.cart_counter = 0
        self.print_progress = False

    def move_carts(self):
        for cart in self.carts:
            cart.move_cart()
            cart.update_direction(self.map_without_carts[cart.pos_y][cart.pos_x])
            for other_cart in self.carts:
                if other_cart.number_tag == cart.number_tag:
                    pass  # Same cart
                else:
                    has_crashed_happen = cart.has_crashed(other_cart)
                    if has_crashed_happen:
                        self.time += 1
                        cart.direction = 'x'
                        other_cart.direction = 'x'
                        print('Time = ' + str(self.time))
                        print('Pos_x = ' + str(cart.pos_x) + ', Pos_y = ' + str(cart.pos_y))
                        self.print_map_with_carts()
                        return False
        self.time += 1
        return True

    def print_map_with_carts(self):
        self.map_with_carts = self.map_without_carts.copy()
        for cart in self.carts:
            self.map_with_carts[cart.pos_y] = replace_str_index(self.map_with_carts[cart.pos_y], cart.pos_x, cart.direction)
            #self.map_with_carts[cart.pos_y].[cart.pos_x] = cart.direction

        for map_line in self.map_with_carts:
            print(map_line)

    def add_line_to_map(self, map_line):
        clean_map_line = map_line
        clean_map_line = clean_map_line.replace('<', '-').replace('>', '-').replace('v', '|').replace('^', '|')

        self.map_without_carts.append(clean_map_line)
        self.map_with_carts.append(map_line)

    def initiate_carts(self):
        for pos_y in range(len(self.map_with_carts)):
            for pos_x in range(len(self.map_with_carts[pos_y])):
                value = self.map_with_carts[pos_y][pos_x]
                if value == '<' or value == '>' or value == '^' or value == 'v':
                    new_cart = Cart(pos_x, pos_y, value, self.cart_counter)
                    self.cart_counter += 1
                    self.carts.append(new_cart)

    def run_mine(self):
        if self.print_progress:
            for map_line in self.map_without_carts:
                print(map_line)
            for map_line in self.map_with_carts:
                print(map_line)
        self.initiate_carts()
        mine_is_running = True
        while mine_is_running: # and self.time < 14:
            mine_is_running = self.move_carts()
            if self.print_progress:
                self.print_map_with_carts()

    def print_map_without_carts(self):
        for map_line in self.map_without_carts:
            print(map_line)


class Cart:
    def __init__(self, x, y, direction, number_tag):
        self.pos_x = x
        self.pos_y = y
        self.direction = direction
        self.inter_section_option = 0
        self.number_tag = number_tag

    def has_crashed(self, another_cart):
        if self.pos_x == another_cart.pos_x and self.pos_y == another_cart.pos_y:
            return True
        return False

    def update_direction(self, map_part):
        if map_part == '+':
            self.inter_sect_direction()
        elif map_part == '/':
            self.normal_turn()
        elif map_part == '\\':
            self.abnormal_turn()
        else:
            print(map_part)

    def normal_turn(self):  # /
        if self.direction == '<':
            self.turn_left()
        elif self.direction == '>':
            self.turn_left()
        elif self.direction == 'v':
            self.turn_right()
        elif self.direction == '^':
            self.turn_right()

    def abnormal_turn(self):  # \
        if self.direction == '<':
            self.turn_right()
        elif self.direction == '>':
            self.turn_right()
        elif self.direction == 'v':
            self.turn_left()
        elif self.direction == '^':
            self.turn_left()

    def inter_sect_direction(self):
        if self.inter_section_option == 0:
            self.turn_left()
        if self.inter_section_option == 1:
            pass  # straight is the same direction
        if self.inter_section_option == 2:
            self.turn_right()

        self.inter_section_option = (self.inter_section_option + 1) % 3

    def turn_left(self):
        if self.direction == '<':
            self.direction = 'v'
        elif self.direction == '>':
            self.direction = '^'
        elif self.direction == '^':
            self.direction = '<'
        elif self.direction == 'v':
            self.direction = '>'

    def turn_right(self):
        if self.direction == '<':
            self.direction = '^'
        elif self.direction == '>':
            self.direction = 'v'
        elif self.direction == '^':
            self.direction = '>'
        elif self.direction == 'v':
            self.direction = '<'

    def move_cart(self):
        if self.direction == '<':
            self.move_left()
        elif self.direction == '>':
            self.move_right()
        elif self.direction == '^':
            self.move_up()
        elif self.direction == 'v':
            self.move_down()

    def move_up(self):
        self.pos_y += -1

    def move_down(self):
        self.pos_y += 1

    def move_left(self):
        self.pos_x += -1

    def move_right(self):
        self.pos_x += 1


mine = Mine()
file = open("test_values.txt", "r")
lines = file.readlines()
for line in lines:
    line = line.replace('\n', '')
    mine.add_line_to_map(line)

mine.print_progress = True
mine.run_mine()

#file = open("values.txt", "r")
#lines = file.readlines()
#for line in lines:
#    print(line)

mine = Mine()
file = open("values.txt", "r")
lines = file.readlines()
for line in lines:
    line = line.replace('\n', '')
    mine.add_line_to_map(line)

#mine.print_progress = True
mine.run_mine()
