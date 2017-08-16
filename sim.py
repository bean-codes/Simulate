import pygame
from pygame.locals import *
from shapes import Entity, RandEnt

# BLUE = (0, 0, 255)



# width, height = 300, 400
# screen = pygame.display.set_mode((width, height))

# background_color = (255, 255, 255)
# screen.fill(background_color)

# p = RandEnt()
# print(p.x)
# print(p.y)
# p.draw(screen)

# pygame.display.flip()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False


class Window:
    def __init__(self):
        self.width, self.height = 400, 300
        self.screen = pygame.display.set_mode((self.height, self.width))
        self.background_color = (255, 255, 255)
        


    def main(self): # main application loop
        running = True
        self.render()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # pygame.display.flip()


    def render(self): # does whatever at the moment
        self.screen.fill(self.background_color)
        num_particles = 10
        particle_list = []

        for i in range(num_particles):
            particle_list.append(RandEnt())
        
        for x in particle_list:
            x.draw(self.screen)
            
        pygame.display.flip()


if __name__ == '__main__':
    app = Window()
    app.main()