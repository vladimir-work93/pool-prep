import json

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
        }
    }

def is_finished(state):
    return state['finished']

if __name__ == '__main__':
    state_1 = new_game()
    state_2 = new_game()
    state_1['positions'][7] = 5
    print("Игра 1", state_1['positions'][7])
    print("Игра 2", state_2['positions'][7])
    print(json.dumps(state_1))
    print(is_finished(state_1))