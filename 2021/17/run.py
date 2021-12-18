import os
from aoc_utils import aoc_utils
from collections import defaultdict
import time

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

def calc_if_hits(velocity, x_target, y_target):
    position = [0, 0]
    has_hit = False
    while position[1] >= y_target[0]:
        if x_target[0] <= position[0] <= x_target[1] and y_target[0] <= position[1] <= y_target[1]:
            has_hit = True
            break

        position[0] += velocity[0]
        position[1] += velocity[1]
        if velocity[0] > 0:
            velocity[0] -= 1
        elif velocity[0] < 0:
            velocity[0] += 1
        velocity[1] -= 1
    return has_hit

def calc_min_x_velocity(x_target: list):
    check_vel = 0
    while True:
        step = 0
        pos_x = 0
        prev_pos_x = -1
        x_vel = check_vel
        while prev_pos_x != pos_x:
            prev_pos_x = pos_x
            pos_x += x_vel
            step += 1
            if x_vel > 0:
                x_vel -= 1
            elif x_vel < 0:
                x_vel += 1
        
        if x_target[0] <= pos_x <= x_target[1]:
            break
        check_vel += 1
    return check_vel, pos_x, step 
        


def answer(problem_input, level, test=None):
    line = problem_input.split('\n')[0].strip()
    line = line.replace('target area: ', '')
    x_range, y_range = line.split(', ')
    x_range = x_range.replace('x=', '')
    y_range = y_range.replace('y=', '')

    x_range = [int(i) for i in x_range.split('..')]
    y_range = [int(i) for i in y_range.split('..')]

    if level == 1:
        # calc_trajectory([6, 3], 10)
        min_x_vel, stop_x, steps_taken = calc_min_x_velocity(x_range)

        check_y_vel = 0
        highest = (None, float('-inf'))
        while True:
            y_vel = check_y_vel
            pos_y = 0
            highest_pos_reached = float('-inf')
            hit_target = False
            while pos_y > y_range[0]: # continue if it's above the bottom of target
                pos_y += y_vel
                if pos_y > highest_pos_reached:
                    highest_pos_reached = pos_y
                if y_range[0] <= pos_y <= y_range[1]:
                    hit_target = True
                y_vel -= 1
            if highest_pos_reached > highest[1] and hit_target:
                highest = (check_y_vel, highest_pos_reached)
                print('end:', (min_x_vel, highest[0]), highest[1])
            # time.sleep(0.5)

            check_y_vel += 1
    elif level == 2:
        # find all x velocities that make it to target.
        # all_x_velocities = []
        # check_vel = 1
        # while check_vel <= x_range[1]:
        #     pos_x = 0
        #     x_vel = check_vel
        #     while pos_x < x_range[1] and x_vel > 0:
        #         pos_x += x_vel

        #         if x_range[0] <= pos_x <= x_range[1]:
        #             all_x_velocities.append(check_vel)
        #             break

        #         if x_vel > 0:
        #             x_vel -= 1
        #         elif x_vel < 0:
        #             x_vel += 1
        
        #     check_vel += 1
        # print(all_x_velocities)
        # test results = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        all_x_velocities = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164]


        # all_y_velocities = []
        # check_y_vel = y_range[0]
        # while True:
        #     # print('check_y_vel', check_y_vel)
        #     pos_y = 0
        #     y_vel = check_y_vel
        #     while pos_y >= y_range[0]:
        #         # print('    ', y_range[0], pos_y,  y_range[1])
        #         # time.sleep(0.5)
        #         if y_range[0] <= pos_y <= y_range[1]:
        #             all_y_velocities.append(check_y_vel)
        #             break

        #         pos_y += y_vel

        #         y_vel -= 1
        
        #     check_y_vel += 1
        #     print('CUR RESULTS:', all_y_velocities)
        # test = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        all_y_velocities = [-140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]

        # print(calc_if_hits([23, -10], x_range, y_range))
        all_hits = []
        for y in all_y_velocities:
            for x in all_x_velocities:
                velocity = [x, y]
                if calc_if_hits(velocity, x_range, y_range):
                    all_hits.append((x, y))

        # print(all_hits)
        return len(all_hits)

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
