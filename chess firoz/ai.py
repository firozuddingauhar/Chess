import random
from board import Square

class Bot:
    def evaluate_board(board):
        eval=0
        for row in range(8):
            for col in range(8):
                if board.squares[row][col].piece != None:
                    if board.squares[row][col].piece.color=='white':
                        eval = eval + board.squares[row][col].piece.value
                    if board.squares[row][col].piece.color=='black':
                        eval = eval - board.squares[row][col].piece.value
        return eval
    
    def random_bot_move(board,color):
        while True:
            row=random.randint(0,7)
            col=random.randint(0,7)
            if board.squares[row][col].piece != None:
                if board.squares[row][col].piece.color==color:
                    board.squares[row][col].piece.calc_valid_moves(row,col,board.squares[row][col].piece,board)
                    if board.squares[row][col].piece.valid_moves != []:
                        move=random.choice(board.squares[row][col].piece.valid_moves)
                        board.squares[row][col].piece.valid_moves = []
                        send=[row,col,move]
                        return send
                        
    # def minimax(self,board,depth,alpha,beta,color):
        
    #     if depth==0:
    #         return self.evaluate_board(board)
    #     if color=='black':
    #         max_eval= -696969
    #         for row in range (7):
    #             for col in range (7):
    #                 if board.squares[row][col].piece != None:
    #                     if board.squares[row][col].piece.color==color:
    #                         board.squares[row][col].piece.calc_valid_moves(row,col,board.squares[row][col].piece,board)
    #                         possiblie_moves= board.squares[row][col].piece.valid_moves
    #                         for move in possiblie_moves:
    #                             move_row , move_col = move
    #                             board.squares[move_row][move_col] = board.squares[row][col]
    #                             board.squares[row][col] = Square(row,col) 
    #                             eval = self.minimax(self,board,depth-1,alpha,beta,'white')
    #                             max_eval = max(eval , max_eval)
    #                             board.squares[row][col]=board.squares[move_row][move_col]
    #                             board.squares[move_row][move_col]= Square(row,col) 
    #                             alpha = max( alpha , eval)
    #                             if beta<=alpha:
    #                                 break
    #         return max_eval
    #     else:
    #         min_eval= 696969
    #         for row in range (7):
    #             for col in range (7):
    #                 if board.squares[row][col].piece != None:
    #                     if board.squares[row][col].piece.color==color:
    #                         board.squares[row][col].piece.calc_valid_moves(row,col,board.squares[row][col].piece,board)
    #                         possiblie_moves= board.squares[row][col].piece.valid_moves
    #                         for move in possiblie_moves:
    #                             move_row , move_col = move
    #                             board.squares[move_row][move_col] = board.squares[row][col]
    #                             board.squares[row][col] = Square(row,col) 
    #                             eval = self.minimax(self,board,depth-1,alpha,beta,'black')
    #                             min_eval = min(eval , min_eval)
    #                             board.squares[row][col]=board.squares[move_row][move_col]
    #                             board.squares[move_row][move_col]= Square(row,col)
    #                             beta = min( beta , eval)
    #                             if beta<=alpha:
    #                                 break
    #         return min_eval
        
    # def Bot_move(self,board,color):
    #     max_eval=-696969
    #     best_move=0
    #     best_row=-1
    #     best_col=-1
    #     for row in range (8):
    #         for col in range (8):
    #             if board.squares[row][col].piece != None:
    #                 if board.squares[row][col].piece.color==color:
    #                     board.squares[row][col].piece.calc_valid_moves(row,col,board.squares[row][col].piece,board)
    #                     possiblie_moves= board.squares[row][col].piece.valid_moves
    #                     for move in possiblie_moves:
    #                         move_row , move_col = move
    #                         board.squares[move_row][move_col] = board.squares[row][col]
    #                         board.squares[row][col] = Square(row,col) 
    #                         # eval = self.minimax(self,board,1,-696969,696969,'white')
    #                         eval=Bot.evaluate_board(board)
    #                         board.squares[row][col]=board.squares[move_row][move_col]
    #                         board.squares[move_row][move_col]= Square(move_row,move_col) 
    #                         if eval > max_eval:
    #                             max_eval = eval
    #                             best_move = move
    #                             best_row=row
    #                             best_col=col
    #     send=[best_row,best_col,best_move]
    #     return send

