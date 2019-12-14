#### Day 12: The N-Body Problem ####

class Moon():
    def __init__(self, position):
        self.position = position
        self.velocity = tuple(0 for _ in range(len(position)))
        self.gravity = (0, 0, 0)

    def update_position(self):
        self.position = tuple(sum(i) for i in zip(self.position, self.velocity))

    def update_velocity(self):
        self.velocity = tuple(sum(i) for i in zip(self.velocity, self.gravity))

    def get_energy(self):
        pot = sum(abs(i) for i in self.position)
        kin = sum(abs(i) for i in self.velocity)
        return pot * kin

class Jupiter():
    def __init__(self):
        self.moons = []
        with open('input.txt', 'r') as file:
            for i, line in enumerate(file):
                line = line.rstrip()
                line = line[1:-1]
                positions = line.split(', ')
                position = tuple(int(i.split('=')[1]) for i in positions)
                self.moons.append(Moon(position))
        self.snapshots = set()

    def print_moons(self):
        for moon in self.moons:
            print(moon.position, moon.velocity)

    def sim(self):
        gravity_tuples = []
        for moon_1 in self.moons:
            gravity = (0, 0, 0)
            for moon_2 in self.moons:
                if moon_1.position == moon_2.position:
                    continue
                gravity_temp = []
                for i in range(len(moon_1.position)):
                    if moon_1.position[i] < moon_2.position[i]:
                        gravity_temp.append(1)
                    elif moon_1.position[i] > moon_2.position[i]:
                        gravity_temp.append(-1)
                    else:
                        gravity_temp.append(0)
                gravity_temp = tuple(gravity_temp)
                gravity = tuple(sum(i) for i in zip(gravity, gravity_temp))
            moon_1.gravity = gravity

        for moon in self.moons:
            moon.update_velocity()
            moon.update_position()

        if self.get_cur_snapshot() in self.snapshots:
            return True
        else:
            self.add_snapshot()
            return False
        
    def get_total_energy(self):
        total_energy = 0
        for moon in self.moons:
            total_energy += moon.get_energy()
        return total_energy

    def add_snapshot(self):
        self.snapshots.add(self.get_cur_snapshot())

    def get_cur_snapshot(self):
        new_snapshot = ""
        for moon in self.moons:
            new_snapshot += f"{moon.position}{moon.velocity}"
        return new_snapshot

## Part One ##
# jupiter = Jupiter()
# for i in range(10):
#     jupiter.sim()

# print(jupiter.get_total_energy())

## Part Two ##
import numpy as np
class Universe():
    def __init__(self):
        self.p = []
        with open('input.txt', 'r') as file:
            for i, line in enumerate(file):
                line = line.rstrip()
                line = line[1:-1]
                positions = line.split(', ')
                positions = [int(pos.split('=')[1]) for pos in positions]
                self.p.append(positions)

        self.v = [[0 for i in range(3)] for j in range(4)]

        self.dim_steps = [0, 0, 0]

    # def sort_dimensions(self):
    #     for dim in self.dimensions:
    #         dim.sort(key = lambda x: x[0])

    def print_moons(self):
        for i in self.p:
            print(i)

    def add_gravity_to_v(self, positions: list, velocities: list):
        gravity = []
        # print(positions)
        # print(velocities)
        for i, p1 in enumerate(positions):
            negs = 0
            posi = 0
            for j, p2 in enumerate(positions):
                if p2 < p1:
                    negs += 1
                elif p2 > p2:
                    posi += 1
            gravity.append(posi - negs)

        print(gravity)
        return list(np.array(gravity) + np.array(velocities))

    def sim_step(self, positions, velocities):
        velocities = self.add_gravity_to_v(positions, velocities)
        positions = list(np.array(positions) + np.array(velocities))
        return positions, velocities

    def sim_dim(self, dim_index: int):
        positions = self.p[dim_index]
        velocities = self.v[dim_index]
        states = set()
        seen = False
        count = 1
        while self.get_state_hash(positions, velocities) not in states:
            states.add(self.get_state_hash(positions, velocities))
            positions, velocities = self.sim_step(positions, velocities)
        self.dim_steps[dim_index] = count
        del(states)

        # if self.get_state_hash() in self.states:
        #     return True
        # else:
        #     self.states.add(self.get_state_hash())
        #     return False

    def get_state_hash(self, p, v):
        return hash(f"{str(p)}{str(v)}")

    # def sim(self):
    #     for dim in self.dimensions:
    #         for i, pos in enumerate(dim):
    #             negs = len(['' for j in dim[:i] if j[0] != pos[0]])
    #             post = len(['' for j in dim[i+1:] if j[0] != pos[0]])
    #             pos[1] += post - negs
    #         for pos in dim:
    #             pos[0] += pos[1]
    #     self.sort_dimensions()

    #     if str(self.dimensions) in self.snapshots:
    #         return True
    #     else:
    #         self.snapshots.add(str(self.dimensions))
    #         return False
        
    #     total = 0
    #     for pot, kin in zip(pots, kins):
    #         total += pot * kin
    #     return total

universe = Universe()
print(universe.p)
print(universe.v)
p = universe.p[0]
v = universe.v[0]
for i in range(1, 11):
    p, v = universe.sim_step(p, v)
    print("step "+str(i))
    # print(p)
    print(v)

    
# seen = False
# count = 1 
# while True:
#     if count % 10000 == 0:
#         print(count)

#     seen = universe.sim()
#     if seen:
#         break
#     else:
#         count += 1
    
# print(count)

