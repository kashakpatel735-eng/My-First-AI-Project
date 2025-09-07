import tkinter as tk
import random
from tkinter import messagebox

def check_winner(board, player):
    win_pos = [
        (0,1,2),(3,4,5),(6,7,8), (0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6),
    ]
    for a,b,c in win_pos:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def aiagent_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner(board, "O"):
                buttons[i].config(text="O", state="disabled")
                return
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner(board, "X"):
                board[i] = "O"
                buttons[i].config(text="O", state="disabled")
                return
            board[i] = " "

    move = random.choice([i for i in range(9) if board[i] == " "])
    board[move] = "O"
    buttons[move].config(text="O", state="disabled")

def player_move(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i].config(text="X", state="disabled")

        if check_winner(board, "X"):
            messagebox.showinfo("Game Over", "You Win!")
            root.quit()
            return

        if " " not in board:
            messagebox.showinfo("Game Over", "It's a Draw!")
            root.quit()
            return

        aiagent_move()

        if check_winner(board, "O"):
            messagebox.showinfo("Game Over", "AI agent Wins!")
            root.quit()
            return

        if " " not in board:
            messagebox.showinfo("Game Over", "It's a Draw!")
            root.quit()
            return

root = tk.Tk()
root.title("Tic Tac Toe AI")

board = [" "] * 9
buttons = []

for i in range(9):
    b = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                  command=lambda i=i: player_move(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

root.mainloop()
