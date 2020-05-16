import pygame

newGame=True
loggedIn=False
miniGame=False

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
greyBackground=(203, 206, 203)

# This sets the WIDTH and HEIGHT of each grid location
width = 65
height = 65
radius = 30

margin = 2
xDistanceFromEdge = 0

gameBoard=[[None]*10 for _ in range(10)] 
windowSize=[1000, 1000]

pygame.init()
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Draughts Game")
done = False
clock = pygame.time.Clock()

# Added helper function.
def square_colour(row, col):
    """ Determine colour of game board square from its position. """
    return white if (row + col) % 2 == 0 else black  # Makes upper-left corner white.

def boardGui(black,white):
    for boardRow in range(10):
        for boardColumn in range(10):
            xCoordinate=((margin+width) * boardColumn + margin)+xDistanceFromEdge
            yCoordinate=(margin+height) * boardRow + margin
            currentColour = square_colour(boardRow, boardColumn)
            pygame.draw.rect(screen,currentColour,[xCoordinate,yCoordinate, width, height])

def piecesGameBoard(gameBoard):
    if newGame:
        newGameBoard(gameBoard)

def newGameBoard(gameBoard):
    gameBoard[:] = [[None]*10 for _ in range(10)]  # Empty the game board.

    for x in range(10):
        for y in range(10):
              if y in range(5,10):
                  gameBoard[x][y]="Red"

    drawPieces(gameBoard,black,red)

def drawPieces(gameBoard,black,red):
    for x in range(10):
        for y in range(10):
            xCoordinate=((margin+width) * x + margin+32)+xDistanceFromEdge
            yCoordinate=(margin+height) * y + margin+33
            if gameBoard[x][y]=="Red":
                pygame.draw.circle(screen,red,(xCoordinate,yCoordinate),radius)
            if gameBoard[x][y]=="Black":
                pygame.draw.circle(screen,black,(xCoordinate,yCoordinate),radius)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            # Change the x/y screen coordinates to grid coordinates
            column = (pos[0]-xDistanceFromEdge) // (width+margin)
            row = pos[1] // (height+margin)
            print((row, column))
            gameBoard[column][row] = "Black"
            
    screen.fill(greyBackground)
    boardGui(black,white)
    piecesGameBoard(gameBoard)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()