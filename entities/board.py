from configurations.configs import Config as const

from entities.pieces import (
    Bishop,
    King,
    Knight,
    Pawn,
    Queen,
    Rook
)


class Board:
    stardard_board = \
        [[Rook(const.black), Knight(const.black), Bishop(const.black), Queen(const.black), King(const.black), Bishop(const.black), Knight(const.black), Rook(const.black)],
         [Pawn(const.black), Pawn(const.black), Pawn(const.black), Pawn(const.black), Pawn(const.black), Pawn(const.black), Pawn(const.black), Pawn(const.black)],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [Pawn(const.white), Pawn(const.white), Pawn(const.white), Pawn(const.white), Pawn(const.white), Pawn(const.white), Pawn(const.white), Pawn(const.white)],
         [Rook(const.white), Knight(const.white), Bishop(const.white), Queen(const.white), King(const.white), Bishop(const.white), Knight(const.white), Rook(const.white)]]
    
    black_king_position = [0, 4]
    white_king_position = [7, 4]