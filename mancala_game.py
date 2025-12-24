import turtle
import sys

turtle.tracer(5)
turtle.Screen().bgcolor("light blue")

# Tuple of player's pits
P1_PITS = ("A", "B", "C", "D", "E", "F")
    
P2_PITS = ("G", "H", "I" , "J", "K", "L")

# Variable that defines the pits and values that are the next pit in order
next_Pit = {'A': 'B', 'B':'C', 'C':'D', 'D':'E', 'E':'F', 'F':'1', '1':'L','L':'K', 'K':'J', 'J':'I', 'I':'H', 'H':'G', 'G':'2', '2':'A'}

# Pit labels in counterclockwise order
pit_Labels = "ABCDEF1LKJHIG2"

# Starting number of seeds at the start of a new game 
start_num_seeds = 1


# START GAME 
def main():
    print("\n"*2)
    print("Welcome to Mancala: The Mini Version!")
    input("Press any key to begin the game. . .") #ask user to start
    VisualBoard()
    displayPebbles()
    turtle.tracer(1)

    gameTextBoard = getNewBoard()
    gameVisualBoard = getNewBoard()
    playerTurn = '1'

    while True: # Run a player's turn
        print("\n"*100) # CLEAR THE BOARD 
        displayBoard(gameTextBoard) # Display updated TEXT board
        numVisualBoard(gameVisualBoard) # Updates number of moves in one pebble on VISUAL board 
        playerMove = askPlayerMove(playerTurn, gameTextBoard) # Start player's move 
        setPebble = setPebbleMove(gameVisualBoard,playerTurn, playerMove) # Set up chosen pebble 
        playerTurn = makeMove(gameTextBoard, playerTurn, playerMove) # Execute player's move

        # Is there a winner? (Check)
        winner = checkWinner(gameTextBoard)
        if (winner == "1") or (winner == "2"):
            displayBoard(gameTextBoard)
            print("Player" + winner + " won!")
            sys.exit()
            
        elif winner == "draw":
            displayBoard(gameTextBoard) 
            print("Draw.") 
            sys.exit()
            

# TEXT BASED PLAYBOARD (FEATURE 2)
def getNewBoard():
    s = start_num_seeds
    
    return {'1': 0, '2':0, 'A':s, 'B':s,'C':s,'D':s,'E':s,'F':s,'G':s,'H':s,'I':s,'J':s,'K':s,'L':s}

def numVisualBoard(board):
    pebbleAmounts =[]
    for pit in "GHIJKLABCDEF":
        # [pit] is the list "GHIJKLABCDEF", 
        # where integers are the number of animated moves for one pebble
        numPebblesInThisPit = int(board[pit]) 
        pebbleAmounts.append(numPebblesInThisPit)

def displayBoard(board):
    pebbleAmounts = []
    for pit in "GHIJKL21ABCDEF": #order of the pits left to right and top to bottom 
        # [pit] is the list "GHIJKL21ABCDEF", 
        # where integers turn into strings values
        numPebblesInThisPit = str(board[pit]).rjust(2) 
        pebbleAmounts.append(numPebblesInThisPit)
    print("""

<<<<<<<<<<<<<<<<<<<<<<<<Player 2<<<<<<<<<<<<<<<<<<<<<<<<<
+------+------+------+------+------+------+------+------+
2      |G     |H     |I     |J     |K     |L     |      1
|      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      |
S      |      |      |      |      |      |      |      S
T  {}  +------+------+------+------+------+------+  {}  T
O      |A     |B     |C     |D     |E     |F     |      O
R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
E      |      |      |      |      |      |      |      E
+------+------+------+------+------+------+------+-------    
>>>>>>>>>>>>>>>>>>>>>>>>Player 1>>>>>>>>>>>>>>>>>>>>>>>>>

""".format(*pebbleAmounts))

def askPlayerMove(playerTurn, board):
    while True: # Ask player to enter a move
        if playerTurn == '1':
            print("Player 1, choose your move [A-F] (or QUIT): ")
        elif playerTurn == '2':
            print("Player 2, choose your move [G-L] (or QUIT): ")
        response = input(' ').upper().strip() # uppercases response and strips aware blank spaces

        if response == "QUIT":
            print("\n")
            print("its okay i understand. thx for playing tho")
            print("\n")
            sys.exit()
            break
        # Make sure it is a valid pit to select
        if (playerTurn == '1' and response not in P1_PITS) or (playerTurn == '2' and response not in P2_PITS):
            print("Please pick a letter on your side of the board.")
            continue # iterates command until appropriate response given
        if board.get(response) == 0:
            print("Please pick a non-empty pit.")
            continue # iterates command until appropriate response given
        return response
    

