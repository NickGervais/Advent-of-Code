### Day 22: Crab Combat ###

player_1 = []
with open('player_1.txt', 'r') as input:
    for i, line in enumerate(input):
        player_1.append(int(line.rstrip()))

player_2 = []
with open('player_2.txt', 'r') as input:
    for i, line in enumerate(input):
        player_2.append(int(line.rstrip()))


def play_round(player_1, player_2):
    if len(player_1) == 0 or len(player_2) == 0:
        return player_1, player_2
    
    p1_card = player_1.pop(0)
    p2_card = player_2.pop(0)

    if p1_card > p2_card:
        player_1.extend([p1_card, p2_card])
    elif p2_card > p1_card:
        player_2.extend([p2_card, p1_card])
        
    return player_1, player_2

def part_1(player_1, player_2):
    while 0 not in [len(player_1), len(player_2)]:
        player_1, player_2 = play_round(player_1, player_2)

    winner = player_1 if len(player_1) > 0 else player_2

    mult = len(winner)
    score = 0
    for i in winner:
        score += mult * i
        mult -= 1

    print(score)

part_1(player_1, player_2)
# solution: 35370
