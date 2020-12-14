### Day 13: Shuttle Search ###

lines = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        lines.append(line.rstrip())

timestamp = int(lines[0])
bus_ids = [None if i == 'x' else int(i) for i in lines[1].split(',')]

print(timestamp)
print(bus_ids)

import math

def part_1(timestamp, bus_ids):
    earliest_bus_id = float('inf')
    earliest_time = float('inf')
    for bus_id in bus_ids:
        if not bus_id:
            continue
        e = math.ceil(timestamp/float(bus_id))
        e = e * bus_id
        if e < earliest_time:
            earliest_bus_id = bus_id
            earliest_time = e
    
    time_diff = earliest_time - timestamp
    print(time_diff * earliest_bus_id)

# part_1(timestamp, bus_ids)
# solution: 138

import numpy

def part_2(bus_ids):
    new_ids = []
    for i, id in enumerate(bus_ids):
        if id:
            new_ids.append((i, id))

    bus_ids = new_ids
    print(bus_ids)

    synced_ids = [bus_ids[0]]
    def t_delta(synced_ids):
        return numpy.prod([i[1] for i in synced_ids])
    
    t = t_delta(synced_ids)
    found = False
    while not found:
        all_match = True
        for i, bus_id in bus_ids:
            if (i, bus_id) in synced_ids:
                continue
            expected = (t + i) % bus_id
            if expected == 0:
                synced_ids.append((i, bus_id))
            else:
                all_match = False
                break
        if all_match:
            found = True
        else:
            t += t_delta(synced_ids)

    print(t)

part_2(bus_ids)
# solution: 226845233210288
