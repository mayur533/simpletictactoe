from tkinter import *
from tkinter import messagebox
from ttkthemes import ThemedStyle

def clicked(row, col):
    global player, stop
    
    # Check if the clicked cell is empty and the game is not stopped
    if state[row][col] == 0 and not stop:
        # Set the player's symbol on the clicked cell
        b[row][col].configure(text=player, bg="white", fg="brown", borderwidth=0)
        state[row][col] = player
        
        # Check if the current player has won or if the game is a tie
        check_winner(row, col)
        
        # Toggle to the other player's turn
        toggle_player()

def toggle_player():
    global player
    player = "O" if player == "X" else "X"

def check_winner(row, col):
    global stop
    
    # Check rows and columns for a win
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] == player:
            stop = True
            show_winner(player)
            break
        elif state[0][i] == state[1][i] == state[2][i] == player:
            stop = True
            show_winner(player)
            break
    
    # Check diagonals for a win
    if row == col:
        if state[0][0] == state[1][1] == state[2][2] == player:
            stop = True
            show_winner(player)
    
    if row + col == 2:
        if state[0][2] == state[1][1] == state[2][0] == player:
            stop = True
            show_winner(player)
    
    # Check if the game is a tie
    if all(state[i][j] != 0 for i in range(3) for j in range(3)):
        stop = True
        show_winner("Tie")

def show_winner(winner):
   
    if winner=="Tie":
    	messagebox.showinfo("Winner", f"{winner}")
    	reset()
    else:
    	messagebox.showinfo("Winner", f"{winner}  Won The Match ")
    	reset()

def reset():
    ans = messagebox.askquestion("Confirm", "Play Again?")
    if ans == "yes":
        for i in range(3):
            for j in range(3):
                b[i][j].configure(text="", fg="white", borderwidth=0)
                state[i][j] = 0
        global stop
        stop = False
    else:
        root.destroy()

# Create the main Tkinter window
root = Tk()
root.title("TIC TAC TOE")
root.resizable(0, 0)
root.configure(bg="grey")
# Initialize game variables
player = "X"
state = [[0, 0, 0] for _ in range(3)]
stop = False

# Create the game board using Buttons
b = [[0, 0, 0] for _ in range(3)]
for i in range(3):
    for j in range(3):
        b[i][j] = Button(root,
            height=1,
            width=3,
            padx=0,
            pady=0,
            bg="white",
            borderwidth=0,
            font=("Xtradex", 90, "bold"),
            command=lambda r=i, c=j: clicked(r, c)
        )
        b[i][j].grid(row=i, column=j)

# Start the Tkinter event loop
root.mainloop()

