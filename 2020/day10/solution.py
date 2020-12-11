### Day 10: Adapter Array ###

adapters = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        adapter = line.rstrip()
        adapters.append(int(adapter))

def part_1(adapters):
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    print(adapters)
    jolt_diffs = {3: 0, 2: 0, 1: 0}

    for index in range(1, len(adapters)):
        jolt_diffs[(adapters[index] - adapters[index - 1])] += 1

    print(jolt_diffs)
    return jolt_diffs[3] * jolt_diffs[1]

# print(part_1(adapters))
# solution: 1755

def part_2(adapters):
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    adapter_children = {adapter: [] for adapter in adapters}
    a = 0
    b = 1
    while a < len(adapters):
        children = 0
        while b < len(adapters) and adapters[b] <= adapters[a] + 3:
            adapter_children[adapters[a]].append(adapters[b])
            b += 1
        a += 1
        b = a + 1
         
    adapter_children[adapters[-1]] = 1
    for adapter in reversed(adapters[:-1]):
        adapter_children[adapter] = sum([adapter_children[a] for a in adapter_children[adapter]])
    
    return adapter_children[adapters[0]]

print(part_2(adapters))
# solution: 4049565169664
