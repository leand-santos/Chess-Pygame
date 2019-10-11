import pygame
from Constant import *
from Pieces import *


def Draw_Board(board):
    for i in range(8):
        for j in range(8):
            if j % 2 == 0:
                if i % 2 == 0:
                    Image.screen.blit(
                        Image.white_square,
                        (Const.width // 8 * j, Const.height // 8 * i),
                    )
                else:
                    Image.screen.blit(
                        Image.black_square,
                        (Const.width // 8 * j, Const.height // 8 * i),
                    )
            else:
                if i % 2 == 0:
                    Image.screen.blit(
                        Image.black_square,
                        (Const.width // 8 * j, Const.height // 8 * i),
                    )
                else:
                    Image.screen.blit(
                        Image.white_square,
                        (Const.width // 8 * j, Const.height // 8 * i),
                    )


def Draw_Pieces(board):
    for i in range(8):
        for j in range(8):
            pos_x = Const.width // 8 * j + Const.center_width
            pos_y = Const.height // 8 * i + Const.center_height
            if board[i][j][0] == Const.bishop:
                if board[i][j][1]:
                    Image.screen.blit(Image.black_bishop, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_bishop, (pos_x, pos_y))
            elif board[i][j][0] == Const.king:
                if board[i][j][1]:
                    Image.screen.blit(Image.black_king, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_king, (pos_x, pos_y))
            elif board[i][j][0] == Const.knight:
                if board[i][j][1]:
                    Image.screen.blit(Image.black_knight, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_knight, (pos_x, pos_y))
            elif board[i][j][0] == Const.pawn:
                if board[i][j][1]:
                    Image.screen.blit(Image.black_pawn, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_pawn, (pos_x, pos_y))
            elif board[i][j][0] == Const.queen:
                if board[i][j][1]:
                    Image.screen.blit(Image.black_queen, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_queen, (pos_x, pos_y))
            elif board[i][j][0] == Const.rook:
                if board[i][j][1]:
                    Image.screen.blit(Image.black_rook, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_rook, (pos_x, pos_y))


def Draw_Possible_Squares(board, possible_squares):
    for i in range(0,len(possible_squares),2):
        Image.screen.blit(
            Image.brown_square,
            (
                Const.width // 8 * possible_squares[i],
                Const.height // 8 * possible_squares[i + 1],
            ),
        )


def piece_identifier(event, board):
    pos_x = event.pos[0] // (Const.width // 8)
    pos_y = event.pos[1] // (Const.height // 8)
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
        p1 = Pawn(Const.black)
        return p1.mark_movements(pos_x, pos_y, board)
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
    return []


def main():
    end = True
    board = Const.matrix
    pygame.display.set_caption("Chess")
    possible_squares = []
    while end:
        Draw_Board(board)
        if possible_squares:
            Draw_Possible_Squares(board, possible_squares)
        Draw_Pieces(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                possible_squares = piece_identifier(event, board)
        pygame.display.update()


main()
