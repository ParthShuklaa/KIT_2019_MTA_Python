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
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")
            if event.key ==pygame.K_LEFT:
                print("You have pressed left arrow key")
        print(event)
pygame.quit()
quit()