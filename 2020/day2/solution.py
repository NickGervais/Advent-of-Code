### Day 2: Password Philosphy ###

def part_1():
    total_valid = 0
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            policy, password = line.split(': ')
            policy_count, policy_letter = policy.split(' ')
            min_count, max_count = policy_count.split('-')
            if int(min_count) <= password.count(policy_letter) <= int(max_count):
                total_valid += 1
    return total_valid

print(part_1())
# solution: 517

def part_2():
    total_valid = 0
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            policy, password = line.split(': ')
            policy_count, policy_letter = policy.split(' ')
            pos_a, pos_b = policy_count.split('-')

            pos_a_valid = password[int(pos_a) - 1] == policy_letter
            pos_b_valid = password[int(pos_b) -1] == policy_letter

            if pos_a_valid != pos_b_valid:
                total_valid += 1
    return total_valid

print(part_2())
# solution: 284