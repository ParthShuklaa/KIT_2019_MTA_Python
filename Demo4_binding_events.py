import pygame
x=pygame.init()
print(x)
gamewindow = pygame.display.set_mode((1000,600))
pygame.display.set_caption("My first game")

exit_game = False
game_over = False

#creating gane loop

while not exit_game:
    for event in pygame.event.get():
        print(event)
pygame.quit()
quit()