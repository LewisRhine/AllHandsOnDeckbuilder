import sys, pygame

pygame.init()
pygame.display.set_caption('All Hands on Deck(builder)')

screem_size = 1280, 720
screen = pygame.display.set_mode(screem_size)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.update()
    clock.tick(60)
