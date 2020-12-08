### Day 7: Amplification Circuit ###

from itertools import permutations

class IntcodeComputer:
    def __init__(self, intcode: list, phase_setting: int):
        self.intcode = intcode
        self.pointer = 0
        self.halted = False

        self.phase_setting = phase_setting
        self.used_phase_setting = False

        self.output_signal = None
        self.opcode_params = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            99: 0
        }

    def read_instruction(self, inst: int) -> (int, list):
        """
        :returns: (opcode, mode per parameter)
        """
        inst = str(inst)
        opcode = int(inst[-2:])
        inst = inst[:-2]

        modes = []
        for i in range(self.opcode_params[opcode]):
            if inst == '':
                modes.append(0)
            else:
                modes.append(int(inst[-1:]))
                inst = inst[:-1]
        return opcode, modes

    def get_val(self, param: int, mode: int) -> int:
        if mode == 0:
            return self.intcode[param]
        elif mode == 1:
            return param


    def run_intcode(self, input_signal: int):
        if self.halted:
            return self.output_signal

        while True:
            opcode, modes = self.read_instruction(self.intcode[self.pointer])
            
            if opcode == 1: # add
                param_1, mode_1 = self.intcode[self.pointer + 1], modes[0]
                param_2, mode_2 = self.intcode[self.pointer + 2], modes[1]
                param_3, mode_3 = self.intcode[self.pointer + 3], modes[2]

                val_1 = self.get_val(param_1, mode_1)
                val_2 = self.get_val(param_2, mode_2)

                if mode_3 == 0:
                    self.intcode[param_3] = val_1 + val_2
                elif mode_3 == 1:
                    incode[self.pointer + 3] = val_1 + val_2

                self.pointer += 4

            elif opcode == 2: # multiply
                param_1, mode_1 = self.intcode[self.pointer + 1], modes[0]
                param_2, mode_2 = self.intcode[self.pointer + 2], modes[1]
                param_3, mode_3 = self.intcode[self.pointer + 3], modes[2]

                val_1 = self.get_val(param_1, mode_1)
                val_2 = self.get_val(param_2, mode_2)

                if mode_3 == 0:
                    self.intcode[param_3] = val_1 * val_2
                elif mode_3 == 1:
                    self.intcode[self.pointer + 3] = val_1 * val_2

                self.pointer += 4

            elif opcode == 3: # input
                param_1, mode_1 = self.intcode[self.pointer + 1], modes[0]
                if not self.used_phase_setting:
                    value = self.phase_setting
                    self.used_phase_setting = True
                else:
                    value = input_signal

                if mode_1 == 0:
                    self.intcode[param_1] = value
                elif mode_1 == 1:
                    self.intcode[self.pointer + 1] = value
                self.pointer += 2

            elif opcode == 4: # output
                param_1, mode_1 = self.intcode[self.pointer + 1], modes[0]
                
                if mode_1 == 0:
                    value = self.intcode[param_1]
                elif mode_1 == 1:
                    value = param_1
                print(f"opcode 4 output: {value}")
                self.output_signal = value
                self.pointer += 2
                return self.output_signal

            elif opcode == 5: # jump-if-true
                param_1, mode_1 = self.intcode[self.pointer + 1], modes[0]
                param_2, mode_2 = self.intcode[self.pointer + 2], modes[1]

                val_1 = self.get_val(param_1, mode_1)
                val_2 = self.get_val(param_2, mode_2)
                if val_1 is not 0:
                    self.pointer = val_2
                else:
                    self.pointer += 3

            elif opcode == 6: # jump-if-false
                param_1, mode_1 = self.intcode[self.pointer + 1], modes[0]
                param_2, mode_2 = self.intcode[self.pointer + 2], modes[1]

                val_1 = self.get_val(param_1, mode_1)
                val_2 = self.get_val(param_2, mode_2)

                if val_1 is 0:
                    self.pointer = val_2
                else:
                    self.pointer += 3
            
            elif opcode == 7: # less than
                param_1, mode_1 = self.intcode[self.pointer + 1], modes[0]
                param_2, mode_2 = self.intcode[self.pointer + 2], modes[1]
                param_3, mode_3 = self.intcode[self.pointer + 3], modes[2]

                val_1 = self.get_val(param_1, mode_1)
                val_2 = self.get_val(param_2, mode_2)
                
                if val_1 < val_2:
                    val = 1
                else:
                    val = 0

                if mode_3 == 0:
                    self.intcode[param_3] = val
                elif mode_3 == 1:
                    self.intcode[self.pointer + 3] = val
                self.pointer += 4

            elif opcode == 8: # equals
                param_1, mode_1 = self.intcode[self.pointer + 1], modes[0]
                param_2, mode_2 = self.intcode[self.pointer + 2], modes[1]
                param_3, mode_3 = self.intcode[self.pointer + 3], modes[2]

                val_1 = self.get_val(param_1, mode_1)
                val_2 = self.get_val(param_2, mode_2)
                
                if val_1 == val_2:
                    val = 1
                else:
                    val = 0
                    
                if mode_3 == 0:
                    self.intcode[param_3] = val
                elif mode_3 == 1:
                    self.intcode[self.pointer + 3] = val
                self.pointer += 4

            elif opcode == 99:
                print('HALT')
                self.halted = True
                return self.output_signal
            
            else:
                print('not a valid opcode')
                return

    def run_intcode_until_halt(self, input_signal: int):
        self.input_signal = input_signal
        while not self.halted:
            print(self.phase_setting, self.input_signal, self.pointer)
            self.process_next_instruction()
        return self.output_signal

    def run_intcode_until_output(self, input_signal: int):
        self.input_signal = input_signal
        prev_output = self.output_signal
        while not self.halted:
            print(self.phase_setting, self.input_signal, self.pointer)
            self.process_next_instruction()

            if self.output_signal != prev_output:
                return self.output_signal

og_intcode = []
with open('input.txt', 'r') as problem_input:
    for i, line in enumerate(problem_input):
        og_intcode = [int(val) for val in line.split(",")]

## Part 1 ##
# outputs = []
# for perm in permutations([0, 1, 2, 3, 4]):
#     input_signal = 0
#     for phase_setting in perm:
#         cur_comp = IntcodeComputer(list(og_intcode), phase_setting)
#         input_signal = cur_comp.run_intcode(input_signal)
#     outputs.append(input_signal)

# print(max(outputs))

## Part 2 - Feedback loop mode ##

outputs = []
for perm in permutations([9, 8, 7, 6, 5]):
    computers = []
    for phase in perm:
        comp = IntcodeComputer(list(og_intcode), phase)
        computers.append(comp)

    input_signal = 0
    while not computers[-1].halted:
        for comp in computers:
            input_signal = comp.run_intcode(input_signal)
    outputs.append(input_signal)

print(max(outputs))
