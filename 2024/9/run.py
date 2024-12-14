import os
from collections import defaultdict
from dataclasses import dataclass
import re
import uuid

from pydantic import BaseModel

from aoc_utils import aoc_utils


script_dir = os.path.dirname(os.path.abspath(__file__))
day = os.path.basename(script_dir)
year = os.path.basename(os.path.dirname(script_dir))


test_cases = [
    {'level': 1, 'input': '''2333133121414131402''', 'output': 1928},
]


class File(BaseModel):
    id_: int
    size: int


class Disk(BaseModel):
    address: str
    size: int
    file: File | None


class DiskFragmenter(BaseModel):
    input_str: str
    disks: list[Disk]

    cur_disks: list[Disk]

    @property
    def rep_cur_state(self) -> str:
        s = ''
        for disk in self.disks:
            if disk.file:
                s += str(disk.file.id_) * disk.file.size
                remaining_space = disk.size - disk.file.size
                if remaining_space > 0:
                    s += '.' * (disk.size - disk.file.size)
            else:
                s += '.' * disk.size

        return s

    @property
    def checksum(self) -> int:
        s = self.rep_cur_state
        checksum_ = 0

        for i, char in enumerate(s):
            if char == '.':
                return checksum_

            checksum_ += i * int(char)
        return checksum_

    def move_file(self, disk_from: Disk, disk_to: Disk):
        assert disk_from.file, 'disk_from has no file'
        assert disk_to.file is None or disk_to.file.size < disk_to.size, 'disk_to is full'

        if disk_to.size == disk_from.size:
            # print('move: disk_to.size == disk_from.size')
            disk_to.file = disk_from.file
            disk_from.file = None

        elif disk_to.size < disk_from.file.size:
            # print('move: disk_to.size < disk_from.file.size')
            # fill free space with file
            disk_to.file = File(id_=disk_from.file.id_, size=disk_to.size)

            # reduce file size and disk size
            disk_from.file.size -= disk_to.size

            # create new empty file after disk_from
            # disk_from_index = self.disks.index(disk_from)
            # new_empty_disk = Disk(size=disk_from.size, file=None)
            # self.disks.insert(disk_from_index + 1, new_empty_disk)

            disk_from.size = disk_from.file.size

        elif disk_to.size > disk_from.file.size:
            # print('move: disk_to.size > disk_from.file.size')
            # fill free space with file
            disk_to.file = disk_from.file

            # there is still space in disk_to, so split it into another empty disk adjecent to disk_to
            disk_to_index = self.disks.index(disk_to)
            # print('new_empty_disk', disk_to.size, disk_to.file.size)
            new_empty_disk = Disk(address=str(uuid.uuid4()), size=disk_to.size - disk_to.file.size, file=None)
            self.disks.insert(disk_to_index + 1, new_empty_disk)

            disk_to.size = disk_to.file.size
            disk_from.file = None


    def part_1(self):
        '''
        00...111...2...333.44.5555.6666.777.888899
        009..111...2...333.44.5555.6666.777.88889.
        0099.111...2...333.44.5555.6666.777.8888..
        00998111...2...333.44.5555.6666.777.888...
        009981118..2...333.44.5555.6666.777.88....
        0099811188.2...333.44.5555.6666.777.8.....
        009981118882...333.44.5555.6666.777.......
        0099811188827..333.44.5555.6666.77........
        00998111888277.333.44.5555.6666.7.........
        009981118882777333.44.5555.6666...........
        009981118882777333644.5555.666............
        00998111888277733364465555.66.............
        0099811188827773336446555566..............
        '''

        # for d in self.disks:
        #     print(d)
        # print()

        # print(self.rep_cur_state)
        while True:
            # find next file
            disk_from = next((disk for disk in reversed(self.disks) if disk.file), None)

            if not disk_from:
                raise Exception('No more files to move')

            # find next free disk space
            disk_to = next((disk for disk in self.disks if not disk.file), None)

            if not disk_to:
                raise Exception('No more free space')

            # print('cur_disks')
            # print('disk_from', disk_from)
            # print('disk_to', disk_to)
            # print()

            # FINISH CONDITION, return the filesystem checksum
            # disk_from_index = self.disks.index(disk_from)
            # disk_to_index = self.disks.index(disk_to)
            disk_from_index = next(i for i, d in enumerate(self.disks) if d.address == disk_from.address)
            disk_to_index = next(i for i, d in enumerate(self.disks) if d.address == disk_to.address)
            if disk_to_index > disk_from_index:
                print('disk_from', disk_from, disk_from_index)
                print('disk_to', disk_to, disk_to_index)
                print(self.rep_cur_state)
                print()

                return self.checksum

            self.move_file(disk_from, disk_to)

            # for d in self.disks:
            #     print(d)
            # print(self.rep_cur_state)

            # print()
            # print()


    @classmethod
    def from_input(cls, input_str: str) -> 'DiskFragmenter':
        line_str = ''
        for line in input_str.split('\n'):
            line = line.strip()
            if line:
                line_str = line
                break

        disks: list[Disk] = []

        cur_id_num = 0
        for i, char in enumerate(line_str):
            disk_size = int(char)

            if i % 2 == 0:
                file = File(id_=cur_id_num, size=disk_size)
                cur_id_num += 1

            else:
                file = None

            disk = Disk(address=str(uuid.uuid4()), size=disk_size, file=file)
            disks.append(disk)

        return cls(input_str=input_str, disks=disks, cur_disks=disks)


def answer(problem_input, level, test=None):

    disk_fragmenter = DiskFragmenter.from_input(problem_input)

    if level == 1:
        return disk_fragmenter.part_1()

    elif level == 2:
        return 0


aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
