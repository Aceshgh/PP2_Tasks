import pygame
import datetime

pygame.init()
W = 800
H = 800
screen =pygame.display.set_mode((W, H))
pygame.display.set_caption("Clock")
clock =pygame.time.Clock()
FPS =50
clockface = pygame.image.load("clock.png")
clockface = pygame.transform.scale(clockface, (600, 600))
hands ={
    "minute": pygame.transform.scale(pygame.image.load("min_hand.png"), (600, 900)), 
    "second": pygame.transform.scale(pygame.image.load("sec_hand.png"), (50, 500)), 
}

run =True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    now =datetime.datetime.now()
    minute = now.minute
    second = now.second

    angles = {
        "minute": -minute * 6,
        "second": -second * 6,
    }
    screen.fill((255, 255, 255))
    screen.blit(clockface, (100, 100))
    for name, img in hands.items():
        rotated = pygame.transform.rotate(img, angles[name])
        rect = rotated.get_rect(center=(W // 2, H // 2))
        screen.blit(rotated, rect.topleft)

    pygame.draw.circle(screen, (0, 0, 0), (W // 2, H // 2), 10)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()