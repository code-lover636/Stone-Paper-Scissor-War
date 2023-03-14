import sys
from utils import *

pygame.init()

# screen
WIDTH, HEIGHT = 500, 500
pygame.display.set_icon(pygame.image.load('assets/scissor.png'))
pygame.display.set_caption("Stone Paper Scissors")
obj = { 
       "stone": pygame.image.load('assets/stone.png'),
       "paper": pygame.image.load('assets/paper.png'),
       "scissor": pygame.image.load('assets/scissor.png'),       
}
screen = pygame.display.set_mode((WIDTH, HEIGHT+30))

font = pygame.font.Font('freesansbold.ttf', 15)
game = Game(screen, obj, WIDTH, HEIGHT, 20, font)
sprite_move = game.wait_and_run(100)

# MAIN LOOP
while 1:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  print(pygame.mouse.get_pos())
        elif event.type == sprite_move:  
            game.move()
            game.collision()
    game.draw()
            
    