import pygame

from interface.draw import Draw
from entities.board import Board
from configurations.configs import Config as const
from configurations.mechanics import Rules as rules
from configurations.mechanics import CheckSystem as check_sys
from animations.move import Movement as mov


class Chess:

    pygame.display.set_caption("Chess")
    Clock = pygame.time.Clock
    c = Clock()

    chess_board = Board.stardard_board.copy()
    black_king = Board.black_king_position
    white_king = Board.white_king_position
    possible_squares = []
    selected = []
    current_turn = const.initial_turn

    while True:

        Draw.draw_board()
        Draw.draw_pieces(chess_board)
        if selected:
            Draw.draw_possible_squares(chess_board, possible_squares, selected)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_y, pos_x = rules.position_converter(event)
                if rules.exist(pos_y, pos_x):
                    # Move selected piece
                    if selected and mov.verify_destin([pos_y, pos_x], possible_squares):
                        if rules.verify_turn(selected, current_turn, chess_board):
                            mov.move_piece(
                                selected, [pos_y, pos_x], chess_board)
                            black_king, white_king = rules.update_kings_position(
                                black_king, white_king, [pos_y, pos_x], chess_board)
                            selected = []
                            current_turn = rules.change_turn(current_turn)
                            if current_turn and check_sys.verify_threaten(current_turn, black_king, chess_board):
                                if check_sys.checkmate(const.black, black_king, chess_board):
                                    print("Checkmate")
                            elif check_sys.verify_threaten(current_turn, white_king, chess_board):
                                if check_sys.checkmate(const.white, white_king, chess_board):
                                    print("Checkmate")
                    # Select piece
                    elif chess_board[pos_y][pos_x] and rules.verify_turn([pos_y, pos_x], current_turn, chess_board):
                        possible_squares = chess_board[pos_y][pos_x].mark_movements(
                            pos_y, pos_x, chess_board)
                        selected = [pos_y, pos_x]
                        if chess_board[pos_y][pos_x].color == const.black:
                            possible_squares = check_sys.check_filter(black_king, possible_squares, selected, chess_board)
                        else:
                            possible_squares = check_sys.check_filter(white_king, possible_squares, selected, chess_board)
                        
        c.tick(40)
        pygame.display.update()
