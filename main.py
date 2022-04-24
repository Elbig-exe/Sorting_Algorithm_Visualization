import pygame
import random

from pygame import mixer

pygame.init()
mixer.init()
from DrawInfo import DrawInfo

def draw(draw_info,algo_name,asc):
    draw_info.window.fill(draw_info.BACHGROUND_COLOR)
    draw_list(draw_info)
    title = draw_info.LARGE.render(f"{algo_name}-{'Ascending' if asc else 'Descending'}", 1, draw_info.GREEN2)
    draw_info.window.blit(title, (20, 10))
    controls=draw_info.FONT.render("-R: Reset | -SPACE: Start Sorting | -A: Ascending | -D: Descending",1,draw_info.BLACK)
    draw_info.window.blit(controls,(20,60))
    controls = draw_info.FONT.render("-I: Reset | -B: Bubble sorting", 1,draw_info.BLACK)
    draw_info.window.blit(controls, (20, 85))
    pygame.display.update()
def draw_list(draw_info,color_position={},clear_bg=False):
    lst = draw_info.lst
    if clear_bg:
        clear_rect= (draw_info.SIDE_PAD//2, draw_info.TOP_PAD,
                        draw_info.width - draw_info.SIDE_PAD , draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACHGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x= draw_info.start_x + i * draw_info.block_width
        y= draw_info.height-(val - draw_info.min_val) * draw_info.block_heigth
        color=draw_info.GRADIENT[i % 3]
        if i in color_position:
            color=color_position[i]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
    if clear_bg:
        pygame.display.update()



def bubble_sort(draw_info, ascending=True):

    lst = draw_info.lst
    for i in range(len(lst) - 1):
        mixer.music.load("sound/loadd.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info,{j:draw_info.CREME,j+1:draw_info.GREEN2},True)
                yield True

    return lst

def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val=random.randint(min_val, max_val)
        lst.append(val)
    return lst
def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(1, len(lst)):
        current = lst[i]
        mixer.music.load("sound/loadd.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending
            if not ascending_sort and not descending_sort:
                break
            lst[i] = lst[i - 1]
            i = i - 1
            lst[i]=current
            draw_list(draw_info, {i-1 : draw_info.CREME, i : draw_info.GREEN2},True)
            yield True
    return lst




def main():
    run = True
    clock = pygame.time.Clock()
    ls=generate_starting_list(80,0,160)
    dis_info= DrawInfo(800,700,ls)
    sorting=False
    asc=True
    sorting_algorithm=bubble_sort
    sorting_algo_name="Bubble Sort"
    sorting_algorithm_generator= None
    while run:
        clock.tick(60)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                mixer.music.load("sound/success-1-6297.mp3")
                mixer.music.set_volume(0.4)
                mixer.music.play()
                sorting = False
        else:
            draw(dis_info,sorting_algo_name,asc)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                ls = generate_starting_list(80, 0, 160)
                dis_info.set_list(ls)
                sorting=False
            elif event.key==pygame.K_SPACE and sorting==False:
                sorting = True
                sorting_algorithm_generator=sorting_algorithm(dis_info, asc)

            elif event.key==pygame.K_a and sorting==False:
                asc = True
            elif event.key==pygame.K_d and sorting==False:
                asc = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key== pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"



    pygame.quit()
if __name__ =="__main__":
    main()
