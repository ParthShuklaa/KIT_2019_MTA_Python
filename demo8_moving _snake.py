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
Clock=pygame.time.Clock()
#creating gane loop

while not exit_game:
    for event in pygame.event.get():
        gamewindow.fill(white)
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Snake_x=Snake_x+10
            if event.key == pygame.K_LEFT:
                Snake_x = Snake_x - 10
            if event.key == pygame.K_DOWN:
                Snake_y = Snake_y + 10
            if event.key == pygame.K_UP:
                Snake_y = Snake_y - 10



        #drawing a snakjdj
        pygame.draw.rect(gamewindow,black,(Snake_x,Snake_y,Snake_size,Snake_size))
        pygame.draw.rect(gamewindow,red,(20,50,15,15))
        pygame.display.update()
        Clock.tick(fps)


pygame.quit()
quit()