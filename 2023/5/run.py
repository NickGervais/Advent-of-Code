import os
from aoc_utils import aoc_utils
from dataclasses import dataclass
import re
from typing import List


year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''seeds:
79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4''', 'output': 35},
    {'level': 2, 'input': '''seeds:
79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4''', 'output': 46},
]


@dataclass
class Convertion:
    dest_start: int
    src_start: int
    range_len: int

    def src_in(self, src_num: int) -> bool:
        return self.src_start <= src_num <= self.src_start + self.range_len


def get_dest_num(map_group: List[Convertion], src_num: int) -> int:
    for conv in map_group:
        if conv.src_in(src_num):
            delta = abs(conv.src_start - src_num)
            return conv.dest_start + delta
    return src_num


def answer(problem_input, level, test=None):
    seeds = []
    maps = []

    raw_maps = problem_input.split('\n\n')
    for i, rm in enumerate(raw_maps):
        lines = rm.split('\n')
        raw_map_header = lines.pop(0)
        print(raw_map_header)
        if i == 0:
            seeds = list(map(int, lines[0].strip().split(' ')))
            print(seeds)
            continue

        # map_name = re.match(r'(?P<map_name>[^ map\n]*)(?:\smap)?:', lines.pop(0)).group('map_name')
        # print(map_name)

        map_group = []
        for line in lines:
            nums = list(map(int, line.strip().split(' ')))
            map_group.append(Convertion(
                dest_start=nums[0],
                src_start=nums[1],
                range_len=nums[2]
            ))
        maps.append(map_group)

    if level == 1:
        final_dest_nums = []

        for seed in seeds:
            dest_num = seed
            for map_group in maps:
                dest_num = get_dest_num(map_group, dest_num)
            final_dest_nums.append(dest_num)

        return min(final_dest_nums)

    elif level == 2:
        seed_pairs = list(zip(seeds[::2], seeds[1::2]))
        # new_seeds = []
        # for start, length in seed_pairs:
        #     new_seeds.extend(list(range(start, start + length)))
        # seeds = new_seeds
        # print('new_seeds', len(seeds))

        end_location_maps = maps.pop(-1)
        end_location_nums = []
        for conv in end_location_maps:
            end_location_nums.extend(list(range(conv.dest_start, conv.dest_start + conv.range_len)))

        print('end_location_nums', len(end_location_nums))

        reversed_maps = []
        for map_group in reversed(maps):
            new_map_group = []
            for conv in map_group:
                new_map_group.append(Convertion(
                    dest_start=conv.src_start,
                    src_start=conv.dest_start,
                    range_len=conv.range_len
                ))
            print(new_map_group)
            reversed_maps.append(new_map_group)

        print(sorted(end_location_nums))
        for i, loc_num in enumerate(sorted(end_location_nums)):
            # if i % 1000:
            #     print(i)

            dest_num = loc_num
            for map_group in maps:
                print(dest_num)
                dest_num = get_dest_num(map_group, dest_num)

            print()

            for start, length in seed_pairs:
                if start <= dest_num <= start + length:
                    return loc_num



aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
