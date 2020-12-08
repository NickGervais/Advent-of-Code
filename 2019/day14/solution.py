## day 14 ##

reactions = {}
with open('input.txt', 'r') as problem_input:
    for _, line in enumerate(problem_input):
        line = line.rstrip()
        i, o = line.split(' => ')
        i_s = i.split(', ')
        l = []
        for j in i_s:
            l.append(j.split(' '))
        o_a, o_n = o.split(' ')
        reactions[o_n] =  [o_a, l]


def get_amnt_and_ore(reactions: dict, element: str) -> (int, int):
    amount = int(reactions[element][0])
    l = reactions[element][1]

    total_ore = 0
    for i in l:
        total_produced = 0
        while total_produced < int(i[0]):
            if i[1] == 'ORE':
                produced = ore = 1
            else:
                produced, ore = get_amnt_and_ore(reactions, i[1])
            total_produced += produced
            total_ore += ore
    return amount, total_ore

def partOne(reactions: dict):
    fuel_amount, total_ore = get_amnt_and_ore(reactions, 'FUEL')
    print(fuel_amount, total_ore)

partOne(reactions)