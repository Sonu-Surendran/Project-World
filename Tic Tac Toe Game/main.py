from tkinter import *

root = Tk()
root.geometry("400x600")
root.title("Tic Tac Toe")

single_player = False

def played(kt):
    """This function changes the value of 'player_value' variable for each turn"""

    #python can only access global variable but it can't make changes unless implicitly mentioned has global variable.
    global player_value, move_allowed
    
    if move_allowed:
        button = kt.widget
        button_num = str(button)
        button_num = button_num[-1]
        
        if button_num == "n":
            button_num = 1
        else:
            button_num = int(button_num)

        if button["text"] == " ":
            if player_value == "x":
                button["text"] = "X"
                board_value[button_num] = player_value

                if check_if_winner(player_value):
                    winner_label = Label(frame1, text=f"{player_value.upper()} won the game!!!", font=("Airal", 24), background="lightblue", width=19, height=1)
                    winner_label.grid(row=0, column=0, columnspan=3)
                    move_allowed = False
                elif check_if_draw():
                    game_draw_label = Label(frame1, text=f"game draw", font=("Airal", 24), background="lightblue", width=19, height=1)
                    game_draw_label.grid(row=0, column=0, columnspan=3)

                player_value = "o"

                if single_player:
                    computer_play()
                    if check_if_winner(player_value):
                        winner_label = Label(frame1, text=f"computer won!!!", font=("Airal", 24), background="lightblue", width=19, height=1)
                        winner_label.grid(row=0, column=0, columnspan=3)
                        move_allowed = False
                    elif check_if_draw():
                        game_draw_label = Label(frame1, text=f"game draw", font=("Airal", 24), background="lightblue", width=19, height=1)
                        game_draw_label.grid(row=0, column=0, columnspan=3)
                    computer_board_update()
                    player_value = "x"
            else:
                button["text"] = "O" 
                board_value[button_num] = player_value

                if check_if_winner(player_value):
                    winner_label = Label(frame1, text=f"{player_value.upper()} won the game!!!", font=("Airal", 24), background="lightblue", width=19, height=1)
                    winner_label.grid(row=0, column=0, columnspan=3)
                    move_allowed = False
                elif check_if_draw():
                    game_draw_label = Label(frame1, text=f"game draw", font=("Airal", 24), background="lightblue", width=19, height=1)
                    game_draw_label.grid(row=0, column=0, columnspan=3)

                player_value = "x"   


def check_if_winner(player_value):
    """This function checks if there is a winner at each step"""

    #checking for winner in all rows
    if board_value[1] == board_value[2] and board_value[3] == board_value[2] and board_value[3] == player_value:
        return True
    
    elif board_value[4] == board_value[5] and board_value[5] == board_value[6] and board_value[6] == player_value:
        return True
    
    elif board_value[7] == board_value[8] and board_value[8] == board_value[9] and board_value[9] == player_value:
        return True
    
    #checking for winner in all columns
    elif board_value[1] == board_value[4] and board_value[4] == board_value[7] and board_value[7] == player_value:
        return True
    
    elif board_value[2] == board_value[5] and board_value[5] == board_value[8] and board_value[8] == player_value:
        return True
    
    elif board_value[3] == board_value[6] and board_value[6] == board_value[9] and board_value[9] == player_value:
        return True
    
    #checking for winnner in diagonal
    elif board_value[1] == board_value[5] and board_value[5] == board_value[9] and board_value[9] == player_value:
        return True
    
    elif board_value[3] == board_value[5] and board_value[5] == board_value[7] and board_value[7] == player_value:
        return True

    return False


def check_if_draw():
    """This function checks if all the keys have value (X or O)"""

    for key in board_value.keys():
        if board_value[key] == " ":
            return False
    return True
        

def restart_game():
    """Function restarts the game"""

    global player_value, move_allowed
    player_value = "x"

    for button in all_buttons:
        button["text"] = " "

    for key in board_value:
        board_value[key] = " "

    titlelabel1 = Label(frame1, text="Tic Tac Toe", font=("Airal, 24"), bg="lightblue", width=19, height=1)
    titlelabel1.grid(row=0, column=0, columnspan=3)

    move_allowed = True