def makeMove(board, playerTurn, pit):
    currentPebs = board[pit] #collect current number of seeds from player's choice of pit
    board[pit] = 0 # empty player's choice of pit 

    while currentPebs > 0: # places pebbles until none left
        pit = next_Pit[pit] # Places pebble in each pit counterclockwise 
        if (playerTurn == '1' and pit == '2') or (playerTurn == '2' and pit =='1'): # pits == '2' and pits == '1' refer to player's storage
            continue # make sure to skip opponent's storage 
        board[pit] +=1
        currentPebs -=1  

    # Returns other player as the next player i.e '1' or '2' 
    if playerTurn == '1':
        return '2'
    elif playerTurn == '2':
        return '1'

def setPebbleMove(board, playerTurn, playerMove):
    import random 
    # assign random color to the selected pebble 
    color = random.choice(["red","dark olive green","deep pink","cyan","gold","orange"]) 
    pebble = turtle.Turtle()
    pebble.color(color)
    pebble.speed(2)

    # move of visual pebble cooresponds to user input selection of 'ABCDEFGHIJKL' on text-based display board
    # turns alternate between player1 and player2
    # if a player's number of moves within a pebble reaches their own storage, turtle is stamped, 
    # then, animation of moves carries onto the other player's side of the board 
    y = -65
    if (playerTurn == '1'): 
        pebble.penup()
        pebble.setheading(0)
        if playerMove == 'A':  
            pebble.shape("circle")
            pebble.goto(-175,y)
            pebble.forward(70*board['A'])
            pebble.hideturtle()
            if board['F'] < 2 and next_Pit == '1':
                pebble.shape("circle")
                pebble.goto(175,y)
                pebble.setheading(180)
                pebble.goto(250,0)
                pebble.stamp()
        elif playerMove == 'B': 
            pebble.shape("turtle")
            pebble.goto(-105,y)
            pebble.forward(70*board['B'])
            pebble.hideturtle()
            if board['F'] < 2 and next_Pit == '1':
                pebble.shape("turtle")
                pebble.goto(175,y)
                pebble.setheading(180)
                pebble.goto(250,0)
                pebble.stamp()
        elif playerMove == 'C': 
            pebble.shape("square")
            pebble.goto(-35,y)
            pebble.forward(70*board['C'])
            pebble.hideturtle()
            if board['F'] < 2 and next_Pit == '1':
                pebble.shape("square")
                pebble.goto(175,y)
                pebble.setheading(180)
                pebble.goto(250,0)
                pebble.stamp()
        elif playerMove == 'D':
            pebble.shape("triangle")
            pebble.goto(35,y)
            pebble.forward(70*board['D'])
            pebble.hideturtle()
            if board['F'] < 2 and next_Pit == '1':
                pebble.goto(175,y)
                pebble.setheading(180)
                pebble.goto(250,0)
                pebble.stamp()
        elif playerMove == 'E': 
            pebble.shape("circle")
            pebble.goto(105,y)
            pebble.forward(70*board['E'])
            pebble.hideturtle()
            if board['F'] == 2:
                pebble.goto(175,y)
                pebble.setheading(180)
                pebble.goto(250,0)
                pebble.stamp()
        elif playerMove == 'F'and board ['F'] < 2:
            pebble.shape("turtle")
            pebble.goto(175,y)
            pebble.setheading(180)
            pebble.goto(250,0)
            pebble.stamp() 
            if playerMove == 'F' and board['F'] > 1: 
                board['F'] = board['F'] - 1 
                pebble.goto(175,y)
                pebble.setheading(180)
                pebble.goto(170,-y)
                pebble.forward(70*(board['F']))
                pebble.hideturtle()


    y = 65      
    if (playerTurn == '2'):
        pebble.setheading(180)
        pebble.penup()
        if playerMove == 'G' and board['G'] < 2:
            pebble.shape("circle")
            pebble.goto(-180,y)
            pebble.setheading(0)
            pebble.goto(-250,0)
            if playerMove == 'G' and board['G'] > 1:
                board['G'] = board['G'] - 1
                pebble.goto(-180,y)
                pebble.setheading(0)
                pebble.goto(-175,-y)
                pebble.forward(70*board['G'])
                pebble.hideturtle()
        elif playerMove == 'H': 
            pebble.shape("turtle")
            pebble.goto(-110,y)
            pebble.forward(70*board['H'])
            pebble.hideturtle()
            if board['G'] == 2:
                pebble.shape("turtle")
                pebble.goto(-180,y)
                pebble.setheading(0)
                pebble.goto(-250,0)
                pebble.stamp()
        elif playerMove == 'I': 
            pebble.shape("square")
            pebble.goto(-40,y)
            pebble.forward(70*board['I'])
            pebble.hideturtle()
            if board['G'] < 2 and next_Pit == '2':
                pebble.shape("square")
                pebble.goto(-180,y)
                pebble.setheading(0)
                pebble.goto(-250,0)
                pebble.stamp()
        elif playerMove == 'J': 
            pebble.shape("triangle")
            pebble.goto(30,y)
            pebble.forward(70*board['J'])
            pebble.hideturtle()
            if board['G'] < 2 and next_Pit == '2':
                pebble.shape("triangle")
                pebble.goto(-180,y)
                pebble.setheading(0)
                pebble.goto(-250,0)
                pebble.stamp()
        elif playerMove == 'K': 
            pebble.shape("circle")
            pebble.goto(100,y)
            pebble.forward(70*board['K'])
            pebble.hideturtle()
            if board['G'] < 2 and next_Pit == '2':
                pebble.shape("circle")
                pebble.goto(-180,y)
                pebble.setheading(0)
                pebble.goto(-250,0)
                pebble.stamp()
        elif playerMove == 'L': 
            pebble.shape("turtle")
            pebble.goto(170,y)
            pebble.forward(70*board['L'])
            pebble.hideturtle()
            if board['G'] < 2 and next_Pit == '2':
                pebble.shape("turtle")
                pebble.goto(-180,y)
                pebble.setheading(0)
                pebble.goto(-250,0)
                pebble.stamp()

