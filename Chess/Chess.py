import pygame
from Constant import *
from Pieces import *


def Draw_Board():
    for i in range(8):
        for j in range(8):
            if j % 2 == 0:
                if i % 2 == 0:
                    Const.screen.blit(
                        Const.white_square, (Const.width//8*j, Const.height//8*i))
                else:
                    Const.screen.blit(
                        Const.black_square, (Const.width//8*j, Const.height//8*i))
            else:
                if i % 2 == 0:
                    Const.screen.blit(
                        Const.black_square, (Const.width//8*j, Const.height//8*i))
                else:
                    Const.screen.blit(
                        Const.white_square, (Const.width//8*j, Const.height//8*i))


def Draw_Pieces():
    for i in range(8):
        for j in range(8):
            pos_x = Const.width//8*j + Const.center_width
            pos_y = Const.height//8*i + Const.center_height
            if Const.matrix[i][j][0] == Const.bishop:
                if Const.matrix[i][j][1]:
                    Const.screen.blit(Const.black_bishop, (pos_x, pos_y))
                else:
                    Const.screen.blit(Const.white_bishop, (pos_x, pos_y))
            elif Const.matrix[i][j][0] == Const.king:
                if Const.matrix[i][j][1]:
                    Const.screen.blit(Const.black_king, (pos_x, pos_y))
                else:
                    Const.screen.blit(Const.white_king, (pos_x, pos_y))
            elif Const.matrix[i][j][0] == Const.knight:
                if Const.matrix[i][j][1]:
                    Const.screen.blit(Const.black_knight, (pos_x, pos_y))
                else:
                    Const.screen.blit(Const.white_knight, (pos_x, pos_y))
            elif Const.matrix[i][j][0] == Const.pawn:
                if Const.matrix[i][j][1]:
                    Const.screen.blit(Const.black_pawn, (pos_x, pos_y))
                else:
                    Const.screen.blit(Const.white_pawn, (pos_x, pos_y))
            elif Const.matrix[i][j][0] == Const.queen:
                if Const.matrix[i][j][1]:
                    Const.screen.blit(Const.black_queen, (pos_x, pos_y))
                else:
                    Const.screen.blit(Const.white_queen, (pos_x, pos_y))
            elif Const.matrix[i][j][0] == Const.rook:
                if Const.matrix[i][j][1]:
                    Const.screen.blit(Const.black_rook, (pos_x, pos_y))
                else:
                    Const.screen.blit(Const.white_rook, (pos_x, pos_y))


def piece_identifier(event, board):
    pos_x = event.pos[0]//(Const.width//8)
    pos_y = event.pos[1]//(Const.height//8)
    if board[pos_y][pos_x] == (Const.bishop, True):
        print("black_bishop")
    elif board[pos_y][pos_x] == (Const.bishop, False):
        print("white_bishop")
    elif board[pos_y][pos_x] == (Const.king, True):
        print("black_king")
    elif board[pos_y][pos_x] == (Const.king, False):
        print("white_king")
    elif board[pos_y][pos_x] == (Const.knight, True):
        print("black_knight")
    elif board[pos_y][pos_x] == (Const.knight, False):
        print("white_knight")
    elif board[pos_y][pos_x] == (Const.pawn, True):
        print("black_pawn")
    elif board[pos_y][pos_x] == (Const.pawn, False):
        print("white_pawn")
    elif board[pos_y][pos_x] == (Const.queen, True):
        print("black_queen")
    elif board[pos_y][pos_x] == (Const.queen, False):
        print("white_queen")
    elif board[pos_y][pos_x] == (Const.rook, True):
        print("black_rook")
    elif board[pos_y][pos_x] == (Const.rook, False):
        print("white_rook")


def main():
    end = True
    board = Const.matrix
    Draw_Board()
    Draw_Pieces()
    pygame.display.update()
    pygame.display.set_caption("Chess")
    while end:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                piece_identifier(event, board)


main()
