### Day 11: Space Police ###

from intcode_computer import IntcodeComputer

og_intcode = []
with open('input.txt', 'r') as problem_input:
    for i, line in enumerate(problem_input):
        og_intcode = [int(val) for val in line.split(",")]

class PaintingRobot(IntcodeComputer):
    def __init__(self, intcode: list, starting_color: int):
        super().__init__(intcode, starting_color)
        self.direction = 1
        self.cords = (0, 0)
        self.direction_delta = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
        self.panels = {}

    def change_direction(self, direction_code: int):
        if direction_code == 0:
            self.direction = (self.direction + 1) % 4
        elif direction_code == 1:
            self.direction = (self.direction - 1) % 4

    def move_forward(self):
        x = self.cords[0] + self.direction_delta[self.direction][0]
        y = self.cords[1] + self.direction_delta[self.direction][1]
        self.cords = (x, y)

    def run_path(self, input_signal: int = 0):
        output_num = 1
        while not self.halted:
            output = self.run_intcode(input_signal)
            if output_num == 1:
                self.panels[self.cords] = output
                output_num = 2
            elif output_num == 2:
                self.change_direction(output)
                self.move_forward()
                if self.cords in self.panels:
                    input_signal = self.panels[self.cords]
                else:
                    input_signal = 0
                output_num = 1

    def print_panels(self):
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        for x, y in self.panels.keys():
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
        
        for y in reversed(range(min_y, max_y + 1)):
            for x in range(min_x, max_x + 1):
                if (x, y) in self.panels:
                    char = 'X' if self.panels[(x, y)] == 1 else ' '
                else:
                    char = ' '
                print(char, end='')
            print('')
        
## Part 1 ##
robot = PaintingRobot(list(og_intcode), 0) # starts on a black
robot.run_path(0)
print("Part 1: " + str(len(robot.panels)))

## Part 2 ##
robot2 = PaintingRobot(list(og_intcode), 1) # starts on a white
robot2.run_path(1) 
print("Part 2: ")
robot2.print_panels()
