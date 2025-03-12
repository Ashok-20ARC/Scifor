import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self,root):
        self.root=root
        self.root.title("Tic Tac Toe")
        self.current_player="X"
        self.buttons=[[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        
    def create_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]=tk.Button(self.root,text="",font=("Arial",24),height=2,width=5,command=lambda r=row,c=col:self.make_move(r,c))
                self.buttons[row][col].grid(row=row,column=col)
                
    def make_move(self,row,col):
        if self.buttons[row][col]["text"]=="":
            self.buttons[row][col]["text"]=self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over",f"Player {self.current_player} wins!")
                self.reset_board()
                
            elif self.check_draw():
                messagebox.showinfo("Game Over","It's a draw!")
                self.reset_board()
                
            else:
                self.switch_player()
                
        else:
            messagebox.showwarning("Invalid Move","This cell is already occupied!")
            
    def switch_player(self):
        self.current_player = "O" if self.current_player=='X' else "X"
        
    def check_winner(self):
        
        for row in range(3):
            if (self.buttons[row][0]["text"]==self.buttons[row][1]["text"]==self.buttons[row][2]["text"]==self.current_player):
                return True
        
        for col in range(3):
            if (self.buttons[0][col]["text"]==self.buttons[1][col]["text"]==self.buttons[2][col]["text"]==self.current_player):
                return True
            
        if (self.buttons[0][0]['text']==self.buttons[1][1]['text']==self.buttons[2][2]['text']==self.current_player):
            return True
        
        if (self.buttons[0][2]['text']==self.buttons[1][1]['text']==self.buttons[2][0]['text']==self.current_player):
            return True
        return False
    
    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]['text']=="":
                    return False
        return True
    
    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text']=""
        self.current_player="X"
        
root=tk.Tk()
game=TicTacToe(root)
root.mainloop()