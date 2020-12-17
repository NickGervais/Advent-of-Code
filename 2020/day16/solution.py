### Day 16: Ticket Translation ###

nearby_tickets = []
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        nearby_tickets.append(line.rstrip())

rules = {}
with open('rules.txt', 'r') as input:
    for i, rule in enumerate(input):
        rule=rule.rstrip()
        name, params = rule.split(': ')
        params = params.split(' or ')
        params = [tuple([int(j) for j in i.split('-')]) for i in params]
        rules[name] = params

def is_valid_on_rules(value, params):
    for x,y in params:
        if x <= value <= y:
            return True
    return False

def part_1(my_ticket, nearby_tickets, rules):
    bad_fields = []
    for ticket in nearby_tickets:
        ticket = [int(i) for i in ticket.split(',')]

        for i in ticket:
            bad_num = True
            for name, params in rules.items():
                res = is_valid_on_rules(i, params)
                # print(i, name, params, res)
                if res:
                    bad_num = False
                    break

            if bad_num:
                bad_fields.append(i)
    
    return sum(bad_fields)

my_ticket = '139,109,61,149,101,89,103,53,107,59,73,151,71,67,97,113,83,163,137,167'
print(part_1(my_ticket, nearby_tickets, rules))
# solution: 20058


def part_2(my_ticket, nearby_tickets, rules):
    good_tickets = []
    for ticket in nearby_tickets:
        ticket = [int(i) for i in ticket.split(',')]

        for i in ticket:
            bad_num = True
            for name, params in rules.items():
                if is_valid_on_rules(i, params):
                    bad_num = False
                    break

            if bad_num:
                break
        if bad_num:
            continue
        else:
            good_tickets.append(ticket)
            
    
    my_ticket = [int(i) for i in my_ticket.split(',')]
    tracker = {name: [0] * len(my_ticket) for name, _ in rules.items()}
    good_tickets.insert(0, my_ticket)

    for ticket in good_tickets:
        for i, value in enumerate(ticket):
            for name, params in rules.items():
                if is_valid_on_rules(value, params):
                    tracker[name][i] += 1
    
    target_number = len(good_tickets)
    pecking_order = [(name, l) for name, l in tracker.items()]
    pecking_order = sorted(pecking_order, key=lambda i: i[1].count(target_number))

    field_order = {}

    for name, l in pecking_order:
        temp = l
        for idx in field_order.keys():
            temp[idx] = None
        final_i = temp.index(target_number)
        field_order[final_i] = name
    
    results = []
    for i, val in enumerate(my_ticket):
        if field_order[i].startswith('departure'):
            results.append(val)
    import numpy
    return numpy.prod(results)


my_ticket = '139,109,61,149,101,89,103,53,107,59,73,151,71,67,97,113,83,163,137,167'
print(part_2(my_ticket, nearby_tickets, rules))
# solution: 366871907221