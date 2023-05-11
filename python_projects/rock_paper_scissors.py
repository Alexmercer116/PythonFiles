import random

def gamePlay(ch):
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    
    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    
    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    
    moves = [rock, paper, scissors]
    game_draw = "Game drawn"
    if(ch.lower() == 'rock'):
        player_move = rock
        pc_move = random.choice(moves)
        print(f"Player Chose:\n{player_move}")
        print(f"PC Chose:\n{pc_move}")  
        if(pc_move == rock):
            return game_draw
        elif(pc_move == paper):
            return "Player lost the game"
        else:
            return "Player won the game"
    elif(ch.lower() == 'paper'):
        player_move = paper
        pc_move = random.choice(moves)
        print(f"Player Chose:\n{player_move}")
        print(f"PC Chose:\n{pc_move}")  
        if(pc_move == rock):
            return "Player won the game"
        elif(pc_move == paper):
            return game_draw
        else:
            return "Player lost the game"
    else:
        player_move = scissors
        pc_move = random.choice(moves)
        print(f"Player Chose:\n{player_move}")  
        print(f"PC Chose:\n{pc_move}")  
        if(pc_move == rock):
            return "Player lost the game"
        elif(pc_move == paper):
            return "Player won the game"
        else:
            return game_draw
          
def gameWin(ch):
    game_win = gamePlay(ch)
    if(game_win == "Player won the game"):
        print("Player won the game")
    elif(game_win == "Player lost the game"):
        print("Player lost the game")
    else:
        print("Game drawn")

print('''**********

___Welcome to Jan-Ken-Po___

**********''')
strt=input("Play the game[Y/N]?\t")
if(strt in 'yY'):
    play_again=True
    while(play_again):
      ch = input('''Choose Your move:
      rock
      paper
      scissors
      \n''')
      gameWin(ch)
      rply=input("Want to play again[Y/N]?\t")
      if(rply in 'yY'):play_again=True
      else:play_again=False
else:
    quit()
