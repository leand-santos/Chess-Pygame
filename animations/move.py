from entities.pieces import (
    King,
    Pawn,
    Rook
)


class Movement:

    @staticmethod
    def change_first_move(selected):
        if isinstance(selected, King) or isinstance(selected, Pawn) or isinstance(selected, Rook):
            selected.first_position = False

    @staticmethod
    def verify_destin(destin, possible_squares):
        for i in range(0, len(possible_squares), 2):
            if destin[0] == possible_squares[i] and destin[1] == possible_squares[i+1]:
                return True
        return False

    @staticmethod
    def castling_move(destin, board):
        y , x = destin
        if board[y][x - 1]:
            board[y][x + 1] = board[y][x - 1]
            board[y][x - 1] = None
            Movement.change_first_move(board[y][x + 1])

        else:
            board[y][x - 1] = board[y][x + 1]
            board[y][x + 1] = None
            Movement.change_first_move(board[y][x - 1])

    @staticmethod
    def verify_castling_move(selected, destin, board):
        y = 0
        x = 1
        if isinstance(board[selected[y]][selected[x]], King):
            if destin[x] > selected[x] + 1 or destin[x] < selected[x] - 1:
                return True
        return False

    @staticmethod
    def move_piece(selected, destin, board):
        y = 0
        x = 1

        Movement.change_first_move(board[selected[y]][selected[x]])

        if Movement.verify_castling_move(selected, destin, board):
            Movement.castling_move(destin, board)

        board[destin[y]][destin[x]] = board[selected[y]][selected[x]]
        board[selected[y]][selected[x]] = None
        return board
