import pygame
from random import randint

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
width = 320
height = 240
size = 10
timer = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
pygame.display.update()


def listener(event, speed_x, speed_y):
    if event.key == pygame.K_d and speed_x != -size:
        speed_y = 0
        speed_x = size
    elif event.key == pygame.K_w and speed_y != size:
        speed_y = -size
        speed_x = 0
    elif event.key == pygame.K_a and speed_x != size:
        speed_y = 0
        speed_x = -size
    elif event.key == pygame.K_s and speed_y != -size:
        speed_y = size
        speed_x = 0
    return speed_x, speed_y


def infinity_walls(pos_x, pos_y):
    if pos_x >= width:
        pos_x = -size
    elif pos_x <= -size:
        pos_x = width-size
    elif pos_y >= height:
        pos_y = -size
    elif pos_y <= -size:
        pos_y = height-size
    return pos_x, pos_y


def Snake(snake_XY):
    cont = 1
    for XY in snake_XY:
        if cont % 4 == 1 or cont % 4 == 2:
            pygame.draw.rect(screen, green, [XY[0], XY[1], size, size])
        else:
            pygame.draw.rect(screen, blue, [XY[0], XY[1], size, size])
        cont += 1


def Apple(apple_x, apple_y):
    pygame.draw.rect(screen, red, [apple_x, apple_y, size, size])


def Snake_Head(snake_XY, pos_x, pos_y):
    snake_head = []
    snake_head.append(pos_x)
    snake_head.append(pos_y)
    snake_XY.append(snake_head)
    if any(Bloco == snake_head for Bloco in snake_XY[:-2]):
        return False
    return True


def main():
    out = True
    pos_x = randint(0, (width-size)/10)*10
    pos_y = randint(0, (height-size)/10)*10

    apple_x = randint(0, (width-size)/10)*10
    apple_y = randint(0, (height-size)/10)*10

    snake_size = 2
    snake_XY = []
    speed_x = size
    speed_y = 0

    while out:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                out = False
            if event.type == pygame.KEYDOWN:
                speed_x, speed_y = listener(event, speed_x, speed_y)

        pos_x, pos_y = infinity_walls(pos_x+speed_x, pos_y+speed_y)
        screen.fill(black)

        if len(snake_XY) > snake_size:
            del snake_XY[0]
        if pos_x == apple_x and pos_y == apple_y:
            apple_x = randint(0, (width-size)/10)*10
            apple_y = randint(0, (height-size)/10)*10
            snake_size += 2
        Snake(snake_XY)
        Apple(apple_x, apple_y)

        end = Snake_Head(snake_XY, pos_x, pos_y)
        if not end:
            out = False
        pygame.display.update()
        timer.tick(15)


main()
pygame.quit()
