import os
from aoc_utils import aoc_utils
from collections import defaultdict
from dataclasses import dataclass
import re
from typing import List
from itertools import product
import concurrent.futures

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    {'level': 1, 'input': '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1''', 'output': 21},
    {'level': 2, 'input': '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1''', 'output': 525152},
]


@dataclass
class Row:
    condition_record: List[str]
    damaged_groups: List[int]

    def number_of_arrangements(self, folds: int) -> int:
        # print(f"number_of_arrangements, {self.condition_record}, {self.damaged_groups}")

        base_num_arrangements = self.get_valid_arrangements_for_record(self.condition_record)

        starts_with_finished_group = ''.join(self.condition_record).startswith('#' * self.damaged_groups[0])
        ends_with_finished_group = ''.join(self.condition_record).endswith('#' * self.damaged_groups[-1])

        # if starts_with_finished_group and ends_with_finished_group:
        #     return base_num_arrangements**folds
        
        if ends_with_finished_group:
            return base_num_arrangements * self.get_valid_arrangements_for_record(self.condition_record + ['?'])**(folds-1)
        
        # if starts_with_finished_group:
        #     return base_num_arrangements * self.get_valid_arrangements_for_record(['?'] + self.condition_record)**(folds-1)

        option1_num_arrangements = self.get_valid_arrangements_for_record(['?'] + self.condition_record)
        option2_num_arrangements = self.get_valid_arrangements_for_record(self.condition_record + ['?'])
        # print(''.join(self.condition_record), self.damaged_groups)
        # print(base_num_arrangements, option1_num_arrangements, option1_num_arrangements)
        # print()

        return base_num_arrangements * max(option1_num_arrangements, option2_num_arrangements)**(folds-1)

    def get_valid_arrangements_for_record(self, record: List[str]) -> int:
        # print()
        # print(f"    get_valid_ar", record)
        num_wildcards = record.count('?')
        all_wildcard_combinations = list(product(['.', '#'], repeat=num_wildcards))

        total_valid_arrangements = 0
        for combo in all_wildcard_combinations:
            combo = list(combo)
            new_record = record.copy()

            while len(combo) > 0:
                new_char = combo.pop(0)
                left_most_wild_index = new_record.index('?')
                new_record[left_most_wild_index] = new_char

            if self.record_matches_damaged_groups(new_record):
                total_valid_arrangements += 1
                # print(f"{new_record=}")
        return total_valid_arrangements

    def record_matches_damaged_groups(self, record: str) -> bool:
        record_groups = ''.join(record).split('.')
        record_groups = [g for g in record_groups if g != '']

        if len(record_groups) != len(self.damaged_groups):
            return False

        for i, g in enumerate(record_groups):
            try:
                if len(g) != self.damaged_groups[i]:
                    return False
            except IndexError:
                return False

        return True


def answer(problem_input, level, test=None):
    rows = []
    for line in problem_input.split('\n'):
        line = line.strip()
        condition_record, damaged_groups = line.split(' ')
        row = Row(condition_record=list(condition_record),
                  damaged_groups=list(map(int, damaged_groups.split(','))))
        rows.append(row)

    if level == 1:
        arrangement_lens = [row.number_of_arrangements(folds=1) for row in rows]
        # print(f"{arrangement_lens=}")
        return sum(arrangement_lens)

    elif level == 2:
        # row = Row(condition_record=list('?###????????'), damaged_groups=[3,2,1])
        # print(row.number_of_arrangements(folds=1))

        # row = Row(condition_record=list('??###????????'), damaged_groups=[3,2,1])
        # print(row.number_of_arrangements(folds=1))

        # row = Row(condition_record=list('?###?????????'), damaged_groups=[3,2,1])
        # print(row.number_of_arrangements(folds=1))

        # row = Row(condition_record=list('.??..??...?##.'), damaged_groups=[1,1,3])
        # print(row.number_of_arrangements(folds=1))

        # row = Row(condition_record=list('?.??..??...?##.'), damaged_groups=[1,1,3])
        # print(row.number_of_arrangements(folds=1))

        # row = Row(condition_record=list('.??..??...?##.?'), damaged_groups=[1,1,3])
        # print(row.number_of_arrangements(folds=1))

        # row = Row(condition_record=list('???.###'), damaged_groups=[1, 1, 3])
        # print(row.number_of_arrangements(folds=5))


        def run(row):
            return row.number_of_arrangements(folds=5)

        # Number of threads to use
        num_threads = 100  # You can adjust this based on your system and requirements

        s = 0
        # Using ThreadPoolExecutor for parallel execution
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            # Submit tasks to the executor
            future_to_data = {executor.submit(run, row): row for row in rows}

            # Retrieve results as they become available
            for future in concurrent.futures.as_completed(future_to_data):
                data = future_to_data[future]
                try:
                    result = future.result()
                    s += result
                    # Process the result as needed
                    print(f"Task for data {data} completed with result: {result}")
                except Exception as e:
                    # Handle exceptions if any
                    print(f"Task for data {data} encountered an exception: {e}")
        return s
        # arrangement_lens = []
        # print(len(rows))
        # for i, row in enumerate(rows):
        #     print(i + 1)
        #     arrangement_lens.append(row.number_of_arrangements(folds=5))
        # return sum(arrangement_lens)


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
