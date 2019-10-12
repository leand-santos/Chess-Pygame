import pygame
from Pieces import *

class Const:
    # Numeric constants
    width = 650
    height = 650
    bishop = 1
    king = 2
    knight = 3
    pawn = 4
    queen = 5
    rook = 6

    black = True
    white = False
    piece_size = 10
    center_width = width//8//2 - width//piece_size//2
    center_height = height//8//2 - height//piece_size//2

    # Initial board
    matrix = \
    [Rook(black), Knight(black), Bishop(black), Queen(black), King(black), Bishop(black), Knight(black), Rook(black)], \
    [Pawn(black), Pawn(black), Pawn(black), Pawn(black), Pawn(black), Pawn(black), Pawn(black), Pawn(black)], \
    [None, None, None, Pawn(white), None, None, None, None], \
    [None, None, None, None, None, None, None, None], \
    [None, None, None, None, None, None, None, None], \
    [None, None, None, None, None, None, None, None], \
    [Pawn(white), Pawn(white), Pawn(white), Pawn(white), Pawn(white), Pawn(white), Pawn(white), Pawn(white)], \
    [Rook(white), Knight(white), Bishop(white), Queen(white), King(white), Bishop(white), Knight(white), Rook(white)]

class Image:
    # Image load

    # Squares load
    screen = pygame.display.set_mode((Const.width, Const.height))
    black_square = pygame.transform.scale((pygame.image.load(
        'img/square_gray_dark.png')), (Const.width//8, Const.height//8))
    white_square = pygame.transform.scale((pygame.image.load(
        'img/square_gray_light.png')), (Const.width//8, Const.height//8))
    brown_square = pygame.transform.scale((pygame.image.load(
        'img/square_brown_light.png')), (Const.width//8, Const.height//8))

    # White pieces load
    white_bishop = pygame.transform.scale((pygame.image.load(
        'img/white_bishop.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
    white_king = pygame.transform.scale((pygame.image.load(
        'img/white_king.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
    white_knight = pygame.transform.scale((pygame.image.load(
        'img/white_knight.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
    white_pawn = pygame.transform.scale((pygame.image.load(
        'img/white_pawn.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
    white_queen = pygame.transform.scale((pygame.image.load(
        'img/white_queen.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
    white_rook = pygame.transform.scale((pygame.image.load(
        'img/white_rook.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))

    # Black pieces load
    black_bishop = pygame.transform.scale((pygame.image.load(
        'img/black_bishop.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
    black_king = pygame.transform.scale((pygame.image.load(
        'img/black_king.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
    black_knight = pygame.transform.scale((pygame.image.load(
        'img/black_knight.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
    black_pawn = pygame.transform.scale((pygame.image.load(
        'img/black_pawn.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
    black_queen = pygame.transform.scale((pygame.image.load(
        'img/black_queen.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
    black_rook = pygame.transform.scale((pygame.image.load(
        'img/black_rook.png')), (Const.width//Const.piece_size, Const.height//Const.piece_size))
