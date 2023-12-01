import os
from aoc_utils import aoc_utils
from collections import defaultdict
from typing import List, NamedTuple
import copy
import pprint

pp = pprint.PrettyPrinter(indent=4)

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

class Node(NamedTuple):
    name: str
    type: str
    size: int = 0
    parent: str = None
    children: List[str] = []

    @property
    def id(self):
        return str(id(self))

class FileStructure:
    def __init__(self, root):
        self.root = root
        self.structure = {
            root.id: root
        }

    def add_node(self, node: Node):
        self.structure[node.id] = node
        if node.parent and self.structure.get(node.parent):
            self.structure[node.parent].children.append(node.id)

    def get_node_by_id(self, id: str):
        return self.structure[id]

    def get_child_by_name(self, parent_id: str, name: str):
        cur_node = self.structure[parent_id]
        for n_id in cur_node.children:
            n = self.structure.get(n_id)
            if n and n.name == name:
                return n

    def display(self):
        def rec(node_id, indent_num=0):
            node = self.structure[node_id]
            print(f"{' '*indent_num}- {node.name} ({node.type}, size={node.size})")
            for i in node.children:
                rec(i, indent_num+2)
        rec(self.root.id)
    
    def get_node_size(self, node_id: str) -> int:
        node = self.structure[node_id]
        size = node.size
        for i in node.children:
            size += self.get_node_size(i)
        
        return size


# def answer(problem_input, level, test=None):
def answer(level):
    # lines = []
    # for line in problem_input.split('\n'):
    #     lines.append(line.strip())
    lines = []
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            lines.append(line.strip())

    root = Node(name='/', type='dir')
    lines.pop(0)

    fs = FileStructure(root=root)

    cur_id = root.id
    for line in lines:
        cur_node = fs.get_node_by_id(cur_id)
        print(line)
        statement = line.split(' ')
        match statement:
            case ['$', 'cd', '..']:
                # move out one level
                cur_id = cur_node.parent
            case ['$', 'cd', '/']:
                # move to root
                cur_id = root.id
            case ['$', 'cd', dir]:
                # move in one level to dir
                search_child = fs.get_child_by_name(cur_id, dir)
                if search_child:
                    cur_id = search_child.id
                else:
                    raise Exception(f"{dir} NOT FOUND IN {cur_id}")
            case ['$', 'ls']:
                # displaying dir items
                pass
            case ['dir', dir]:
                # displaying dir (create it)
                new_dir = Node(dir, 'dir', parent=cur_id, children=[])
                fs.add_node(new_dir)
            case [size, file]:
                # displaying file and size
                new_file = Node(file, 'file', int(size), parent=cur_id, children=[])
                fs.add_node(new_file)

    fs.display()

    directory_total_sizes = []
    for i, n in fs.structure.items():
        if n.type != 'dir':
            continue
        size = fs.get_node_size(i)
        directory_total_sizes.append((i, size))
    
    if level == 1:
        total_size = 0
        for i, size in directory_total_sizes:
            if size <= 100_000:
                total_size += size
        return total_size
    elif level == 2:
        total_disk_space = 70_000_000
        space_needed = 30_000_000
        used_space = fs.get_node_size(root.id)
        unused_space = total_disk_space - used_space
        space_to_delete = space_needed - unused_space

        s_list = sorted(directory_total_sizes, key=lambda i: i[1])
        for i, s in s_list:
            if s >= space_to_delete:
                return s


            
print(answer(2))
# aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
