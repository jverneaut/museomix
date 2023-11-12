import vlc
import pygame
from pygame.locals import KEYDOWN, K_LEFT, K_DOWN

instance = vlc.Instance('--no-xlib --quiet')
player = instance.media_list_player_new()

media_list = []

media_list.append('video-1.mp4')
media_list.append('video-2.mp4')
media_list.append('video-3.mp4')
media_list.append('video-4.mp4')

player.set_media_list(instance.media_list_new(media_list))


pygame.init()

# Set up the display (you can skip this if you don't need a window)
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Arrow Key Detection")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                print("Left arrow key pressed")
            if event.key == K_DOWN:
                print("Down arrow key pressed")

pygame.quit()
