
def partOne():
    valid_count = 0

    for i in range(240920, 789857 + 1):
        num = str(i)

        p1 = 0
        p2 = 1
        valid = False
        while p2 < len(num):
            if int(num[p1]) > int(num[p2]):
                valid = False
                break
            if num[p1] == num[p2] and not valid:
                valid = True
            p1 += 1
            p2 += 1

        if valid:
            valid_count += 1

    return valid_count

print(partOne())

## part 2 ##
def partTwo():
    valid_count = 0

    for i in range(240920, 789857 + 1):
        num = str(i)
    
        p1 = 0
        p2 = 1
        increasing = True
        has_dup = False
        while p2 < len(num):
            if int(num[p1]) > int(num[p2]):
                increasing = False
                break
            if num[p1] == num[p2]:
                while p2 < len(num) and num[p1] == num[p2]:
                    p2 += 1
                if p2 - p1 == 2:
                    has_dup = True
                p1 = p2 - 1
            else:
                p1 += 1
                p2 += 1

        if increasing and has_dup:
            valid_count += 1

    return valid_count

print(partTwo())