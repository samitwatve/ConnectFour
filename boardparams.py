#Game Board size

COLUMN_COUNT = 7
ROW_COUNT = 6

#Parameters for the game board display in pygame

SQUARE_SIZE = 100 #pixels

CIRCLE_RADIUS = int(SQUARE_SIZE/2 - 5) #pixels
OFFSET = SQUARE_SIZE/2 #pixels
WIDTH = COLUMN_COUNT * SQUARE_SIZE #pixels
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE #pixels
SIZE = (WIDTH, HEIGHT) #pixels

#Display colors

BLACK = (0,0,0) #R,G,B
WHITE = (255,255,255) #R,G,B
BLUE = (0,0,255) #R,G,B
RED = (255,0,0) #R,G,B
YELLOW = (255,255,0) #R,G,B



