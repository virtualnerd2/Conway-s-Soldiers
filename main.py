import pygame
import time

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
greyBackground=(203, 206, 203)

width = 65
height = 65
radius = 30
margin = 2
xDistanceFromEdge = 0
gameBoard=[[None]*10 for _ in range(10)] 
windowSize=[670, 670]

pygame.init()
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Draughts Game")
done = False
clock = pygame.time.Clock()

level = 1
newGame=True

def square_colour(row, col):
    return white if (row + col) % 2 == 0 else black  

def boardGui():
    for boardRow in range(10):
        for boardColumn in range(10):
            xCoordinate=((margin+width) * boardColumn + margin)+xDistanceFromEdge
            yCoordinate=(margin+height) * boardRow + margin
            currentColour = square_colour(boardRow, boardColumn)
            pygame.draw.rect(screen,currentColour,[xCoordinate,yCoordinate, width, height])

def piecesGameBoard(gameBoard):
    if newGame:
        newGameBoard(gameBoard)
    else:
      drawPieces(gameBoard)

def newGameBoard(gameBoard):
    gameBoard[:] = [[None]*10 for _ in range(10)]  # Empty the game board.

    for x in range(10):
        for y in range(10):
              if y in range(5,10):
                gameBoard[x][y]="Red"
              else:
                gameBoard[x][y]="Empty"

    drawPieces(gameBoard)

def drawPieces(gameBoard):
    for x in range(10):
        for y in range(10):
            xCoordinate=((margin+width) * x + margin+32)+xDistanceFromEdge
            yCoordinate=(margin+height) * y + margin+33
            if gameBoard[x][y]=="Red":
                pygame.draw.circle(screen,red,(xCoordinate,yCoordinate),radius)
            elif gameBoard[x][y]=="Blue":
                pygame.draw.circle(screen,blue,(xCoordinate,yCoordinate),radius)

def drawLine(gameBoard):
  x = 6 - level
  xCoordinate= (0,   ((margin+width) * x + margin)+xDistanceFromEdge)
  yCoordinate= (670, ((margin+width) * x + margin)+xDistanceFromEdge)
  pygame.draw.line(screen, yellow, xCoordinate, yCoordinate, 4)

def checkMove(column, row):
  if(gameBoard[column][row] != "Empty"):
    return "NOT VALID"
  
  if(row - 2 >= 0 and gameBoard[column][row-2] == "Blue"):
    return "UP"
  elif(row + 2 < len(gameBoard[column]) and gameBoard[column][row+2] == "Blue"):
    return "DOWN"
  elif(column+2 < len(gameBoard) and gameBoard[column+2][row] == "Blue"):
    return "LEFT"
  elif(column-2 >= 0 and gameBoard[column-2][row] == "Blue"):
    return "RIGHT"
  else:
    return "NOT VALID"

def renderImage():
  screen.fill(greyBackground)
  boardGui()
  drawLine(gameBoard)
  piecesGameBoard(gameBoard)
  clock.tick(60)
  pygame.display.flip()


selected = False
def printLevel():
  if level == 1:
    print("LEVEL 1: EASY ENOUGH")
  if level == 2:
    print("LEVEL 2: KINDA TRICKY")
  if level == 3:
    print("LEVEL 3: HEY THIS IS AN ACTUAL CHALLENGE")
  if level == 4:
    print("LEVEL 4: THIS IS GETTING OUT OF HAND")
  if level == 5:
    print("LEVEL 5: WINNING IS OVERATED")

printLevel()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            # Change the x/y screen coordinates to grid coordinates
            column = (pos[0]-xDistanceFromEdge) // (width+margin)
            row = pos[1] // (height+margin)
            print((column, row))

            validMove = checkMove(column, row)
            if(gameBoard[column][row] == "Blue"):
              gameBoard[column][row] = "Red"
              selected = False

            elif (selected and validMove != "NOT VALID"):
              gameBoard[column][row] = "Red"
              if(validMove == "UP"):
                gameBoard[column][row-2] = "Empty"
                gameBoard[column][row-1] = "Empty"
              elif(validMove == "DOWN"):
                gameBoard[column][row+2] = "Empty"
                gameBoard[column][row+1] = "Empty"
              elif(validMove == "LEFT"):
                gameBoard[column+2][row] = "Empty"
                gameBoard[column+1][row] = "Empty"
              elif(validMove == "RIGHT"):
                gameBoard[column-2][row] = "Empty"
                gameBoard[column-1][row] = "Empty"
              selected = False

              if(row == 5 - level):
                print("You did it")
                print("Level Complete")

                level = level + 1
                printLevel()
                
                renderImage()
                time.sleep(2)
                newGame = True
            

            elif(selected and validMove == "NOT VALID"):
                print("Not Valid")
            elif(not selected and gameBoard[column][row] == "Red" and column < len(gameBoard) and row < len(gameBoard[0])):
              gameBoard[column][row] = "Blue"
              selected = True
        elif pygame.key.get_pressed()[pygame.K_r] == True:
          newGame = True
          print("Reset")
            
    renderImage()
    newGame = False

pygame.quit()