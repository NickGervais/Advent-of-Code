### Day 1: Report Repair ###

def part_1(target_sum):
    seen_expenses = set()
    with open('input.txt', 'r') as input:
        for i, expense in enumerate(input):
            expense = int(expense)
            matching_expense = target_sum - expense
            if matching_expense in seen_expenses:
                return matching_expense * expense
            else:
                seen_expenses.add(expense)

# print(part_1(2020))
# solution: 444019

def part_2(target_sum):
    expenses = []
    with open('input.txt', 'r') as input:
        for i, expense in enumerate(input):
            expenses.append(int(expense))

    expense_set = set(expenses)
    total_expenses = len(expenses)
    for a_idx, a_expense in enumerate(expenses):
        for b_idx, b_expense in enumerate(expenses[a_idx:]):
            for c_expense in expenses[b_idx:]:
                if a_expense + b_expense + c_expense == target_sum:
                    return a_expense * b_expense * c_expense

# print(part_2(2020))
# solution: 29212176


expenses = []
with open('input.txt', 'r') as file:
    for line in file:
        expenses.append(int(line))

print(expenses)

