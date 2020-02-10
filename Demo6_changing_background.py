import pygame
x=pygame.init()
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
print(x)
gamewindow = pygame.display.set_mode((1000,600))
pygame.display.set_caption("My first game")

exit_game = False
game_over = False
Snake_x=45
Snake_y=55
Snake_size=10
fps=30
clock=pygame.time.clock()
#creating gane loop

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gamewindow.fill(white)
                pygame.display.update()
                print("You have pressed right arrow key")
            if event.key ==pygame.K_LEFT:
                gamewindow.fill(red)
                pygame.display.update()
                print("You have pressed left arrow key")
        print(event)
pygame.quit()
quit()