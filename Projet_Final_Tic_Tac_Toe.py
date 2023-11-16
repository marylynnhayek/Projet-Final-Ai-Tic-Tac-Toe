# Projet Final Intelligence Artificielle:
# Karim Fallakha - 192484
# Mary-Lynn El Hayek - 191359

from tkinter import *
import time
from tkinter import messagebox

Main_Game_Window =Tk() # Create a new window and name it Main_Main_Main_Game_Window
Main_Game_Window.title("Tic Tac Toe Final Project 2023") # Game Window Title
Main_Game_Window.configure(background="#E0F4FF") # Change the bg colour of the main window.
Font = ("Times New Roman", 14, "italic") # Syntax is: (font_family, font_size, font_weight)
DISABLED_COLOR = "#808080"  # You can adjust this color

def PlayVsAI():
    global x 
    Child_Window = Toplevel(Main_Game_Window,background="#E0F4FF")
    Child_Window.title("Play Against an AI")

    # Define 2 types of players:
    global player # The user
    global bot # The Ai
    bot="X"

    # Allow the user to make a move, and call the Ai once he's made his valid move:
    def UserTurn(button_index):        
        i=int(button_index[0])
        global UserTurn
        UserTurn=True
        if Userchoice(button_UserChoice["text"],i):
            UserTurn=False
        if UserTurn== False:
            Bot_Turn()

    def EmptySpot(position):
        return x[position] == 0

    # Clear the Tic Tac Toe game board by resetting all of the buttons to their empty state.
    def ResetBoard(): 
        for i in x: # Iterate through the buttons on the screen.
            i[1]["text"]=""
            i[2]=0
        return True # Return true if board has cleared successfully.

    def Userchoice(Player_sign, positioner):
        if EmptySpot(positioner)==0:
            x[positioner][1]["text"]=button_UserChoice["text"]
            x[positioner][2]=1
            if (CheckIfTie()):
                messagebox.showinfo("Game Status", "It's a Tie!")
                Child_Window.destroy()
                ResetBoard()       
            if CheckIfWin():
                if Player_sign == button_UserChoice["text"]:
                    ResetBoard()                                       
                else:
                    messagebox.showinfo("Game Over", "Bot wins!")
                    Child_Window.destroy()        
                    ResetBoard()
        x[positioner][1]["state"] = "disabled"
        x[positioner][1]["disabledforeground"] = "black"  # You can adjust this color
        x[positioner][1]["highlightbackground"] = "gray"  # You can adjust this color
        x[positioner][1]["highlightcolor"] = "gray"  # You can adjust this color


        return True
        return False

    def SetBotMove(BotSign, position):
        if x[position][2]==0:      # If the position is not already filled.     
            x[position][1]["text"]=bot
            x[position][2]=2
            
            if (CheckIfTie()):
                messagebox.showinfo("Game Status", "It's a Tie!")
                x_turn=True
                Child_Window.destroy()
                ResetBoard()   
            
            if CheckIfWin():
                if BotSign == bot:
                    messagebox.showinfo("Game Over", "Bot wins!")   
                    Child_Window.destroy()   
                    ResetBoard()   
                else:
                    messagebox.showinfo("Game Status", "User Wins")
                    Child_Window.destroy()
                    ResetBoard()   
        x[position][1]["state"] = "disabled"
        x[position][1]["disabledforeground"] = "black"  # You can adjust this color
        x[position][1]["highlightbackground"] = "gray"  # You can adjust this color
        x[position][1]["highlightcolor"] = "gray"  # You can adjust this color
        return

    def CheckIfTie():
            for i in x:
                if (i[2] == 0):
                    return False
            return True  

    # Checking all combinations: Vertical, Horizontal and Diagonal:
    def CheckIfWin():
        return (
            (x[0][2] == x[1][2] == x[2][2] != 0) or
            (x[3][2] == x[4][2] == x[5][2] != 0) or
            (x[6][2] == x[7][2] == x[8][2] != 0) or
            (x[0][2] == x[3][2] == x[6][2] != 0) or
            (x[1][2] == x[4][2] == x[7][2] != 0) or
            (x[2][2] == x[5][2] == x[8][2] != 0) or
            (x[0][2] == x[4][2] == x[8][2] != 0) or
            (x[6][2] == x[4][2] == x[2][2] != 0)
        )

    def check_winner(x_o):
        return (
        (x[0][2] == x[1][2] == x[2][2] == x_o) or
        (x[3][2] == x[4][2] == x[5][2] == x_o) or
        (x[6][2] == x[7][2] == x[8][2] == x_o) or
        (x[0][2] == x[3][2] == x[6][2] == x_o) or
        (x[1][2] == x[4][2] == x[7][2] == x_o) or
        (x[2][2] == x[5][2] == x[8][2] == x_o) or
        (x[0][2] == x[4][2] == x[8][2] == x_o) or
        (x[6][2] == x[4][2] == x[2][2] == x_o)
    )

    def Bot_Turn(): 
        bestScore = -2 
        bestMove = 0   
        for i in x: 
            if (i[2] == 0): 
                i[2] = 2
                score = minimax(x, 0, -float('inf'), float('inf'), False)  # Fix here
                i[2] = 0
                if (score > bestScore): 
                    bestScore = score
                    bestMove = int(i[0]) 
        SetBotMove(bot, bestMove)
        return

    # Minimax Algorithm using Alpha-Beta Pruning:
    def minimax(board, depth, alpha, beta, is_max):
        if check_winner(2):
            return 1
        elif check_winner(1):
            return -1
        elif CheckIfTie():
            return 0

        if is_max:
            best_score = -2
            for i in x:
                if i[2] == 0:
                    i[2] = 2
                    score = minimax(x, depth + 1, alpha, beta, False)
                    i[2] = 0
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
            return best_score
        else:
            best_score = 2
            for i in x:
                if i[2] == 0:
                    i[2] = 1
                    score = minimax(x, depth + 1, alpha, beta, True)
                    i[2] = 0
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
            return best_score


    # To ensure that the player symbol is as chosen and is different than the bot's symbol:
    def split():
        global bot
        if button_UserChoice["text"]=="O":
            button_UserChoice["text"]="X"
            player=button_UserChoice["text"]
            bot="O"
        else:
            player="O"
            bot="X"

    # Switch roles between the user and the bot.
    def first_player():
        if y[1]["text"]=="Bot":
           y[1]["text"]="You"
        else:
            global firstPLayer
            SetBotMove(bot,4)
            y[1]["text"]="Bot"

    def get():
        # Initialize the player and bot symbols based on the current text of the button.
        player=button_UserChoice["text"]
        if player=="O":
            bot="X"
    def RestartGame():
        # Reset the game state, enable all buttons, and clear the board
        for i in x:
            i[1]["state"] = "normal"
            i[1]["text"] = ""
            i[2] = 0
    def QuitGame():
        Main_Game_Window.destroy()
         
    # For the GUI: We made sure to keep the design responsive:
    # Creating the buttons and making them responsive:
    button1 = Button(Child_Window, text=" ", fg="white", bg="#39A7FF", font=Font, command=lambda m=["0"]:[UserTurn(m)], padx=40,pady=30)
    button2 = Button(Child_Window, text=" ", fg="white", bg="#39A7FF", font=Font, command=lambda m=["1"]:[UserTurn(m)], padx=40,pady=30)
    button3 = Button(Child_Window, text=" ", fg="white", bg="#39A7FF", font=Font, command=lambda m=["2"]:[UserTurn(m)], padx=40,pady=30)
    button4 = Button(Child_Window, text=" ", fg="white", bg="#39A7FF", font=Font, command=lambda m=["3"]:[UserTurn(m)], padx=40,pady=30)
    button5 = Button(Child_Window, text=" ", fg="white", bg="#39A7FF", font=Font, command=lambda m=["4"]:[UserTurn(m)], padx=40,pady=30)
    button6 = Button(Child_Window, text=" ", fg="white", bg="#39A7FF", font=Font, command=lambda m=["5"]:[UserTurn(m)], padx=40,pady=30)
    button7 = Button(Child_Window, text=" ", fg="white", bg="#39A7FF", font=Font, command=lambda m=["6"]:[UserTurn(m)], padx=40,pady=30)
    button8 = Button(Child_Window, text=" ", fg="white", bg="#39A7FF", font=Font, command=lambda m=["7"]:[UserTurn(m)], padx=40,pady=30)
    button9 = Button(Child_Window, text=" ", fg="white", bg="#39A7FF", font=Font, command=lambda m=["8"]:[UserTurn(m)], padx=40,pady=30)
    
    # User can change the following settings:
    Label_Change_Sign=Label(Child_Window,text="Change Sign",fg="white",bg="#0802A3",font=Font)
    button_UserChoice=Button(Child_Window,text="O",fg="white",bg="#0802A3",command=lambda m=["O"]:split(),font=Font,padx=5)
    Label_Start_Game=Label(Child_Window,text="Start Game",fg="white",bg="#0802A3",font=Font)
    button_switch_player=Button(Child_Window,text="you",fg="white",bg="#0802A3",command=lambda m=["you"]:first_player(),font=Font)
    
    x=[["0",button1,0],
       ["1",button2,0],
       ["2",button3,0],
       ["3",button4,0],
       ["4",button5,0],
       ["5",button6,0],
       ["6",button7,0],
       ["7",button8,0],
       ["8",button9,0],
       ]
    
    for i in range(3):  # Assuming you have 3 rows
        Child_Window.grid_rowconfigure(i, weight=1)

    for i in range(5):  # Assuming you have 5 columns
        Child_Window.grid_columnconfigure(i, weight=1)

    button1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    button2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    button3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
    button4.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    button5.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    button6.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
    button7.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    button8.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
    button9.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

    Label_Change_Sign.grid(row=3, column=0, padx=20, pady=5, sticky="nsew")
    button_UserChoice.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

    Label_Start_Game.grid(row=4, column=0, padx=20, pady=5, sticky="nsew")
    button_switch_player.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

    button_RestartGame = Button(Child_Window, text="Restart Game", fg="white", bg="#0802A3", command=RestartGame, font=Font, padx=5, pady=5)
    button_RestartGame.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

    button_QuitGame = Button(Child_Window, text="Quit Game", fg="white", bg="#0802A3", command=QuitGame, font=Font, padx=5, pady=5)
    button_QuitGame.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

    y=[button_UserChoice,button_switch_player]

# To make the design responsive:
for i in range(3):
    Main_Game_Window.rowconfigure(i, weight=1)
    Main_Game_Window.columnconfigure(i, weight=1)

def QuitGame() :
   Main_Game_Window.destroy() # Call this function to click on the button to exit the game and close the window.

# Main Window Buttons:
button_Bot = Button(Main_Game_Window, text="Play Game", fg="white", bg="#0802A3", command=PlayVsAI, font=Font, padx=112, pady=30)
button_QuitGame = Button(Main_Game_Window, text="Quit Game", fg="white", bg="#0802A3", command=QuitGame, font=Font, padx=112, pady=30)
button_Bot.grid(row=0, column=0, sticky="W", padx=5, pady=5)
button_QuitGame.grid(row=1, column=0, sticky="W", padx=5, pady=5)

Main_Game_Window.mainloop()