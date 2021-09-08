
from tkinter import *
from tkinter import messagebox

window = Tk()
BACKGROUND_COLOR = "#000000"
player_1, player_2 = "X" , "O"


board = [["", "" , ""], ["", "" , ""] , ["", "" , ""]]
current_player = player_1

buttons = []

grid_pos = {}
grid_pos[1] = (0,0)
grid_pos[2] = (0,1)
grid_pos[3] = (0,2)
grid_pos[4] = (1,0)
grid_pos[5] = (1,1)
grid_pos[6] = (1,2)
grid_pos[7] = (2,0)
grid_pos[8] = (2,1)
grid_pos[9] = (2,2)

win_combinations = [[1,2,3], [4,5,6], [7,8,9], # horizontal
                    [1,4,7], [2,5,8], [3,6,9], # vertical
                    [1,5,9], [3,5,7]] # diagonal

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

def reset_game():
    global current_player, board
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    current_player = player_1
    for btn in buttons:
        btn.config(text="")
    lbl_player.config(text=f"Player ({current_player})")

def game_draw():
    draw = True
    for pos in grid_pos.keys():
        r, c = grid_pos[pos]
        if board[r][c] == "":
            draw = False
            break
    return draw

def toggle_player():
    global current_player
    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1
    lbl_player.config(text=f"Player ({current_player})")

def check_status():
    win = False
    for win_comb in win_combinations:
        r1,c1 = grid_pos[win_comb[0]]
        r2,c2 = grid_pos[win_comb[1]]
        r3,c3 = grid_pos[win_comb[2]]
        if board[r1][c1] == current_player and board[r2][c2] == current_player and board[r3][c3] == current_player:
            win = True
            lbl_player.config(text=f"Player ({current_player}) wins")
            if messagebox.askyesno("Continue?", f"Player ({current_player}) wins! Do you want to continue?"):
                reset_game()
            else:
                on_closing()
            break

    if win == False:
        if game_draw():
            if messagebox.askyesno("Continue?", "Game drawn! Do you want to continue?"):
                reset_game()
            else:
                on_closing()
        else:
            toggle_player()

def update_board(btn, row, column):
    if board[row][column] == "":
        btn.config(text=current_player,fg="white")
        board[row][column] = current_player
        check_status()


window.title("Tic Tac Toe")
window.config(padx=50, pady=50, bg="white", width=360, height=360)

window.protocol("WM_DELETE_WINDOW", on_closing)

lbl_player = Label(window, text="Player 1 (X)", fg="black", font = "Times 12 bold")
lbl_player.grid(row=0, column=0)

btn_1 = Button(window, bg=BACKGROUND_COLOR, font="Times 15 bold",padx=10,pady=10,width=8, height=4,fg="white", command = lambda: update_board(btn_1,0,0))
btn_1.grid(row=1,column=0)

btn_2= Button(window, bg=BACKGROUND_COLOR, font="Times 15 bold",padx=10,pady=10,width=8, height=4,fg="white", command = lambda: update_board(btn_2,0,1))
btn_2.grid(row=1,column=1)

btn_3 = Button(window, bg=BACKGROUND_COLOR, font="Times 15 bold",padx=10,pady=10,width=8, height=4,fg="white", command = lambda: update_board(btn_3,0,2))
btn_3.grid(row=1,column=2)

btn_4 = Button(window, bg=BACKGROUND_COLOR, font="Times 15 bold",padx=10,pady=10,width=8, height=4,fg="white", command = lambda: update_board(btn_4,1,0))
btn_4.grid(row=2,column=0)

btn_5= Button(window, bg=BACKGROUND_COLOR, font="Times 15 bold",padx=10,pady=10,width=8, height=4,fg="white", command = lambda: update_board(btn_5,1,1))
btn_5.grid(row=2,column=1)

btn_6 = Button(window, bg=BACKGROUND_COLOR, font="Times 15 bold",padx=10,pady=10,width=8, height=4,fg="white", command = lambda: update_board(btn_6,1,2))
btn_6.grid(row=2,column=2)

btn_7 = Button(window, bg=BACKGROUND_COLOR, font="Times 15 bold",padx=10,pady=10,width=8, height=4,fg="white", command = lambda: update_board(btn_7,2,0))
btn_7.grid(row=3,column=0)

btn_8= Button(window, bg=BACKGROUND_COLOR, font="Times 15 bold",padx=10,pady=10,width=8, height=4,fg="white", command = lambda: update_board(btn_8,2,1))
btn_8.grid(row=3,column=1)

btn_9 = Button(window, bg=BACKGROUND_COLOR, font="Times 15 bold",padx=10,pady=10,width=8, height=4,fg="white", command = lambda: update_board(btn_9,2,2))
btn_9.grid(row=3,column=2)

buttons.append(btn_1)
buttons.append(btn_2)
buttons.append(btn_3)
buttons.append(btn_4)
buttons.append(btn_5)
buttons.append(btn_6)
buttons.append(btn_7)
buttons.append(btn_8)
buttons.append(btn_9)

window.mainloop()

