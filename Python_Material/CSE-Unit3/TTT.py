# the | sign is the pipe -> will see this again
from tkinter import HORIZONTAL


artBoard='''
     |    |    
----------------
     |    |    
----------------
     |    |    
'''

gameBoard=[[" "," "," "],[" "," "," "],[" "," "," "]]

def printBoard(board):
     for row in range(len(board)):
          for col in range(len(board[0])):
               if col!=2:
                    print(board[row][col],end="|")
               else:
                    print(board[row][col])
          if row!=2:
               print("-"*6)
          else:
               print("\n"*2)  #\n is a new line

#check if the spot is taken or not
def chooseSpot(row,column,symbol,board):
     #if the spot is taken
     if board[row][column]==" ":
          #add the symbol and return true
          board[row][column]=symbol
          return True
     return False

def checkForWinner(board):
     #vertical
     for c in range(len(board)):
          if(board[0][c]==board[1][c] and board[1][c]==board[2][c]and board[0][c]!=" "):
               print("winner winner chicken dinner")
               printBoard(board)
               return True
     # HORIZONTAL
     for c in range(len(board)):
          if(board[r][0]==board[r][1] and board[r][1]==board[r][2]and board[r][0]!=" "):
               print("winner winner chicken dinner")
               printBoard(board)
               return True
     # diagonal

symbol="X" 
              
while (symbol!="Q"):
     printBoard(gameBoard)



     #playerGoes(symbol)
     goodSpot=False
     while not goodSpot:
          #we need to see if user inputs correct data -> null,no negs,strings
          r=int(input("row: "))-1
          c=int(input("col: "))-1
          if r in range(3) and c in range(3):
               #choose spot will set the symbol and if spot is taken, returns false 
               if(not chooseSpot(r, c, symbol, gameBoard)):
                    print("spot taken") 
               else:
                    goodSpot=True #breaks the players turn loopz



               #check to see if the spot is taken
     #check for a winner -> if win set symbol to Q
     if checkForWinner(gameBoard):
          symbol="Q"
     #switch symbols for the next player
     if symbol=="X":
          symbol="O"
     elif symbol=="O":
          symbol="X"

