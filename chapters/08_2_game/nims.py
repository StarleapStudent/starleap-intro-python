import math



def play_nims(pile=100, max_stones=5):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    player = 0
    name1 = ''
    name2 = ''
    name = ''

    def print_status():
        print(f'There are {pile} stones in the pile.')

    def prompt_player():
        max = min(pile, max_stones)
        while True:
            answer_str = input(f'{name}, how many do you take? ')
            if (answer_str.isnumeric()):
                answer = int(answer_str)
                if answer > max:
                    print(f"You can't take more than {max}.")
                elif answer < 1:
                    print(f"You can't take fewer than 1.")
                else:
                    return answer
            else:
                print("That is not a valid answer.")

    def switch_player():
        nonlocal player, name
        if player == 1:
            player = 2
            name = name2
        else:
            player = 1
            name = name1

    def instructions():
        print('''
Nims:
In this game, two players sit in front of a pile of 100 stones.
They take turns, each removing between 1 and 5 stones (assuming there are at least 5 stones left in the pile).
The person who removes the last stone(s) wins.

            ''')

    ## Basic structure of program (feel free to alter as you please):

    print("Welcome to Nims!")
    answer = input("Do you need instructions? (Y/N) ")
    if answer == 'Y':
        instructions()

    name1 = input("Player 1, what is your name? ").strip() or "Player 1"
    name2 = input("Player 2, what is your name? ").strip() or "Player 2"

    while pile > 0:
        print_status()
        switch_player()
        answer = prompt_player()
        pile = pile - answer


    print(f"Game over.  {name} is the winner!")

play_nims(100, 5)