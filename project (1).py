import random

def grid(moves):

  print("     |       |      ")
  print(f"  {moves[0]}  |   {moves[1]}   |   {moves[2]}  ")
  print("_____|_______|______")
  print("     |       |      ")
  print(f"  {moves[3]}  |   {moves[4]}   |   {moves[5]}  ")
  print("_____|_______|______")
  print("     |       |      ")
  print(f"  {moves[6]}  |   {moves[7]}   |   {moves[8]}  ")
  print("     |       |      ")



#asking player to choose a sign from # and X

player = input("Do u want to be X or #: ")

while player != "X" and player != "#":
  print("Invalid input")
  player = input("Do u want to be X or #: ")

print(f"You sign is {player}")

if player == "X":
  computer = "#"
else:
  computer = "X"

moves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
]


def check_winner():
    for a, b, c in winning_combinations:
        if moves[a] == moves[b] == moves[c] and moves[a] != " ":
            return moves[a]

def board_full():
    return all(i != " " for i in moves)
win = 1
player_turn = random.choice([True,False])

while win:

  if player_turn:
    grid(moves)
    while True:
      try:
        mo = int(input("Please enter an number (1-9): "))
        if mo < 1 or mo > 9:
            print("Please enter a number between 1-9")
            continue
        if moves[mo-1] == " ":
            moves[mo-1] = player
            # grid(moves)
            winner = check_winner()
            if winner == player:
              grid(moves)
              print("Player won")
              win = 0
              break
            if board_full():
                grid(moves)
                print("It's a draw")
                win = 0
                break
            break
        else:
            print("spot taken")
      except ValueError:
        print("invalid input")

  else:
    while True:
      mo = random.randint(0,8)
      if moves[mo] == " ":
          moves[mo] = computer
          winner = check_winner()
          if winner == computer:
            grid(moves)
            print("Computer won")
            win = 0
            break
          if board_full():
              grid(moves)
              print("It's a draw")
              win = 0
          break
  player_turn = not player_turn