def checkWinner(board): 
    # Game ends when one player's side of their pits is empty. Any remaining pebbles on the other player's side will be added
    # to their storage at this point, clearing out all pits he whole board, except the storages. 
    # The winner is the player who has the most pebbles

    player1Total = board['A'] + board['B'] + board['C'] + board['D'] + board['E'] + board['F']
    player2Total = board['G'] + board['H'] + board['I'] + board['J'] + board['K'] + board['L']

    if (player1Total == 0): # when no remaining pebbles for player 1's side
        board['2'] += player2Total # remaining pebbles on player 2's side is added to their storage 
        for pit in P2_PITS: 
            board[pit] = 0 # Sets all pits to zero 
    
    elif (player2Total == 0): # when no remaining pebbles for player 2's side
        board['1'] += player1Total # remaining pebbles on player 1's side is added to their storage 
        for pit in P1_PITS: 
            board[pit] = 0 # Sets all pits to zero
    
    else: 
        return 'no winner' # game continues until endgame 

    # Game is over, player with largest score wins. 
    if board['1'] > board['2']:
        return '1'
    elif board['2'] > board['1']:
        return '2'
    elif board['1'] == board['2']: # tie if scores are equal 
        return 'draw'

# VISUAL-OUTPUT DISPLAY BOARD (FEATURE 1)
def VisualBoard():
    board = turtle.Turtle()
    board.hideturtle()

    #Configure base board 
    col = "burlywood"
    board.penup()
    board.pencolor(col)
    board.fillcolor(col)
    board.goto(-250,-100)
    board.pendown()
    board.pensize(100)
    board.begin_fill()
    for base_board in range (2):
        board.forward(500)
        board.left(90)
        board.forward(200)
        board.left(90)
    board.end_fill()

    # Configure pits / storage
    startx = -175
    starty = -100
    board.setheading(90)
    board.pensize(50)
    col = "peru"
    board.pencolor(col)
    board.penup()

    # Create 2 rows and 6 columns of pits
    for pits in range (2):
        for pits in range (6):
            board.goto(startx,starty)
            board.pendown()
            board.forward(60)
            board.penup()
            startx = startx + 70
        startx = startx - 420
        starty = starty + 140

    # Create player storages
    board.goto(-250,-100)
    board.pendown()
    for storage in range (2):
        board.forward(200)
        board.penup()
        board.goto(250,-100)
        board.pendown() 

def displayPebbles(): 
    # Create an empty list of pebbles
    players_pebbles = []

    # Use various shapes and colors 
    pebble_shapes = ["circle", "turtle", "square", "triangle","circle", "turtle"]
    pebble_colors = ["blue", "blue", "blue", "blue", "blue", "blue","blue", "blue", "blue", "blue", "blue", "blue"]

    ploc = -175
    starty = -65
    direction = 0
    
    #setup pebbles on page
    for rows in range(2):
        for pebbles in pebble_shapes:
            pebs = turtle.Turtle(shape=pebbles) 
            players_pebbles.append(pebs)
            pebs.penup()
            new_color = pebble_colors.pop()
            pebs.color(new_color)
            pebs.goto(ploc, starty)
            pebs.setheading(direction)
            ploc += 70
        direction = direction + 180
        ploc = ploc - 425
        starty = starty + 130


main()

wn = turtle.Screen()
wn.mainloop()