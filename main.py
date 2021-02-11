

def print_header():
  print('''

  ____   ___   ____                                            
  |    \ /  _] /    |                                           
  |  o  )  [_ |   __|                                           
  |   _/    _]|  |  |                                           
  |  | |   [_ |  |_ |                                           
  |  | |     ||     |                                           
  |__| |_____||___,_|                                           
                                                                
    _____  ___   _      ____  ______   ____  ____  ____     ___ 
  / ___/ /   \ | |    |    ||      | /    ||    ||    \   /  _]
  (   \_ |     || |     |  | |      ||  o  | |  | |  D  ) /  [_ 
  \__  ||  O  || |___  |  | |_|  |_||     | |  | |    / |    _]
  /  \ ||     ||     | |  |   |  |  |  _  | |  | |    \ |   [_ 
  \    ||     ||     | |  |   |  |  |  |  | |  | |  .  \|     |
    \___| \___/ |_____||____|  |__|  |__|__||____||__|\_||_____|
                                                                
  '''
  )
  print("How to play: \n \nAt the beginning, all the holes are filled except for the middle one. \nThe goal is to only have one remaining peg in the center hole. \nTo remove a peg, you can jump over it.")

# https://www.patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

# Global Variables
HEIGHT = 6
WIDTH = 6
CORNER = 2

# board = []

def create_board(board):
  for i in range(HEIGHT):
    for j in range(WIDTH):
      if (j in range(0, CORNER) or j in range(WIDTH-CORNER, WIDTH)) and (i in range(0, CORNER) or i in range(HEIGHT-CORNER, HEIGHT)):
        board[i, j] = " "
      elif i == HEIGHT/2 and j == WIDTH/2:
        board[i, j] = "O"
      else:
        board[i, j] = "X"
      return board

def print_board(board):
  for i in range(HEIGHT):
    for j in range(WIDTH):
      print(board[i][j])
    print("\n")
  print("\n")
  return

def check_if_board_is_solved(board):
  count = 0
  for i in range(HEIGHT):
    for j in range(WIDTH):
      if board[i][j] == "X":
        count+=1
  if count ==1:
    return True
  else:
    return False

print_header()
create_board([])
