import os
import sys
import pygame
import numpy as np

from rope import rope

WINDOW_SIZE = (1000, 500)
ANCHOR_POINT = [WINDOW_SIZE[0]/2, 0]
BACKGROUND_COLOR = (1, 11, 19)
RUN = True
FPS = 30
LINE_COLOR = (255, 255, 255)
MASS = 10
MASS_COLOR = (179, 25, 66)

def main():
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED']='1'
    window = pygame.display.set_mode(WINDOW_SIZE)
    window.fill(BACKGROUND_COLOR)
    pygame.display.update()
    pygame.display.set_caption('Compound Pendulum')
    # pygame.display.update()
    clock = pygame.time.Clock()
    rope1 = rope(length=200, start=ANCHOR_POINT)
    while RUN:
        clock.tick(FPS)
        window.fill(BACKGROUND_COLOR)
        # update thetas
        swing_factor = 0.1
        new_theta = rope1.theta + swing_factor
        rope1.theta = new_theta
        # update start
        rope1.start = ANCHOR_POINT
        # update end
        rope1.swing()
        #draw lines
        pygame.draw.line(surface=window, color=LINE_COLOR, start_pos=rope1.start, end_pos=rope1.end, width=rope1.width)
        # pygame.draw.line(surface=window, color=MASS_COLOR, start_pos=(250,0), end_pos=(250,100), width=2) # The horizontal
        pygame.draw.circle(surface=window,  color=MASS_COLOR, center=rope1.end, radius=MASS)
        # draw masses at ends
        # Update graphics
        pygame.display.update()
        # check quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    sys.exit()

if __name__ == '__main__':
    main()