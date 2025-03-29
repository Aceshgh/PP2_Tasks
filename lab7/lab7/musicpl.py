import pygame
import os

print("ARROW RIGHT TO NEXT, ARROW LEFT TO PREVIOUS, ARROW DOWN TO PLAY/STOP")
pygame.init()
pygame.mixer.init()
screen =pygame.display.set_mode((400, 300))
pygame.display.set_caption("music player")

playlist =["song1.mp3", "song2.mp3"]
currsong =0

def play(indexsong):
    pygame.mixer.music.load(playlist[indexsong])
    pygame.mixer.music.play()

play(currsong)
run=True
while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run =False
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN: 
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key ==pygame.K_UP: 
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT: 
                currsong =(currsong + 1) %len(playlist)
                play(currsong)
            elif event.key == pygame.K_LEFT: 
                currsong= (currsong - 1) %len(playlist)
                play(currsong)

pygame.quit()
