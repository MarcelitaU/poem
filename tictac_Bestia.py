def evaluate (board: str) -> str:
    
    r=""
    if len(board)==20:
    
        if "xxx" in board:
            r="x"
        elif "ooo" in board:
            r="o"
        elif "-" not in board:
            r="!"
        else: 
            r="-"
    else: 
        print("The board is invalid")
    return r

def move (board: str, mark: str, position: int) -> str:
    board= board[:position]+mark+board[position+1:]
    return board

 

def player_move (board: str) -> str:
    invalid=True
    while invalid:
        print("Please enter a valid position, with a number between 0 and 20")
        position=input("Which position do you want to play?")
        try:
            position=int(position)
            
        except:
            print("Please enter a number")
        if ((type(position) is int) and (position > 0) and (position < 20)):
            board=move(board, "x", position)
            invalid=False
   
    return board



def pc_move (board: str) -> str:
    import random
    empty=False
    while not empty:
        position=random.randint(0, 19)
        
        if board[position] == "-":
            board=move(board, "o", position)
            empty=True
    return board

def D_tictactoe ():
   
    r="-"
    board="--------------------"
    while r=="-":
        board=player_move(board)
        board=pc_move(board)
        print(board)
        r=evaluate(board)
    if r=="x":
        print("Player wins")
    elif r=="o":
        print("PC wins")
    elif r=="!":
        print("It is a draw")
     
    return board

