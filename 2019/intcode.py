class IntcodeComputer:
    def __init__(self, intcode: list, phase_setting: int):
        self.intcode = intcode
        self.pointer = 0
        self.relative_base = 0
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
            9: 1,
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

    def expand_intcode(self):
        # double intcode size filling with 0
        self.intcode.extend([0 for _ in range(len(self.intcode))])

    def get_val(self, param: int, mode: int) -> int:
        if param >= len(self.intcode) or self.relative_base + param >= len(self.intcode):
            self.expand_intcode()

        if mode == 0:
            return self.intcode[param]
        elif mode == 1:
            return param
        elif mode == 2:
            return self.intcode[self.relative_base + param]
        
    def set_val(self, opcode: int, param: int, mode: int, value: int):
        num_params = self.opcode_params[opcode]
        if param >= len(self.intcode) or self.pointer + num_params >= len(self.intcode) or self.relative_base + param >= len(self.intcode):
            self.expand_intcode()

        if mode == 0:
            self.intcode[param] = value
        elif mode == 1:
            self.intcode[self.pointer + num_params] = value
        elif mode == 2:
            self.intcode[self.relative_base + param] = value

    def run_intcode(self, input_signal: int):
        if self.halted:
            return self.output_signal

        while True:
            opcode, modes = self.read_instruction(self.intcode[self.pointer])
            params = [self.intcode[self.pointer + i] for i in range(1,self.opcode_params[opcode] + 1)]
            if opcode == 1: # add
                values = [self.get_val(p, m) for p, m in zip(params[:-1], modes[:-1])]
                result = values[0] + values[1]
                self.set_val(opcode, params[-1], modes[-1], result)

                self.pointer += self.opcode_params[opcode] + 1

            elif opcode == 2: # multiply
                values = [self.get_val(p, m) for p, m in zip(params[:-1], modes[:-1])]
                result = values[0] * values[1]
                self.set_val(opcode, params[-1], modes[-1], result)

                self.pointer += self.opcode_params[opcode] + 1

            elif opcode == 3: # input
                if not self.used_phase_setting:
                    value = self.phase_setting
                    self.used_phase_setting = True
                else:
                    value = input_signal
                self.set_val(opcode, params[-1], modes[-1], value)
    
                self.pointer += self.opcode_params[opcode] + 1

            elif opcode == 4: # output
                value = self.get_val(params[0], modes[0])
                # print(f"opcode 4 output: {value}")
                self.output_signal = value
                self.pointer += self.opcode_params[opcode] + 1
                return self.output_signal

            elif opcode == 5: # jump-if-true
                values = [self.get_val(p, m) for p, m in zip(params, modes)]
                if values[0] is not 0:
                    self.pointer = values[1]
                else:
                    self.pointer += self.opcode_params[opcode] + 1

            elif opcode == 6: # jump-if-false
                values = [self.get_val(p, m) for p, m in zip(params, modes)]
                if values[0] is 0:
                    self.pointer = values[1]
                else:
                    self.pointer += self.opcode_params[opcode] + 1
            
            elif opcode == 7: # less than
                values = [self.get_val(p, m) for p, m in zip(params[:-1], modes[:-1])]
                if values[0] < values[1]:
                    result = 1
                else:
                    result = 0

                self.set_val(opcode, params[-1], modes[-1], result)
                self.pointer += self.opcode_params[opcode] + 1

            elif opcode == 8: # equals
                values = [self.get_val(p, m) for p, m in zip(params[:-1], modes[:-1])]
                if values[0] == values[1]:
                    result = 1
                else:
                    result = 0

                self.set_val(opcode, params[-1], modes[-1], result)
                self.pointer += self.opcode_params[opcode] + 1

            elif opcode == 9: # relative base offset
                value = self.get_val(params[0], modes[0])
                self.relative_base += value
                self.pointer += self.opcode_params[opcode] + 1

            elif opcode == 99:
                print('HALT')
                self.halted = True
                return self.output_signal
            
            else:
                print('not a valid opcode')
                return