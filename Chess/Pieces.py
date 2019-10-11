import pygame
from Constant import *


def exist(pos_y, pos_x):
    if pos_x >= 8 or pos_y >= 8 or pos_x < 0 or pos_y < 0:
        return False
    return True


class Bishop:
    pass


class King:
    pass


class Knight:
    pass


class Pawn:
    def __init__(self, color):
        self.first_position = True
        self.color = color
        if color:
            self.enemy_color = False
            self.mult = 1
        else:
            self.enemy_color = True
            self.mult = -1

    def mark_movements(self, pos_x, pos_y, board):
        possible_squares = []
        if (
            exist(pos_y + self.mult, pos_x)
            and board[pos_y + self.mult][pos_x][0] == Const.none
        ):
            possible_squares.append(pos_x)
            possible_squares.append(pos_y + self.mult)
            if (
                exist(pos_y + 2 * self.mult, pos_x)
                and self.first_position
                and board[pos_y + 2 * self.mult][pos_x][0] == Const.none
            ):
                possible_squares.append(pos_x)
                possible_squares.append(pos_y + 2 * self.mult)

        if (
            exist(pos_y + self.mult, pos_x + self.mult)
            and board[pos_y + self.mult][pos_x + self.mult][1] == self.enemy_color
        ):
            possible_squares.append(pos_x + self.mult)
            possible_squares.append(pos_y + self.mult)

        if (
            exist(pos_y + self.mult, pos_x - self.mult)
            and board[pos_y + self.mult][pos_x - self.mult][1] == self.enemy_color
        ):
            possible_squares.append(pos_x - self.mult)
            possible_squares.append(pos_y + self.mult)

        return possible_squares


class Queen:
    pass


class Rook:
    pass
