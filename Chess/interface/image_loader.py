import pygame
from configurations.configs import Config as const


class Loader:

    screen = pygame.display.set_mode((const.width, const.height))
    black_square = pygame.transform.scale((pygame.image.load(
        'img/square_gray_dark.png')), (const.width//8, const.height//8))
    white_square = pygame.transform.scale((pygame.image.load(
        'img/square_gray_light.png')), (const.width//8, const.height//8))
    brown_square = pygame.transform.scale((pygame.image.load(
        'img/square_brown_light.png')), (const.width//8, const.height//8))

    # White pieces load
    white_bishop = pygame.transform.scale((pygame.image.load(
        'img/white_bishop.png')), (const.width//const.piece_size, const.height//const.piece_size))
    white_king = pygame.transform.scale((pygame.image.load(
        'img/white_king.png')), (const.width//const.piece_size, const.height//const.piece_size))
    white_knight = pygame.transform.scale((pygame.image.load(
        'img/white_knight.png')), (const.width//const.piece_size, const.height//const.piece_size))
    white_pawn = pygame.transform.scale((pygame.image.load(
        'img/white_pawn.png')), (const.width//const.piece_size, const.height//const.piece_size))
    white_queen = pygame.transform.scale((pygame.image.load(
        'img/white_queen.png')), (const.width//const.piece_size, const.height//const.piece_size))
    white_rook = pygame.transform.scale((pygame.image.load(
        'img/white_rook.png')), (const.width//const.piece_size, const.height//const.piece_size))

    # Black pieces load
    black_bishop = pygame.transform.scale((pygame.image.load(
        'img/black_bishop.png')), (const.width//const.piece_size, const.height//const.piece_size))
    black_king = pygame.transform.scale((pygame.image.load(
        'img/black_king.png')), (const.width//const.piece_size, const.height//const.piece_size))
    black_knight = pygame.transform.scale((pygame.image.load(
        'img/black_knight.png')), (const.width//const.piece_size, const.height//const.piece_size))
    black_pawn = pygame.transform.scale((pygame.image.load(
        'img/black_pawn.png')), (const.width//const.piece_size, const.height//const.piece_size))
    black_queen = pygame.transform.scale((pygame.image.load(
        'img/black_queen.png')), (const.width//const.piece_size, const.height//const.piece_size))
    black_rook = pygame.transform.scale((pygame.image.load(
        'img/black_rook.png')), (const.width//const.piece_size, const.height//const.piece_size))
