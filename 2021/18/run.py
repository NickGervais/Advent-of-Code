from __future__ import annotations
import os
from aoc_utils import aoc_utils
from collections import defaultdict
from random import randint
import time
import math

year, day = os.getcwd().split('/')[-2:]

test_cases = [
    # {'level': 1, 'input': '', 'output': ''},
]

'''
[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]] (explode)
[[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]] (explode)
[[[[4,0],[5,4]],[[0,[7,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]] (explode)
[[[[4,0],[5,4]],[[7,0],[15,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]] (explode)
[[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[0,[11,3]],[[6,3],[8,8]]]]] (explode)
[[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[11,0],[[9,3],[8,8]]]]] (explode)
[[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[11,9],[0,[11,8]]]]] (explode)
[[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[11,9],[11,0]]]] (explode)

[[[[4,0],[5,4]],[[7,0],[[7,8],5]]],[10,[[11,9],[11,0]]]] (split)
[[[[4,0],[5,4]],[[7,7],[0,13]]],[10,[[11,9],[11,0]]]] (explode)
[[[[4,0],[5,4]],[[7,7],[0,[6,7]]]],[10,[[11,9],[11,0]]]] (split)
[[[[4,0],[5,4]],[[7,7],[6,0]]],[17,[[11,9],[11,0]]]] (explode)

'''

class Node:
    def __init__(self, val: int = None, x: Node = None, y: Node = None, parent: Node = None):
        self.val = val
        self.x = x
        self.y = y
        self.parent = parent

    def set_left_to_right(self, n: Node) -> None:
        if self.x is None:
            self.x = n
        elif self.y is None:
            self.y = n

    def depth(self) -> int:
        if self.val is not None:
            return 0
        return 1 + max(self.x.depth(), self.y.depth())

    def leftmost(self) -> Node:
        if self.val is not None:
            return self
        return self.x.leftmost()

    def rightmost(self) -> Node:
        if self.val is not None:
            return self
        return self.y.rightmost()

    def leftmost_pair(self, search_depth: int, cur_depth: int = 0) -> Node:
        if self.val is not None:
            return None
        elif self.x.val is not None and self.y.val is not None and search_depth == cur_depth:
            return self
        
        l = self.x.leftmost_pair(search_depth, cur_depth=cur_depth+1)
        if l:
            return l
        r = self.y.leftmost_pair(search_depth, cur_depth=cur_depth+1)
        if r:
            return r
        return None

    def ten_or_more(self) -> Node:
        if self.val is not None:
            # it is a leaf node
            if self.val >= 10:
                return self
            else:
                return None
        l = self.x.ten_or_more()
        if l:
            return l
        r = self.y.ten_or_more()
        if r:
            return r
        return None

    def split(self) -> None:
        assert self.val >= 10
        self.x = Node(math.floor(self.val / 2), parent=self)
        self.y = Node(math.ceil(self.val / 2), parent=self)
        self.val = None
    
    def explode(self):
        assert self.x and self.x.val is not None
        assert self.y and self.y.val is not None

        L = self.x.val
        n = self
        p = self.parent
        while p is not None:
            if n != p.x:
                # n came from right.
                # predecessor is in p.x
                p.x.rightmost().val += L
                break
            n = p
            p = p.parent
        
        R = self.y.val
        n = self
        p = self.parent
        while p is not None:
            if n != p.y:
                # n came from left
                # successor is in p.y
                p.y.leftmost().val += R
                break
            n = p
            p = p.parent

        self.x = None
        self.y = None
        self.val = 0

    def reduce(self) -> None:
        while True:
            did_something = False
            d = self.depth()
            if d > 4:
                # explode
                l = self.leftmost_pair(d, 1)
                l.explode()
                did_something = True
            else:
                t = self.ten_or_more()
                if t:
                    t.split()
                    did_something = True

            if not did_something:
                break   
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.y is None and self.x is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.y is None:
            lines, n, p, x = self.x._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.x is None:
            lines, n, p, x = self.y._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.x._display_aux()
        right, m, q, y = self.y._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def new_node(s: str) -> Node:
    head = None
    stack = []
    for _, c in enumerate(s):
        if c == '[':
            n = Node(None)
            stack.append(n)
        elif c == ']':
            # done with SR.
            done = stack.pop(-1)
            if len(stack) == 0:
                head = done
            else:
                stack[-1].set_left_to_right(done)
                done.parent = stack[-1]

        elif c == ',':
            # next is right side.
            pass
        else:
            # otherwise it should be an int
            try:
                val = int(c)
                n = Node(val, parent=stack[-1])
                stack[-1].set_left_to_right(n)
            except ValueError:
                pass
    return head

def add_nodes(x: Node, y: Node) -> Node:
    z = Node(None, x=x, y=y, parent=None)
    x.parent = z
    y.parent = z
    z.reduce()
    return z

def calc_magnitude(n: Node) -> int:
    l = -1
    if n.x.val is not None:
        l = n.x.val
    else:
        l = calc_magnitude(n.x)
    
    r = -1
    if n.y.val is not None:
        r = n.y.val
    else:
        r = calc_magnitude(n.y)

    return 3*l + 2*r

# def assert_all_have_parent(n, depth=0):
#     if n.val is not None:
#         return
#     if depth != 0:
#         assert n.parent
#     n.display()
#     assert_all_have_parent(n.x, depth+1)
#     assert_all_have_parent(n.y, depth+1)

def answer(problem_input, level, test=None):
    sn_strings = []
    for line in problem_input.split('\n'):
        sn_strings.append(line.strip())

    # Explosion Examples:
    # examples = [
    #    '[[[[[9,8],1],2],3],4]',
    #    '[7,[6,[5,[4,[3,2]]]]]',
    #    '[[6,[5,[4,[3,2]]]],1]',
    #    '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]',
    #    '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]',
    # ]
    # for s in examples:
    #     n = new_node(s)
    #     n.display()
    #     n.reduce()
    #     n.display()
    #     print()

    if level == 1:
        sn = new_node(sn_strings[0])
        sn.display()
        for s in sn_strings[1:]:
            nn = new_node(s)
            sn = add_nodes(sn, nn)
            sn.display()
        
        return calc_magnitude(sn)
    elif level == 2:
        max_mag = float('-inf')
        for a in sn_strings:
            for b in sn_strings:
                if a == b:
                    continue
                else:
                    an = new_node(a)
                    bn = new_node(b)
                    c = add_nodes(an, bn)
                    mag = calc_magnitude(c)
                    if mag > max_mag:
                        max_mag = mag
        print(max_mag)
        return max_mag

aoc_utils.run(answer, test_cases=test_cases, year=year, day=day)
