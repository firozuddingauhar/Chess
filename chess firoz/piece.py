import os

class Piece:

    def __init__(self,name,color,texture=None):
        self.name=name
        self.color=color
        self.texture=texture
        self.valid_moves=[]

    def set_texture(self):
        self.texture=os.path.join(f'assets/{self.color}_{self.name}.png')

    def line_moves(self,row,col,piece,board,directions):
        for direction in directions:
            row_direction , col_direction =direction
            move_row =row+row_direction
            move_col =col+col_direction
            while True:
                move=(move_row,move_col)
                if move_col<8 and move_row<8:
                    if move_col>=0 and move_row>=0:
                       if board.squares[move_row][move_col].piece == None:
                           self.valid_moves.append(move)
                       elif board.squares[move_row][move_col].piece.color != piece.color:
                           self.valid_moves.append(move)
                           break
                       elif board.squares[move_row][move_col].piece.color == piece.color:
                           break
                    else:
                        break
                else:
                    break
                move_row=move_row+row_direction
                move_col=move_col+col_direction


class Pawn(Piece):

    def __init__(self,color,):
        self.value=10
        super().__init__('pawn', color)

    def calc_valid_moves(self,row,col,piece,board):
        if piece.color=='white':
            pawn_direction= -1
            pawn_rank=6
        else:
            pawn_direction= +1
            pawn_rank=1

        if board.squares[row+pawn_direction][col].piece == None:
            self.valid_moves.append((row+pawn_direction,col))
            if row==pawn_rank and board.squares[row+(2*pawn_direction)][col].piece == None:
                self.valid_moves.append((row+(2*pawn_direction),col))
        if board.squares[row+pawn_direction][col-1].piece != None:
            if piece.color != board.squares[row+pawn_direction][col-1].piece.color:
                self.valid_moves.append((row+pawn_direction,col-1))
        if col<7:
            if board.squares[row+pawn_direction][col+1].piece != None:
                if piece.color != board.squares[row+pawn_direction][col+1].piece.color:
                    self.valid_moves.append((row+pawn_direction,col+1)) 
        
class Knight(Piece):

    def __init__(self, color):
        self.value=30
        super().__init__('knight', color)

    def calc_valid_moves(self,row,col,piece,board):
        all_possible_moves = [(row-2, col+1),(row-1, col+2),(row+1, col+2),(row+2, col+1),
                              (row+2, col-1),(row+1, col-2),(row-1, col-2),(row-2, col-1),]
        for move in all_possible_moves:
            move_row,move_col=move
            if move_col<8 and move_row<8:
               if move_col>=0 and move_row>=0:
                   self.valid_moves.append(move) 
                   if board.squares[move_row][move_col].piece != None:                    
                        if piece.color == board.squares[move_row][move_col].piece.color:
                            self.valid_moves.remove(move) 

class Bishop(Piece):

    def __init__(self,color):
        self.value=30
        super().__init__('bishop', color)

    def calc_valid_moves(self,row,col,piece,board):
        directions=[(-1, 1),(-1, -1),(1, 1),(1, -1),]
        self.line_moves(row,col,piece,board,directions)

class Rook(Piece):

    def __init__(self,color):
        self.value=50
        super().__init__('rook', color)

    def calc_valid_moves(self,row,col,piece,board):
        directions=[(-1, 0),(0, 1),(1, 0),(0, -1),]
        self.line_moves(row,col,piece,board,directions)

class Queen(Piece):

    def __init__(self,color):
        self.value=90
        super().__init__('queen', color)

    def calc_valid_moves(self,row,col,piece,board):
        directions=[(-1, 1),(-1, -1),(1, 1),(1, -1),(-1, 0),(0, 1),(1, 0),(0, -1)]
        self.line_moves(row,col,piece,board,directions)

class King(Piece):

    def __init__(self,color):
        self.value=10000
        
        super().__init__('king', color)

    def calc_valid_moves(self,row,col,piece,board):
        all_possible_moves =[
                (row-1, col+0),(row-1, col+1), (row+0, col+1), (row+1, col+1), 
                (row+1, col+0),(row+1, col-1), (row+0, col-1), (row-1, col-1), 
            ]
        for move in all_possible_moves:
            move_row,move_col=move
            if move_col<8 and move_row<8:
               if move_col>=0 and move_row>=0: 
                   self.valid_moves.append(move) 
                   if board.squares[move_row][move_col].piece != None:                                         
                      if piece.color == board.squares[move_row][move_col].piece.color:
                         self.valid_moves.remove(move)
