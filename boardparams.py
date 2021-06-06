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

#For scoring

WINDOW_SIZE = 4

#Rolling windows

horizontal_windows, vertical_windows, pos_diag_windows, neg_diag_windows = [], [], [], []

#horizontal windows
for c in range(COLUMN_COUNT-3):
    for r in range(ROW_COUNT):
        horizontal_windows.append([(r, c), (r, c+1), (r, c+2), (r,c+3)])

#vertical windows        
for c in range(COLUMN_COUNT):
    for r in range(ROW_COUNT-3):
        vertical_windows.append([(r, c), (r+1, c), (r+2, c), (r+3,c)])

#positively sloping diagonal windows
for c in range(COLUMN_COUNT-3):
    for r in range(ROW_COUNT-3):
        pos_diag_windows.append([(r, c), (r+1, c+1), (r+2, c+2), (r+3,c+3)])

#negatively sloping diagonal windows
for c in range(COLUMN_COUNT-4,COLUMN_COUNT):
    for r in range(ROW_COUNT-3):
        neg_diag_windows.append([(r, c), (r+1, c-1), (r+2, c-2), (r+3,c-3)])

