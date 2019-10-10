import pygame


class Const():
    # Numeric constants
    width = 800
    height = 800
    bishop = 1
    king = 2
    knight = 3
    pawn = 4
    queen = 5
    rook = 6
    none = 7
    piece_size = 10
    center_width = width//8//2 - width//piece_size//2
    center_height = height//8//2 - height//piece_size//2

    # Image load

    # Squares load
    screen = pygame.display.set_mode((width, height))
    black_square = pygame.transform.scale((pygame.image.load(
        'img/square_gray_dark.png')), (width//8, height//8))
    white_square = pygame.transform.scale((pygame.image.load(
        'img/square_gray_light.png')), (width//8, height//8))

    # White pieces load
    white_bishop = pygame.transform.scale((pygame.image.load(
        'img/white_bishop.png')), (width//piece_size, height//piece_size))
    white_king = pygame.transform.scale((pygame.image.load(
        'img/white_king.png')), (width//piece_size, height//piece_size))
    white_knight = pygame.transform.scale((pygame.image.load(
        'img/white_knight.png')), (width//piece_size, height//piece_size))
    white_pawn = pygame.transform.scale((pygame.image.load(
        'img/white_pawn.png')), (width//piece_size, height//piece_size))
    white_queen = pygame.transform.scale((pygame.image.load(
        'img/white_queen.png')), (width//piece_size, height//piece_size))
    white_rook = pygame.transform.scale((pygame.image.load(
        'img/white_rook.png')), (width//piece_size, height//piece_size))

    # Black pieces load
    black_bishop = pygame.transform.scale((pygame.image.load(
        'img/black_bishop.png')), (width//piece_size, height//piece_size))
    black_king = pygame.transform.scale((pygame.image.load(
        'img/black_king.png')), (width//piece_size, height//piece_size))
    black_knight = pygame.transform.scale((pygame.image.load(
        'img/black_knight.png')), (width//piece_size, height//piece_size))
    black_pawn = pygame.transform.scale((pygame.image.load(
        'img/black_pawn.png')), (width//piece_size, height//piece_size))
    black_queen = pygame.transform.scale((pygame.image.load(
        'img/black_queen.png')), (width//piece_size, height//piece_size))
    black_rook = pygame.transform.scale((pygame.image.load(
        'img/black_rook.png')), (width//piece_size, height//piece_size))

    # Initial board
    matrix = \
    [(rook, True), (knight, True), (bishop, True), (queen, True), (king, True), (bishop, True), (knight, True), (rook, True)], \
    [(pawn, True), (pawn, True), (pawn, True), (pawn, True), (pawn, True), (pawn, True), (pawn, True), (pawn, True)], \
    [(none, none), (none, none), (none, none), (none, none), (none, none), (none, none), (none, none), (none, none)], \
    [(none, none), (none, none), (none, none), (none, none), (none, none), (none, none), (none, none), (none, none)], \
    [(none, none), (none, none), (none, none), (none, none), (none, none), (none, none), (none, none), (none, none)], \
    [(none, none), (none, none), (none, none), (none, none), (none, none), (none, none), (none, none), (none, none)], \
    [(pawn, False), (pawn, False), (pawn, False), (pawn, False), (pawn, False), (pawn, False), (pawn, False), (pawn, False)], \
    [(rook, False), (knight, False), (bishop, False), (queen, False), (king, False), (bishop, False), (knight, False), (rook, False)]
