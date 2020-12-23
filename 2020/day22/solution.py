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

def calc_score(hand):
    mult = len(hand)
    score = 0
    for i in hand:
        score += mult * i
        mult -= 1

    return score

def part_1(player_1, player_2):
    while 0 not in [len(player_1), len(player_2)]:
        player_1, player_2 = play_round(player_1, player_2)

    winner = player_1 if len(player_1) > 0 else player_2

    print(calc_score(winner))

# part_1(player_1, player_2)
# solution: 35370

def part_2(player_1, player_2):
    def recursive_combat(p_1, p_2, game_num = 1):
        round_num = 1
        previous_plays = set()
        while 0 not in [len(p_1), len(p_2)]:   
            # print(f"-- Round {round_num} (Game {game_num}) --")  
            # print(f"Player 1's deck: {', '.join([str(i) for i in p_1])}")
            # print(f"Player 2's deck: {', '.join([str(i) for i in p_2])}")       
            if f'{p_1[0]},{p_2[0]}' in previous_plays:
                return 'p1', p_1, p_2  # game winner, p_1 hand, p_2 hand
            
            card_1, card_2 = p_1.pop(0), p_2.pop(0)
            previous_plays.add(f'{card_1},{card_2}')
            # print(f"Player 1 plays: {card_1}")
            # print(f"Player 2 plays: {card_2}")

            round_winner = None
            if card_1 <= len(p_1) and card_2 <= len(p_2):
                round_winner, sub_p_1, sub_p_2 = recursive_combat(p_1[:card_1], p_2[:card_2], game_num+1)
            elif card_1 > card_2:
                round_winner = 'p1'
            elif card_2 > card_1:
                round_winner = 'p2'

            if round_winner == 'p1':
                p_1.extend([card_1, card_2])
            else:
                p_2.extend([card_2, card_1])

            # print(f"Round Winner: {round_winner}", f"p1: {', '.join([str(i) for i in p_1])}", f"p2: {', '.join([str(i) for i in p_2])}")
            round_num += 1

        game_winner = 'p1' if len(p_1) > 0 else 'p2'
        # print(f"Game Winner: {game_winner}")
        return game_winner, p_1, p_2

    winner, p_1, p_2 = recursive_combat(player_1, player_2)
    winner_hand = p_1 if winner == 'p1' else p_2
    print(winner_hand)
    print(calc_score(winner_hand))
        
part_2(player_1, player_2)
