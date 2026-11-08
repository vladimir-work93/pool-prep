import json
import random

HORSES = list(range(2, 13))
TRACK_LENGTH = 21
START_POSITION = 1
FINISH_POSITION = 21

def new_game():
    return {
        'finished': False,
        'winner': None,
        'last_roll': None,
        'positions': {
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
        },
    }

def is_finished(state):
    return state['finished']

def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return (d1, d2)

def apply_roll(state, dice=None):
    if state['finished']:
        return None
    if dice is None:
        d1, d2 = roll_dice()
    else:
        d1, d2 = dice
    total = d1 + d2
    state['positions'][total] += 1
    position = state['positions'][total]
    if position >= FINISH_POSITION:
        state['finished'] = True
        state['winner'] = total
    state['last_roll'] = {
        'dice': [d1, d2],
        'total': total
    }

    return {
        'dice': [d1, d2],
        'total': total,
        'position': position,
        'winner': state['winner'],
    }

def print_state(state):
    text = 'Позиции: '
    for horse, pos in state['positions'].items():
        text += str(horse) + ':' + str(pos) + ' '
    print(text)

def play_game(initial_state=None):
    state = initial_state if initial_state is not None else new_game()
    turn = 0
    while not is_finished(state):
        print_state(state)
        cmd = input("Enter — бросить, 'q' — выйти: ").strip().lower()
        if cmd == 'q':
            print("Игра прервана")
            return state['winner']
        else:
            report = apply_roll(state)
        turn += 1
        print(f"Ход {turn}: выпало {report['dice'][0]} и "
              f"{report['dice'][1]}, сумма {report['total']} → лошадь"
              f" {report['total']} идёт на позицию {report['position']}")
    print(f"🏆 Победила лошадь №{state['winner']}. Количество ходов: {turn}")


if __name__ == '__main__':
    state = new_game()
    state['positions'][7] = 20
    play_game(state)