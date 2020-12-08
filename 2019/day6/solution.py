### Day 6: Universal Orbit Map ###
## Part 1 ##

# class Planet:
#     def __init__(self, name: str, children: list = []):
#         self.name = name
#         self.children = children
    
#     def add_child(child: Planet):
#         self.children.append(child)

# COM = Planet('COM', [])

space = {
    'COM': []
}

with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        parent, child = line.split(')')
        child = child.rstrip()
        if parent in space:
            space[parent].append(str(child))
        else:
            space[parent] = [str(child)]

def calc_orbits(planet: str, depth: int) -> int:
    if planet not in space:   # planet has no children
        return depth
    else:
        children = space[planet]
        orbits = 0
        for child in children:
            orbits += calc_orbits(child, depth + 1)
        return depth + orbits

total_orbits = calc_orbits('COM', 0)

print(f'Part 1: {total_orbits}')

## Part 2 ##

def find_least_common_ancestor(planet: str):
    if planet == 'YOU':
        return 'YOU'
    if planet == 'SAN':
        return 'SAN'
    if planet not in space:
        return None
    
    children = space[planet]
    results = []
    for child in children:
        results.append(find_least_common_ancestor(child))

    for i in results:
        if i not in ['SAN', 'YOU', None]:
            return i
    if 'SAN' in results and 'YOU' in results:
        return planet
    if 'SAN' in results:
        return 'SAN'
    if 'YOU' in results:
        return 'YOU'
    return None

lca = find_least_common_ancestor('COM')

def calc_transfer_orbital(planet: str, depth: int):
    if planet in ['YOU', 'SAN']:
        return depth - 1
    if planet not in space:
        return 0
    
    children = space[planet]
    result = 0
    for child in children:
        result += calc_transfer_orbital(child, depth + 1)

    return result

transfer_orbital_num = calc_transfer_orbital(lca, 0)
print(f'Part 2: {transfer_orbital_num}')