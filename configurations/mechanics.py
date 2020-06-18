from configurations.configs import Config as const
from entities import pieces


class Rules:
    @staticmethod
    def position_converter(event):
        return (event.pos[1] // (const.height // 8), event.pos[0] // (const.width // 8))

    @staticmethod
    def is_contained_in(list_A, list_B):
        for i in range(0, len(list_B), 2):
            if list_A[0] == list_B[i] and list_A[1] == list_B[i + 1]:
                return True
        return False

    @staticmethod
    def get_enemys(squares, enemy_color, board):
        enemy_squares = []
        for i in range(0, len(squares), 2):
            if board[squares[i]][squares[i+1]] and board[squares[i]][squares[i+1]].color == enemy_color:
                enemy_squares.append(squares[i])
                enemy_squares.append(squares[i + 1])
        return enemy_squares

    @staticmethod
    def exist(pos_y, pos_x):
        if pos_x >= 8 or pos_y >= 8 or pos_x < 0 or pos_y < 0:
            return False
        return True

    @staticmethod
    def change_turn(turn):
        return not turn

    @staticmethod
    def verify_turn(selected, turn, board):
        y, x = selected
        if board[y][x].color == turn:
            return True
        return False

    @staticmethod
    def castling_conditions(pos_y, pos_x, start, end, color, board):
        if isinstance(board[pos_y][pos_x], pieces.Rook) and board[pos_y][pos_x].first_position:
            for i in range(start, end):
                if board[pos_y][i]:
                    return False
                if CheckSystem.verify_threaten(color, [pos_y, i], board):
                    return False
            return True
        return False

    @staticmethod
    def castling(pos_y, pos_x, board):
        possible_squares = []
        color = board[pos_y][pos_x].color

        if Rules.castling_conditions(pos_y, 0, 1, pos_x, color, board):
            possible_squares.extend([pos_y, pos_x - 3])

        if Rules.castling_conditions(pos_y, 7, pos_x + 1, 7, color, board):
            possible_squares.extend([pos_y, pos_x + 2])

        return possible_squares

    @staticmethod
    def update_kings_position(black_king, white_king, new_position, board):
        moved_piece = board[new_position[0]][new_position[1]]
        if isinstance(moved_piece, pieces.King):
            if moved_piece.color == const.black:
                return new_position, white_king
            else:
                return black_king, new_position
        return black_king, white_king

class CheckSystem:
    @staticmethod
    def verify_line_threaten(way_y, way_x, color, square, board):
        y = square[0]
        x = square[1]
        while Rules.exist(y, x):
            if board[y][x] and board[y][x].color != color:
                threaten_squares = board[y][x].mark_movements(y, x, board)
                if Rules.is_contained_in(square, threaten_squares):
                    return True
            y += 1 * way_y
            x += 1 * way_x
        return False

    @staticmethod
    def verify_knight_threaten(way_y, way_x, color, square, board):
        y = square[0]
        x = square[1]
        if Rules.exist(y + way_y, x + way_x):
            if board[y + way_y][x + way_x] and isinstance(board[y + way_y][x + way_x], pieces.Knight) and board[y + way_y][x + way_x].color != color:
                return True
        return False

    @staticmethod
    def verify_threaten(color, square, board):

        # Superior diagonals
        if CheckSystem.verify_line_threaten(-1, -1, color, square, board) or CheckSystem.verify_line_threaten(-1, 1, color, square, board):
            return True

        # Inferior diagonals
        elif CheckSystem.verify_line_threaten(1, 1, color, square, board) or CheckSystem.verify_line_threaten(1, -1, color, square, board):
            return True

        # North & South
        elif CheckSystem.verify_line_threaten(1, 0, color, square, board) or CheckSystem.verify_line_threaten(-1, 0, color, square, board):
            return True

        # Weast & East
        elif CheckSystem.verify_line_threaten(0, 1, color, square, board) or CheckSystem.verify_line_threaten(0, -1, color, square, board):
            return True

        elif CheckSystem.verify_knight_threaten(1, 2, color, square, board) or CheckSystem.verify_knight_threaten(1, -2, color, square, board):
            return True

        elif CheckSystem.verify_knight_threaten(-1, 2, color, square, board) or CheckSystem.verify_knight_threaten(-1, -2, color, square, board):
            return True

        elif CheckSystem.verify_knight_threaten(2, 1, color, square, board) or CheckSystem.verify_knight_threaten(2, -1, color, square, board):
            return True

        elif CheckSystem.verify_knight_threaten(-2, 1, color, square, board) or CheckSystem.verify_knight_threaten(-2, -1, color, square, board):
            return True

        return False
    
    @staticmethod
    def king_treatment(color, ps_y, ps_x, new_possible_squares, board_cpy, mult):
        board_cpy[ps_y][ps_x - mult] = board_cpy[ps_y][ps_x + mult]
        board_cpy[ps_y][ps_x + mult] = None
        if not CheckSystem.verify_threaten(color, [ps_y, ps_x], board_cpy):
            new_possible_squares.append(ps_y)
            new_possible_squares.append(ps_x)
        board_cpy[ps_y][ps_x + mult] = board_cpy[ps_y][ps_x - mult]
        board_cpy[ps_y][ps_x - mult] = None

    @staticmethod
    def check_filter(king, possible_squares, selected, board):
        s_y = selected[0]
        s_x = selected[1]
        new_possible_squares = []
        board_cpy = board.copy()
        color = board_cpy[s_y][s_x].color

        for i in range(0, len(possible_squares), 2):
            ps_y = possible_squares[i]
            ps_x = possible_squares[i + 1]
            # Move
            mem_piece = board_cpy[ps_y][ps_x]
            board_cpy[ps_y][ps_x] = board_cpy[s_y][s_x]
            board_cpy[s_y][s_x] = None

            if selected == king:
                if ps_x > s_x + 1:
                    CheckSystem.king_treatment(color, ps_y, ps_x, new_possible_squares, board_cpy, 1)
                elif ps_x < s_x - 1:
                    CheckSystem.king_treatment(color, ps_y, ps_x, new_possible_squares, board_cpy, -1)
                else:
                    if not CheckSystem.verify_threaten(color, [ps_y, ps_x], board_cpy):
                        new_possible_squares.append(ps_y)
                        new_possible_squares.append(ps_x)
            else:
                if not CheckSystem.verify_threaten(color, king, board_cpy) and selected != king:
                    new_possible_squares.append(ps_y)
                    new_possible_squares.append(ps_x)

            # Comeback
            board_cpy[s_y][s_x] = board_cpy[ps_y][ps_x]
            board_cpy[ps_y][ps_x] = mem_piece

        return new_possible_squares

    @staticmethod
    def checkmate(color, king, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] and board[i][j].color == color:
                    moves = []
                    moves = board[i][j].mark_movements(i, j, board)
                    moves = CheckSystem.check_filter(king, moves, [i, j], board)
                    if moves:
                        return False
        return True