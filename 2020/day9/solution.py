

input_numbers = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        input_numbers.append(int(line.rstrip()))

def part_1(numbers):
    preamble = 25
    i = preamble

    def has_two_sum(target, nums):
        for a in nums:
            for b in nums:
                if a + b == target:
                    return True
        return False


    while has_two_sum(numbers[i], numbers[i-preamble:i]):
        i += 1

    return i, numbers[i]

# print(part_1(input_numbers))
# solution: 1309761972

def part_2(numbers):

    target_index, target_value = part_1(numbers)

    add_nums = []
    cumsum = 0
    for val in numbers:
        cumsum += val
        add_nums.append(cumsum)
    
    a = 0
    b = 2
    found = False
    while b < target_index and a < target_index:
        if add_nums[b] - add_nums[a] == target_value:
            found = True
            break
        elif add_nums[b] - add_nums[a] < target_value:
            b += 1
        elif add_nums[b] - add_nums[a] > target_value:
            a += 1

    print(a, b)

    contigous_range = numbers[a+1:b+1]
    print(sum(contigous_range))

    return max(contigous_range) + min(contigous_range)

print(part_2(input_numbers))
# solution: 177989832