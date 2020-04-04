import pygame
from interface.image_loader import Loader as img
from configurations.configs import Config as const
from entities.pieces import (
    Bishop,
    King,
    Knight,
    Pawn,
    Queen,
    Rook
)


class Draw:

    @staticmethod
    def draw_board():
        for i in range(8):
            for j in range(8):
                if j % 2 == 0:
                    if i % 2 == 0:
                        img.screen.blit(
                            img.white_square,
                            (const.width // 8 * j, const.height // 8 * i),
                        )
                    else:
                        img.screen.blit(
                            img.black_square,
                            (const.width // 8 * j, const.height // 8 * i),
                        )
                else:
                    if i % 2 == 0:
                        img.screen.blit(
                            img.black_square,
                            (const.width // 8 * j, const.height // 8 * i),
                        )
                    else:
                        img.screen.blit(
                            img.white_square,
                            (const.width // 8 * j, const.height // 8 * i),
                        )

    @staticmethod
    def draw_pieces(board):
        for i in range(8):
            for j in range(8):
                pos_x = const.width // 8 * j + const.center_width
                pos_y = const.height // 8 * i + const.center_height
                if isinstance(board[i][j], Bishop):
                    if board[i][j].color:
                        img.screen.blit(img.black_bishop, (pos_x, pos_y))
                    else:
                        img.screen.blit(img.white_bishop, (pos_x, pos_y))
                elif isinstance(board[i][j], King):
                    if board[i][j].color:
                        img.screen.blit(img.black_king, (pos_x, pos_y))
                    else:
                        img.screen.blit(img.white_king, (pos_x, pos_y))
                elif isinstance(board[i][j], Knight):
                    if board[i][j].color:
                        img.screen.blit(img.black_knight, (pos_x, pos_y))
                    else:
                        img.screen.blit(img.white_knight, (pos_x, pos_y))
                elif isinstance(board[i][j], Pawn):
                    if board[i][j].color:
                        img.screen.blit(img.black_pawn, (pos_x, pos_y))
                    else:
                        img.screen.blit(img.white_pawn, (pos_x, pos_y))
                elif isinstance(board[i][j], Queen):
                    if board[i][j].color:
                        img.screen.blit(img.black_queen, (pos_x, pos_y))
                    else:
                        img.screen.blit(img.white_queen, (pos_x, pos_y))
                elif isinstance(board[i][j], Rook):
                    if board[i][j].color:
                        img.screen.blit(img.black_rook, (pos_x, pos_y))
                    else:
                        img.screen.blit(img.white_rook, (pos_x, pos_y))

    
    @staticmethod
    def draw_possible_squares(board, possible_squares, selected):
        green_square = pygame.Surface(
            (const.width // 8, const.height // 8), pygame.SRCALPHA
        )
        red_square = pygame.Surface((const.width // 8, const.height // 8), pygame.SRCALPHA)
        green_square.fill((0, 255, 0, 35))
        red_square.fill((255, 0, 0, 35))
        img.screen.blit(
            green_square, (const.height // 8 * selected[1], const.width // 8 * selected[0])
        )
        for i in range(0, len(possible_squares), 2):
            if board[possible_squares[i]][possible_squares[i + 1]] != None:
                img.screen.blit(
                    red_square,
                    (
                        const.height // 8 * possible_squares[i + 1],
                        const.width // 8 * possible_squares[i],
                    ),
                )
            else:
                img.screen.blit(
                    green_square,
                    (
                        const.height // 8 * possible_squares[i + 1],
                        const.width // 8 * possible_squares[i],
                    ),
                )
