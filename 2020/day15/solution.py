### Day 15: Rambunctious Recitation ###

numbers = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        line = line.rstrip()
        numbers = [int(j) for j in line.split(',')]

def part_1(numbers):
    def last_index(l, val):
        try:
            return len(l) - 1 - l[::-1].index(val)
        except ValueError:
            return None
    
    spoken_numbers = numbers
    last_spoken = spoken_numbers[-1]

    for i in range(len(spoken_numbers), 30000000):
        # print(spoken_numbers)
        index = last_index(spoken_numbers[:-1], last_spoken)
        if index is None:
            # print(last_spoken, index)
            last_spoken = 0
        else:
            # print(last_spoken, len(spoken_numbers), index + 1)
            last_spoken = len(spoken_numbers) - (index + 1)
        spoken_numbers.append(last_spoken)
    
    return last_spoken

# print(part_1(numbers))
# solution: 441

def part_2(numbers):
    spoken_numbers = numbers[:-1]
    last_spoken = numbers[-1]
    last_seen_numbers = {}

    def last_index(value):
        try:
            return last_seen_numbers[value]
        except KeyError:
            return None

    for i, n in enumerate(spoken_numbers):
        last_seen_numbers[n] = i
    
    for i in range(len(spoken_numbers), 30000000 -1):
        index = last_index(last_spoken)
        # print(f'last_spoken: {last_spoken}', f'index: {index}', spoken_numbers, last_seen_numbers)
        if index is None:
            next_spoken = 0
        else:
            next_spoken = len(spoken_numbers) - (index)
        
        spoken_numbers.append(last_spoken)
        last_seen_numbers[last_spoken] = len(spoken_numbers) - 1
        last_spoken = next_spoken

    return last_spoken
    
import time
start_seconds = time.time()
print(part_2(numbers))
print("Seconds: ", time.time() - start_seconds)
# solution: 10613991



