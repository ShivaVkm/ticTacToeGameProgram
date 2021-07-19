
board = ["-", "-", "-","-", "-", "-","-", "-", "-"]

gameStillGoing = True

winner = None

currentPlayer = "X"

def play_game():

  displayBoard()
  while gameStillGoing:
    handleTurn(current_player)
    checkIfGameOver()
    flipPlayer()
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

def displayBoard():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

def handleTurn(player):
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")
  board[position] = player
  displayBoard()

def checkIfGameOver():
  checkForWinner()
  checkForTie()

def checkForWinner():
  global winner
  rowWinner = checkRows()
  columnWinner = checkColumns()
  diagonalWinner = checkDiagonals()
  if rowWinner:
    winner = rowWinner
  elif columnWinner:
    winner = columnWinner
  elif diagonalWinner:
    winner = diagonalWinner
  else:
    winner = None

def checkRows():
  global gameStillGoing
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row1 or row2 or row3:
    gameStillGoing = False
  if row1:
    return board[0] 
  elif row2:
    return board[3] 
  elif row3:
    return board[6] 
  else:
    return None

def checkColumns():
  global gameStillGoing
  column1 = board[0] == board[3] == board[6] != "-"
  column2 = board[1] == board[4] == board[7] != "-"
  column3 = board[2] == board[5] == board[8] != "-"
  if column1 or column2 or column3:
    gameStillGoing = False
  if column1:
    return board[0] 
  elif column2:
    return board[1] 
  elif column3:
    return board[2] 
  else:
    return None

def checkDiagonals():
  global gameStillGoing
  diagonal1 = board[0] == board[4] == board[8] != "-"
  diagonal2 = board[2] == board[4] == board[6] != "-"
  if diagonal1 or diagonal2:
    gameStillGoing = False
  if diagonal1:
    return board[0] 
  elif diagonal2:
    return board[2]
  else:
    return None


def checkForTie():
  global gameStillGoing
  if "-" not in board:
    gameStillGoing = False
    return True
  else:
    return False


def flipPlayer():
  global currentPlayer
  if currentPlayer == "X":
    currentPlayer = "O"
  elif currentPlayer == "O":
    currentPlayer = "X"

playGame()
