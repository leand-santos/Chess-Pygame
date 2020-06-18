from configurations.mechanics import Rules as rules


class Piece:
    def __init__(self, color):
        self.color = color
        self.enemy_color = not color

    def mark_movements(self, pos_y, pos_x, board):
        raise NotImplementedError

    def travels_towards(self, pos_y, pos_x, board, mult_y, mult_x):
        possible_squares = []
        while rules.exist(pos_y, pos_x):
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

    def walk_one(self, pos_y, pos_x, board):
        possible_squares = []
        if rules.exist(pos_y, pos_x):
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


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []

        possible_squares.extend(super().travels_towards(
            pos_y + 1, pos_x + 1, board, 1, 1))
        possible_squares.extend(super().travels_towards(
            pos_y - 1, pos_x + 1, board, -1, 1))
        possible_squares.extend(super().travels_towards(
            pos_y + 1, pos_x - 1, board, 1, -1))
        possible_squares.extend(super().travels_towards(
            pos_y - 1, pos_x - 1, board, -1, -1))

        return possible_squares


class King(Piece):
    def __init__(self, color):
        self.first_position = True
        super().__init__(color)


    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []

        possible_squares.extend(super().walk_one(pos_y + 1, pos_x, board))
        possible_squares.extend(super().walk_one(pos_y - 1, pos_x, board))
        possible_squares.extend(super().walk_one(pos_y, pos_x + 1, board))
        possible_squares.extend(super().walk_one(pos_y, pos_x - 1, board))

        possible_squares.extend(super().walk_one(pos_y + 1, pos_x + 1, board))
        possible_squares.extend(super().walk_one(pos_y - 1, pos_x + 1, board))
        possible_squares.extend(super().walk_one(pos_y + 1, pos_x - 1, board))
        possible_squares.extend(super().walk_one(pos_y - 1, pos_x - 1, board))

        if self.first_position:
            possible_squares.extend(rules.castling(pos_y, pos_x, board))

        return possible_squares


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []

        possible_squares.extend(self.walk_one(pos_y + 1, pos_x + 2, board))
        possible_squares.extend(self.walk_one(pos_y + 1, pos_x - 2, board))
        possible_squares.extend(self.walk_one(pos_y - 1, pos_x + 2, board))
        possible_squares.extend(self.walk_one(pos_y - 1, pos_x - 2, board))

        possible_squares.extend(self.walk_one(pos_y + 2, pos_x + 1, board))
        possible_squares.extend(self.walk_one(pos_y + 2, pos_x - 1, board))
        possible_squares.extend(self.walk_one(pos_y - 2, pos_x + 1, board))
        possible_squares.extend(self.walk_one(pos_y - 2, pos_x - 1, board))

        return possible_squares


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.first_position = True
        if color:
            self.side = 1
        else:
            self.side = -1

    def walk_one(self, pos_y, pos_x, board):
        possible_squares = []
        if rules.exist(pos_y, pos_x):
            if not board[pos_y][pos_x]:
                possible_squares.append(pos_y)
                possible_squares.append(pos_x)
        return possible_squares

    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []
        diagonal_enemys = []

        possible_squares.extend(Pawn.walk_one(
            self, pos_y + 1 * self.side, pos_x, board))

        if self.first_position == True and possible_squares:
            possible_squares.extend(Pawn.walk_one(
                self, pos_y + 2 * self.side, pos_x, board))

        diagonal_enemys.extend(super().walk_one(
            pos_y + 1 * self.side, pos_x - 1, board))
        diagonal_enemys.extend(super().walk_one(
            pos_y + 1 * self.side, pos_x + 1, board))

        possible_squares.extend(rules.get_enemys(
            diagonal_enemys, self.enemy_color, board))

        return possible_squares


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []

        # Diagonals
        possible_squares.extend(
            super().travels_towards(pos_y + 1, pos_x + 1, board, 1, 1)
        )
        possible_squares.extend(
            super().travels_towards(pos_y - 1, pos_x + 1, board, -1, 1)
        )
        possible_squares.extend(
            super().travels_towards(pos_y + 1, pos_x - 1, board, 1, -1)
        )
        possible_squares.extend(
            super().travels_towards(pos_y - 1, pos_x - 1, board, -1, -1)
        )

        # North, South, East, West
        possible_squares.extend(super().travels_towards(
            pos_y + 1, pos_x, board, 1, 0))
        possible_squares.extend(super().travels_towards(
            pos_y - 1, pos_x, board, -1, 0))
        possible_squares.extend(super().travels_towards(
            pos_y, pos_x + 1, board, 0, 1))
        possible_squares.extend(super().travels_towards(
            pos_y, pos_x - 1, board, 0, -1))

        return possible_squares


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.first_position = True

    def mark_movements(self, pos_y, pos_x, board):
        possible_squares = []

        possible_squares.extend(super().travels_towards(pos_y + 1, pos_x, board, 1, 0))
        possible_squares.extend(super().travels_towards(pos_y - 1, pos_x, board, -1, 0))
        possible_squares.extend(super().travels_towards(pos_y, pos_x + 1, board, 0, 1))
        possible_squares.extend(super().travels_towards(pos_y, pos_x - 1, board, 0, -1))

        return possible_squares
