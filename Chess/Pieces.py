import pygame
from Constant import *


def exist(pos_y, pos_x):
    if pos_x >= 8 or pos_y >= 8 or pos_x < 0 or pos_y < 0:
        return False
    return True


def travels_towards(self, pos_y, pos_x, board, mult_y, mult_x):
    possible_squares = []
    while exist(pos_y, pos_x):
        if board[pos_y][pos_x] != None and board[pos_y][pos_x].color == self.color:
            return possible_squares
        elif (
            board[pos_y][pos_x] != None
            and board[pos_y][pos_x].color == self.enemy_color
        ):
            possible_squares.append(pos_y)
            possible_squares.append(pos_x)
            return possible_squares
        else:
            possible_squares.append(pos_y)
            possible_squares.append(pos_x)
        pos_y += 1 * mult_y
        pos_x += 1 * mult_x
    return possible_squares


def verify_just_one(self, pos_y, pos_x, board):
    possible_squares = []
    if exist(pos_y, pos_x):
        if board[pos_y][pos_x] != None and board[pos_y][pos_x].color == self.color:
            return possible_squares
        elif (
            board[pos_y][pos_x] != None
            and board[pos_y][pos_x].color == self.enemy_color
        ):
            possible_squares.append(pos_y)
            possible_squares.append(pos_x)
            return possible_squares
        else:
            possible_squares.append(pos_y)
            possible_squares.append(pos_x)
    return possible_squares


class Bishop:
    def __init__(self, color):
        self.color = color
        if color:
            self.enemy_color = False
        else:
            self.enemy_color = True

    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []

        possible_squares.extend(
            travels_towards(self, pos_y + 1, pos_x + 1, board, 1, 1)
        )
        possible_squares.extend(
            travels_towards(self, pos_y - 1, pos_x + 1, board, -1, 1)
        )
        possible_squares.extend(
            travels_towards(self, pos_y + 1, pos_x - 1, board, 1, -1)
        )
        possible_squares.extend(
            travels_towards(self, pos_y - 1, pos_x - 1, board, -1, -1)
        )

        return possible_squares

    def move_piece(self, selected, destin, board):
        board[destin[0]][destin[1]] = board[selected[0]][selected[1]]
        board[selected[0]][selected[1]] = None
        return board


class King:
    def __init__(self, color):
        self.color = color
        if color:
            self.enemy_color = False
        else:
            self.enemy_color = True

    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []

        possible_squares.extend(verify_just_one(self, pos_y + 1, pos_x, board))
        possible_squares.extend(verify_just_one(self, pos_y - 1, pos_x, board))
        possible_squares.extend(verify_just_one(self, pos_y, pos_x + 1, board))
        possible_squares.extend(verify_just_one(self, pos_y, pos_x - 1, board))

        return possible_squares

    def move_piece(self, selected, destin, board):
        board[destin[0]][destin[1]] = board[selected[0]][selected[1]]
        board[selected[0]][selected[1]] = None
        return board


class Knight:
    def __init__(self, color):
        self.color = color
        if color:
            self.enemy_color = False
        else:
            self.enemy_color = True

    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []

        possible_squares.extend(verify_just_one(self, pos_y + 1, pos_x + 2, board))
        possible_squares.extend(verify_just_one(self, pos_y + 1, pos_x - 2, board))
        possible_squares.extend(verify_just_one(self, pos_y - 1, pos_x + 2, board))
        possible_squares.extend(verify_just_one(self, pos_y - 1, pos_x - 2, board))

        possible_squares.extend(verify_just_one(self, pos_y + 2, pos_x + 1, board))
        possible_squares.extend(verify_just_one(self, pos_y + 2, pos_x - 1, board))
        possible_squares.extend(verify_just_one(self, pos_y - 2, pos_x + 1, board))
        possible_squares.extend(verify_just_one(self, pos_y - 2, pos_x - 1, board))

        return possible_squares

    def move_piece(self, selected, destin, board):
        board[destin[0]][destin[1]] = board[selected[0]][selected[1]]
        board[selected[0]][selected[1]] = None
        return board


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
        possible_squares.extend(verify_just_one(self, pos_y + self.mult, pos_x, board))

        # Two squares ahead
        if possible_squares:
            if self.first_position:
                possible_squares.extend(
                    verify_just_one(self, pos_y + self.mult * 2, pos_x, board)
                )

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
        if color:
            self.enemy_color = False
        else:
            self.enemy_color = True

    def mark_movements(self, pos_y, pos_x, board):

        possible_squares = []

        # Diagonals
        possible_squares.extend(
            travels_towards(self, pos_y + 1, pos_x + 1, board, 1, 1)
        )
        possible_squares.extend(
            travels_towards(self, pos_y - 1, pos_x + 1, board, -1, 1)
        )
        possible_squares.extend(
            travels_towards(self, pos_y + 1, pos_x - 1, board, 1, -1)
        )
        possible_squares.extend(
            travels_towards(self, pos_y - 1, pos_x - 1, board, -1, -1)
        )

        # North, South, East, West
        possible_squares.extend(travels_towards(self, pos_y + 1, pos_x, board, 1, 0))
        possible_squares.extend(travels_towards(self, pos_y - 1, pos_x, board, -1, 0))
        possible_squares.extend(travels_towards(self, pos_y, pos_x + 1, board, 0, 1))
        possible_squares.extend(travels_towards(self, pos_y, pos_x - 1, board, 0, -1))

        return possible_squares

    def move_piece(self, selected, destin, board):
        board[destin[0]][destin[1]] = board[selected[0]][selected[1]]
        board[selected[0]][selected[1]] = None
        return board


class Rook:
    def __init__(self, color):
        self.color = color
        if color:
            self.enemy_color = False
        else:
            self.enemy_color = True

    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []

        possible_squares.extend(travels_towards(self, pos_y + 1, pos_x, board, 1, 0))
        possible_squares.extend(travels_towards(self, pos_y - 1, pos_x, board, -1, 0))
        possible_squares.extend(travels_towards(self, pos_y, pos_x + 1, board, 0, 1))
        possible_squares.extend(travels_towards(self, pos_y, pos_x - 1, board, 0, -1))

        return possible_squares

    def move_piece(self, selected, destin, board):
        board[destin[0]][destin[1]] = board[selected[0]][selected[1]]
        board[selected[0]][selected[1]] = None
        return board
