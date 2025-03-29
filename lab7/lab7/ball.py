import pygame

pygame.init()

WIDTH, HEIGHT = 500,500
RADIUS =25
CLR =(255,0, 0)
BACKCLR =(255, 255, 255)
STEP =20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ball")

x, y = WIDTH// 2, HEIGHT// 2
run=True
while run:
    screen.fill(BACKCLR)
    pygame.draw.circle(screen,CLR, (x,y),RADIUS)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP and y -RADIUS- STEP >=0:
                y -=STEP
            elif event.key == pygame.K_DOWN and y + RADIUS + STEP<=HEIGHT:
                y += STEP
            elif event.key == pygame.K_LEFT and x -RADIUS -STEP>= 0:
                x -= STEP
            elif event.key == pygame.K_RIGHT and x +RADIUS+STEP <=WIDTH:
                x +=STEP

pygame.quit()