def computer_play():
    """This function uses minmax algorithm to find the best possible move"""

    best_score = -100
    best_move = 0

    for key in board_value:
        if board_value[key] == " ":
            board_value[key] = "o"
            score = minmax(board_value, False)
            board_value[key] = " "

            if score > best_score:
                best_score = score
                best_move = key

    print(best_move)

    if best_move in board_value:
        board_value[best_move] = "o"


def minmax(current_board, is_computer_turn):

    if check_if_winner('o'):
        return 1
    
    elif check_if_winner("x"):
        return -1
    
    elif check_if_draw():
        return 0
    
    if is_computer_turn:
        best_score = -100

        for key in current_board:
            if current_board[key] == " ":
                current_board[key] = "o"
                score = minmax(current_board, False)
                board_value[key] = " "

                if score > best_score:
                    best_score = score

        return best_score
    
    else:
        best_score = 100

        for key in current_board:
            if current_board[key] == " ":
                current_board[key] = "x"
                score = minmax(current_board, True)
                current_board[key] = " "

                if score < best_score:
                    best_score = score

        return best_score


def computer_board_update():
    """This function update board when computer plays the game"""

    for key in board_value:
        all_buttons[key-1]["text"] = board_value.get(key).upper()


def single_player_mode():
    global single_player
    single_player = True

def multipler_player_mode():
    global single_player
    single_player = False

#To display the title inside the board
frame1 = Frame(root)
frame1.pack()
titlelabel1 = Label(frame1, text="Tic Tac Toe", font=("Airal, 24"), bg="lightblue", width=19, height=1)
titlelabel1.grid(row=0, column=0, columnspan=3)

single_player_button = Button(frame1, text = "Single Player".title(), width=19, height=1, font=("Airal, 12"), bg="lightgreen", relief=RAISED, borderwidth=5, command=single_player_mode)
single_player_button.grid(row=1, column=0)

multiple_player_button = Button(frame1, text = "Mutli player".title(), width=19, height=1, font=("Airal, 12"), bg="lightgreen", relief=RAISED, borderwidth=5, command=multipler_player_mode)
multiple_player_button.grid(row=1, column=1)

#virtual space where tic tac toe board will be contained
frame2 = Frame(root)
frame2.pack()

#This variable keeps track of the turn value (O or X)
player_value = "x"
move_allowed = True

#Dictionary which keeps track of the position occupied.
board_value = {1: " ", 2: " ", 3:" ",
               4: " ", 5: " ", 6:" ",
               7: " ", 8: " ", 9:" "}


# No Changes further ---------------------*********************-----------------------------------------------

#create button for all 3 columns and 3 rows

#creating first row
button1 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver", relief=RAISED, borderwidth=5)
button1.grid(row=0, column=0)
button1.bind("<Button-1>", played)

button2 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver", relief=RAISED, borderwidth=5)
button2.grid(row=0, column=1)
button2.bind("<Button-1>", played)

button3 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver", relief=RAISED, borderwidth=5)
button3.grid(row=0, column=2)
button3.bind("<Button-1>", played)

#Creating second row
button4 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver", relief=RAISED, borderwidth=5)
button4.grid(row=1, column=0)
button4.bind("<Button-1>", played)

button5 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver", relief=RAISED, borderwidth=5)
button5.grid(row=1, column=1)
button5.bind("<Button-1>", played)

button6 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver", relief=RAISED, borderwidth=5)
button6.grid(row=1, column=2)
button6.bind("<Button-1>", played)

#Creating third row
button7 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver", relief=RAISED, borderwidth=5)
button7.grid(row=2, column=0)
button7.bind("<Button-1>", played)

button8 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver", relief=RAISED, borderwidth=5)
button8.grid(row=2, column=1)
button8.bind("<Button-1>", played)

button9 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver", relief=RAISED, borderwidth=5)
button9.grid(row=2, column=2)
button9.bind("<Button-1>", played)

#creating a list to store all the button variable for restart function
all_buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

restart_button = Button(frame2, text = "restart game".title(), width=19, height=1, font=("Airal, 23"), bg="lightgreen", relief=RAISED, borderwidth=5, command=restart_game)
restart_button.grid(row=3, column=0, columnspan=3)


root.mainloop()