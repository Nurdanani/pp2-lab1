import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
bg_image = pygame.image.load('lab2/lab7/clock/main.png')
sec_img = pygame.image.load('lab2/lab7/clock/left-hand.png')
min_img = pygame.image.load('lab2/lab7/clock/right-hand.png')
rect = bg_image.get_rect(center=(400, 400))

while not done:
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now().time()

    sec_angle = -(time.second*6)+90
    nsec_img = pygame.transform.rotate(sec_img, sec_angle)
    sec_rect = nsec_img.get_rect(center=rect.center)
    screen.blit(nsec_img, sec_rect.topleft)

    min_angle = -((time.minute +1)* 6)+90
    nmin_img = pygame.transform.rotate(min_img, min_angle)
    min_rect = nmin_img.get_rect(center=rect.center)
    screen.blit(nmin_img, min_rect.topleft)

    pygame.display.flip()