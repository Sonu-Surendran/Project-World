from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")

def played(user_input):
    """This function changes the value of 'player_value' variable for each turn"""

    button = user_input.widget

    #python can only access global variable but it can't make changes unless implicitly mentioned has global variable.
    global player_value

    if player_value == "x":
        button["text"] = "X"
        player_value = "o"
    else:
        button["text"] = "O" 
        player_value = "x"   

#To display the title inside the board
frame1 = Frame(root)
frame1.pack()
titlelabel1 = Label(frame1, text="Tic Tac Toe", font=("Airal, 18"), bg="lightblue")
titlelabel1.pack()

#virtual space where tic tac toe board will be contained
frame2 = Frame(root)
frame2.pack()

#This variable keeps track of the turn value (O or X)
player_value = "x"

#create button for all 3 columns and 3 rows

#creating first row
button1 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver")
button1.grid(row=0, column=0)
button1.bind("<Button-1>", played)

button2 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver")
button2.grid(row=0, column=1)
button2.bind("<Button-1>", played)

button3 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver")
button3.grid(row=0, column=2)
button3.bind("<Button-1>", played)

#Creating second row
button4 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver")
button4.grid(row=1, column=0)
button4.bind("<Button-1>", played)

button5 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver")
button5.grid(row=1, column=1)
button5.bind("<Button-1>", played)

button6 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver")
button6.grid(row=1, column=2)
button6.bind("<Button-1>", played)

#Creating third row
button7 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver")
button7.grid(row=2, column=0)
button7.bind("<Button-1>", played)

button8 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver")
button8.grid(row=2, column=1)
button8.bind("<Button-1>", played)

button9 = Button(frame2, text = " ", width=4, height=2, font=("Airal, 32"), bg="silver")
button9.grid(row=2, column=2)
button9.bind("<Button-1>", played)


root.mainloop()