
class board:
    def __init__(self,size) -> None:
        self.reset(size)
    def reset(self,size):
        self.size=size
        self.matrix=[[" " for i in range(size)] for j in range(size)]
        self.forward_diag={}
        self.backward_diag={}
        self.row={}
        self.col={}
    def place_marker(self,pos_x,pos_y,player) -> bool:
        if self.matrix[pos_x][pos_y]!=" ":
            return NameError
        marker=player
        self.matrix[pos_x][pos_y]=marker
        self.row[pos_x]=self.row.get(pos_x,{})
        self.row[pos_x][marker]=self.row[pos_x].get(marker,0)+1
        if self.row[pos_x][marker]==self.size:
            return True
        print("Row",self.row,self.row[pos_x][marker])
        self.col[pos_y]=self.col.get(pos_y,{})
        self.col[pos_y][marker]=self.col[pos_y].get(marker,0)+1
        if self.col[pos_y][marker]==self.size:
            return True
        print("Col",self.col,self.col[pos_y][marker])

        
        if pos_x==pos_y:
            self.forward_diag[marker]=self.forward_diag.get(marker,0)+1
            if self.forward_diag[marker]==self.size:
                return True
            print("Forward",self.forward_diag,self.forward_diag[marker])
        if pos_x+pos_y+1==self.size:
            
            self.backward_diag[marker]=self.backward_diag.get(marker,0)+1
            if self.backward_diag[marker]==self.size:
                return True
            print("Backward",self.backward_diag,self.backward_diag[marker])
        return False
    def print_board(self):
        print()
        print()
        print(" ------------------- ")
        for i in self.matrix:
            for j in i:

                print(" | ",end=" ")
                print(j,end=" ")        
            print(" |")
            print(" ------------------- ")



class game:
    def __init__(self,player1,player2,board) -> None:
        self.player1=player1
        self.player2=player2
        self.board=board
    def start(self):
        turn=1
        gameDone=False
        while not gameDone:
            x,y=map(int,input("Enter the X and Y pos in board to place marker : ").split(" "))
            x=x-1
            y=y-1
            if turn%2==1:
                if self.board.place_marker(x,y,self.player1.marker):
                    self.board.print_board()
                    gameDone=True
                    print("{} wins".format(self.player1.name))
                else:
                    self.board.print_board()
                    turn+=1
            else:
                if self.board.place_marker(x,y,self.player2.marker):
                    self.board.print_board()
                    gameDone=True
                    print("{} wins".format(self.player2.name))
                else:
                    self.board.print_board()
                    turn+=1
        
class player:
    def __init__(self,name,marker) -> None:
        self.name=name
        self.marker=marker

player1=player("Gaurav","X")
player2=player("Kesav","O")
Board=board(3)
Game=game(player1,player2,Board)
Game.start()

        
        