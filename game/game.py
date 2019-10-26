import pygame, sys

pygame.init()
size = width, height = 600, 400
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size)

speed = [1, 1]
ball = pygame.image.load('basketball.jpg')
ballrect = ball.get_rect()

fps = 300
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.update()

    fclock.tick(fps)

