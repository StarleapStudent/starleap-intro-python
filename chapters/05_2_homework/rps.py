
def is_valid_answer(answer):
    if (answer == 'Rock'):
        return True
    elif (answer == 'Paper'):
        return True
    elif (answer == 'Scissors'):
        return True
    else:
        return False

def get_player_input(num):
    answer = input(f"Player {num}? ").capitalize()
    if (not is_valid_answer(answer)):
        print("This is not a valid object selection")
        return get_player_input(num)
    else:
        return answer

def get_winner(a1, a2):
    if (a1 == a2):
        return 0
    elif (a1 == 'Rock'):
        if (a2 == 'Paper'):
            return 2
        else:
            return 1
    elif (a1 == 'Paper'):
        if (a2 == 'Rock'):
            return 1
        else:
            return 2
    elif (a1 == 'Scissors'):
        if (a2 == 'Rock'):
            return 2
        else:
            return 1
    return 0

def play_rps():
    a1 = get_player_input(1)
    a2 = get_player_input(2)
    # print(f'{a1} vs {a2} :')
    winner = get_winner(a1, a2)
    if (winner == 0):
        print("No winner.")
    else:
        print(f"Player {winner} wins.")

play_rps()