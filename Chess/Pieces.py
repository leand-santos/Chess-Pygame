import pygame
from Constant import *

def exist(pos_y, pos_x):
    if pos_x >= 8 or pos_y >= 8 or pos_x < 0 or pos_y < 0:
        return False
    return True


class Bishop:
    def __init__(self, color):
        self.color = color


class King:
    def __init__(self, color):
        self.color = color


class Knight:
    def __init__(self, color):
        self.color = color


class Pawn:
    def __init__(self, color):
        self.first_position = True
        self.color = color
        if color:
            self.enemy_color = False
            self.mult = 1
            self.last_square = 7
        else:
            self.last_square = 0
            self.enemy_color = True
            self.mult = -1

    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []

        # One square ahead
        if (
            exist(pos_y + self.mult, pos_x)
            and board[pos_y + self.mult][pos_x] == None
        ):
            possible_squares.append(pos_y + self.mult)
            possible_squares.append(pos_x)

            # Two squares ahead
            if (
                exist(pos_y + 2 * self.mult, pos_x)
                and self.first_position
                and board[pos_y + 2 * self.mult][pos_x] == None
            ):
                possible_squares.append(pos_y + 2 * self.mult)
                possible_squares.append(pos_x)

        # Enemy on diagonal
        if (
            exist(pos_y + self.mult, pos_x + self.mult)
            and board[pos_y + self.mult][pos_x + self.mult] != None
            and board[pos_y + self.mult][pos_x + self.mult].color == self.enemy_color
        ):
            possible_squares.append(pos_y + self.mult)
            possible_squares.append(pos_x + self.mult)

        # Enemy on diagonal
        if (
            exist(pos_y + self.mult, pos_x - self.mult)
            and board[pos_y + self.mult][pos_x - self.mult] != None
            and board[pos_y + self.mult][pos_x - self.mult].color == self.enemy_color
        ):
            possible_squares.append(pos_y + self.mult)
            possible_squares.append(pos_x - self.mult)

        return possible_squares

    def move_piece(self, selected, destin, board):
        self.first_position = False
        if destin[0] == self.last_square:
            board[destin[0]][destin[1]] = Queen(self.color)
        else:
            board[destin[0]][destin[1]] = board[selected[0]][selected[1]]
        board[selected[0]][selected[1]] = None
        return board


class Queen:
    def __init__(self, color):
        self.color = color


class Rook:
    def __init__(self, color):
        self.color = color
