import math

import pygame

class DrawInfo:
    DARK=221, 221, 221
    BLACK=4, 28, 50
    GREEN=4, 41, 58
    BLUE=6, 70, 99
    WHITE=255,255,255
    CREME=236, 179, 101
    GREEN2=65, 125, 122
    BACHGROUND_COLOR=DARK
    SIDE_PAD=80
    TOP_PAD=120
    GRADIENT=[BLACK,GREEN,BLUE]
    FONT=pygame.font.SysFont('comicsans', 20)
    LARGE=pygame.font.SysFont('comicsans', 40)

    def __init__(self, width, height, lst):
        self.width=width
        self.height = height
        self.window=pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        self.block_width=round((self.width - self.SIDE_PAD)/len(lst))
        self.block_heigth=math.floor((self.height - self.TOP_PAD)/(self.max_val-self.min_val))
        self.start_x=self.SIDE_PAD//2




