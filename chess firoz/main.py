import pygame
import sys 
from piece import *
from board import *
from ai import Bot

WIDTH=HEIGHT=800
ROWS=COLS=8
SQUARESIZE=WIDTH//COLS

class Main:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game=Game()
        self.bot=Bot()
        Game.show_background(self.screen)
        self.game.show_pieces(self.screen)
        
    def mainloop(self):
        while True:
            pygame.display.update()
            Game.show_background(self.screen)
            self.game.show_pieces(self.screen)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #dragging piece
                if self.game.current_player=='white':
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        inital_x, inital_y = pygame.mouse.get_pos()
                        inital_x_index=inital_x//SQUARESIZE
                        inital_y_index=inital_y//SQUARESIZE
                        initial_square=self.game.board.squares[inital_y_index][inital_x_index]
                        if initial_square.piece != None and initial_square.piece.color==self.game.current_player:
                            initial_square.piece.calc_valid_moves(inital_y_index,inital_x_index,initial_square.piece,self.game.board)
                            Game.show_moves(self.screen,initial_square.piece.valid_moves)

                    if event.type==pygame.MOUSEBUTTONUP:
                        if initial_square.piece != None and initial_square.piece.color==self.game.current_player:
                            final_x, final_y = pygame.mouse.get_pos()
                            final_x_index=final_x//SQUARESIZE
                            final_y_index=final_y//SQUARESIZE
                            if inital_x_index != final_x_index  or inital_y_index != final_y_index:
                                if (final_y_index,final_x_index) in initial_square.piece.valid_moves:
                                    final_square=self.game.board.squares[final_y_index][final_x_index]
                                    self.game.board.squares[final_y_index][final_x_index] = initial_square
                                    self.game.board.squares[inital_y_index][inital_x_index] = Square(inital_y,inital_x)
                                    print(Bot.evaluate_board(self.game.board))
                                    initial_square.piece.valid_moves=[]
                                    self.game.board.squares[final_y_index][final_x_index].piece.calc_valid_moves(final_y_index,final_x_index,self.game.board.squares[final_y_index][final_x_index].piece,self.game.board)
                                    nextmove=self.game.board.squares[final_y_index][final_x_index].piece.valid_moves
                                    for moves in nextmove:
                                        move_x , move_y = moves
                                        if self.game.board.squares[move_x][move_y].piece != None and self.game.board.squares[move_x][move_y].piece.name=='king':
                                            print("check")
                                            initial_square.piece.valid_moves=[]
                                            break               
                                    self.game.next_turn()
                elif Bot.evaluate_board(self.game.board)>1000:
                    pygame.quit()
                    sys.exit()
                else:
                    recived=Bot.random_bot_move(self.game.board,'black')
                    row,col,move=recived
                    move_row,move_col=move
                    self.game.board.squares[move_row][move_col]=self.game.board.squares[row][col]
                    self.game.board.squares[row][col]= Square(row,col)
                    self.game.next_turn()

                    

            pygame.time.Clock().tick(20)


class Game:

    def __init__(self):
         self.current_player='white'
         self.board= Board()
           
    def show_background(surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) %2 == 0:
                    color=(234,235,200)
                else :
                    color=(119,154,88)
                rect=(col*SQUARESIZE,row*SQUARESIZE,SQUARESIZE,SQUARESIZE)
                pygame.draw.rect(surface,color,rect)

    def show_moves(surface,valid_moves):
            for move in valid_moves:
                move_row,move_col=move
                color = (255,0,0) if (move_row + move_col) % 2 == 0 else (245,0,0)
                rect = (move_col * SQUARESIZE, move_row * SQUARESIZE, SQUARESIZE, SQUARESIZE)
                pygame.draw.rect(surface, color, rect)
            
    def show_pieces(self,surface):
         for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece                    
                    piece.set_texture()
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQUARESIZE + SQUARESIZE // 2, row * SQUARESIZE + SQUARESIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)

    def next_turn(self):
        if self.current_player== "white":
             self.current_player = "black"
        else:
             self.current_player = "white"

main=Main()
main.mainloop()
