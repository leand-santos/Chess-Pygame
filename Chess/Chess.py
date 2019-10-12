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
            if board[i][j] == Const.bishop:
                if board[i][j]:
                    Image.screen.blit(Image.black_bishop, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_bishop, (pos_x, pos_y))
            elif board[i][j] == Const.king:
                if board[i][j]:
                    Image.screen.blit(Image.black_king, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_king, (pos_x, pos_y))
            elif board[i][j] == Const.knight:
                if board[i][j]:
                    Image.screen.blit(Image.black_knight, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_knight, (pos_x, pos_y))
            elif board[i][j] == Const.pawn:
                if board[i][j]:
                    Image.screen.blit(Image.black_pawn, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_pawn, (pos_x, pos_y))
            elif board[i][j] == Const.queen:
                if board[i][j]:
                    Image.screen.blit(Image.black_queen, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_queen, (pos_x, pos_y))
            elif board[i][j] == Const.rook:
                if board[i][j]:
                    Image.screen.blit(Image.black_rook, (pos_x, pos_y))
                else:
                    Image.screen.blit(Image.white_rook, (pos_x, pos_y))


def Draw_Possible_Squares(board, possible_squares):
    for i in range(0, len(possible_squares), 2):
        Image.screen.blit(
            Image.brown_square,
            (
                Const.height // 8 * possible_squares[i + 1],
                Const.width // 8 * possible_squares[i],
            ),
        )


def position_converter(event):
    return (event.pos[1] // (Const.height // 8), event.pos[0] // (Const.width // 8))


def piece_identifier(event, board, turn):
    pos_y, pos_x = position_converter(event)
    if board[pos_y][pos_x] == (Const.bishop, True) and turn == Const.black:
        print("black_bishop")
    elif board[pos_y][pos_x] == (Const.bishop, False) and turn == Const.white:
        print("white_bishop")
    elif board[pos_y][pos_x] == (Const.king, True) and turn == Const.black:
        print("black_king")
    elif board[pos_y][pos_x] == (Const.king, False) and turn == Const.white:
        print("white_king")
    elif board[pos_y][pos_x] == (Const.knight, True) and turn == Const.black:
        print("black_knight")
    elif board[pos_y][pos_x] == (Const.knight, False) and turn == Const.white:
        print("white_knight")
    elif board[pos_y][pos_x] == (Const.pawn, True) and turn == Const.black:
        p1 = Pawn(Const.black)
        return p1.mark_movements(pos_y, pos_x, board), (pos_y, pos_x)
        print("black_pawn")
    elif board[pos_y][pos_x] == (Const.pawn, False) and turn == Const.white:
        p2 = Pawn(Const.white)
        return p2.mark_movements(pos_y, pos_x, board), (pos_y, pos_x)
        print("white_pawn")
    elif board[pos_y][pos_x] == (Const.queen, True) and turn == Const.black:
        print("black_queen")
    elif board[pos_y][pos_x] == (Const.queen, False) and turn == Const.white:
        print("white_queen")
    elif board[pos_y][pos_x] == (Const.rook, True) and turn == Const.black:
        print("black_rook")
    elif board[pos_y][pos_x] == (Const.rook, False) and turn == Const.white:
        print("white_rook")
    return [], []


def verify_movement(possible_squares, selected):
    for i in range(0, len(possible_squares), 2):
        if (
            possible_squares[i] == selected[0]
            and possible_squares[i + 1] == selected[1]
        ):
            return [possible_squares[i], possible_squares[i + 1]]
    return []


def change_turn(turn):
    if turn == Const.white:
        return Const.black
    else:
        return Const.white


def move_piece(destin, selected, board):
    if board[selected[0]][selected[1]][0] == Const.pawn:
        p3 = Pawn(board[selected[0]][selected[1]][1])
        print(selected)
        board = p3.move_pawn(selected, destin, board)
        return board
    return board


def main():
    end = True
    pygame.display.set_caption("Chess")

    turn = Const.white
    board = Const.matrix
    possible_squares = []
    selected = []
    destin = []

    while end:
        Draw_Board(board)
        if possible_squares:
            Draw_Possible_Squares(board, possible_squares)
        Draw_Pieces(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(possible_squares,destin,selected)
                if possible_squares:
                    destin = verify_movement(
                        possible_squares, (position_converter(event))
                    )
                if destin:
                    board = move_piece(destin, selected, board)
                    turn = change_turn(turn) 
                    possible_squares = []
                    destin = []
                else:
                    possible_squares, selected = piece_identifier(event, board, turn)
                print(possible_squares,destin,selected)
        pygame.display.update()


main()
