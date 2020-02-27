# Global Vars----

board = ["-","-","-",
         "-","-","-", 
         "-","-","-"]

game_still_playing = True

winner = None


current_player = "x"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():

    #display first
    display_board()

    while game_still_playing:

    handle_turn(current_player)

    check_game_end()

    switch_player()

    if winner == "x" or winner == "o":
        print (winner + "won!")
    elif winner == None:
        print("Issa Tie")



def handle_turn(player):
    position = input("Choosev your position from 1-9: ")
    position = int(position) - 1

    board[position] = "x"

    display_board()

def check_game_end():
    win_check()
    tie_check()

def win_check():

    global winner

    #rows
    row_winner = row_check()

    col_winner = col_check()

    diag_winner = diag_check()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner

    else:
        winner = None
    return

def row_check():
    global game_still_playing
    #equal value check between rows
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_still_playing = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def col_check():
    global game_still_playing
    #equal value check between rows
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        game_still_playing = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


def diag_check():
        global game_still_playing
    #equal value check between rows
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"
    if diag1 or diag2:
        game_still_playing = False
    if diag1:
        return board[0]
    elif diag2:
        return board[]
    
    return


def tie_check():
    
    return

def switch_player():
    
    return


play_game


#display board
#play game function
#handle turns
#win check/row/column/diagonal
#tie check
#switch player