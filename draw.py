"""
Made by Mayedl10 on GitHub, Reddit
"""

import pygame

def draw_circle(win, x, y, radius = 1, colour = (255,255,255)):
    try:
        pygame.draw.circle(win, colour, (x, y), radius)
        return True
    except:
        return False
    
def draw_square(win, x, y, s = 1, colour = (255,255,255)):
    try:
        pygame.draw.rect(win, colour, (x, y, s, s))
        return True
    except:
        return False
    

example = """
def draw_window():
    win.fill(STD_BGCOL) # fills screen in gray, STD_BGCOL as global variable: (200,200,200)

    dr.draw_circle(win, 50, 100, 100, (100, 255, 200)) # draw example circle
    dr.draw_circle(win, 1000, 800, 500, (255,200,255)) # draw example circle
    dr.draw_circle(win, 450, 250, 50, (0,0,0))         # draw example circle

    dr.draw_square(win, 50, 100, 1, (255,200,50))    # example square (x, y, lenght, colour)

    pygame.display.update() # refresh screen"""