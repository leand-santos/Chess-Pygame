import pygame
from json import (
    load,
    dump
)


class Config:
    with open('./configurations/settings.JSON') as file:
        settings = load(file)
    width = settings['width']
    height = settings['height']

    black = settings['black']
    white = settings['white']
    initial_turn = white

    piece_size = settings['piece_size']
    center_width = width//8//2 - width//piece_size//2
    center_height = height//8//2 - height//piece_size//2
    # def redefine(self, width):
    #     with open('./configurations/settings.JSON') as file:
    #         settings = load(file)
    #     settings['width'] = width
    #     with open('./configurations/settings.JSON', 'w') as update:
    #         dump(settings, update)
    # def printJSON(self):
    #     with open('./configurations/settings.JSON', 'r') as file:
    #         settings = load(file)
    #         print(settings['width'])
