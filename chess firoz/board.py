from piece import *

class Board:

    def __init__(self):
        self.squares = [ [  0,    0,    0,    0,    0,    0,    0,    0],  #8
                         [  0,    0,    0,    0,    0,    0,    0,    0],  #7
                         [  0,    0,    0,    0,    0,    0,    0,    0],  #6
                         [  0,    0,    0,    0,    0,    0,    0,    0],  #5
                         [  0,    0,    0,    0,    0,    0,    0,    0],  #4
                         [  0,    0,    0,    0,    0,    0,    0,    0],  #3
                         [  0,    0,    0,    0,    0,    0,    0,    0],  #2
                         [  0,    0,    0,    0,    0,    0,    0,    0] ] #1
                         #  a     b     c     d     e     f     g     h
        self.create_board()
        self.add_piece("white")
        self.add_piece("black")

    def create_board(self):
        for row in range(8):
            for col in range(8):
                self.squares[row][col]=Square(row,col)

    def add_piece(self,color):
        if color == 'white':
            pawn_row=6
            piece_row=7
        else:
            pawn_row=1
            piece_row=0
        #pawn
        for col in range(8):
            self.squares[pawn_row][col] = Square(pawn_row, col, Pawn(color))
        # knights
        self.squares[piece_row][1] = Square(piece_row, 1, Knight(color))
        self.squares[piece_row][6] = Square(piece_row, 6, Knight(color))
        # bishops
        self.squares[piece_row][2] = Square(piece_row, 2, Bishop(color))
        self.squares[piece_row][5] = Square(piece_row, 5, Bishop(color))
        # rooks
        self.squares[piece_row][0] = Square(piece_row, 0, Rook(color))
        self.squares[piece_row][7] = Square(piece_row, 7, Rook(color))
        # queen
        self.squares[piece_row][3] = Square(piece_row, 3, Queen(color))
        # king
        self.squares[piece_row][4] = Square(piece_row, 4, King(color))       

class Square:
    def __init__(self,row,col,piece=None):
        self.row=row
        self.col=col
        self.piece=piece

    def has_piece(self):
        return self.piece !=None
