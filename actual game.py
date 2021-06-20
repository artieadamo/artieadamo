import pygame
import time

pygame.init()

screen_x = 500
screen_y = 500

rectangle_width = 10
rectangle_height = 20
rectangle_x = 10
rectangle_y = 10

white = (255,255,255)
black = (0, 0, 0)
red = (255, 0, 0)
running = True

vel = 5
isJump = False
jumpCount = 10

screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Game")

while running:
    pygame.time.delay(10) #rate of which the movement of the rectangle is delayed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and rectangle_x > vel: 
        rectangle_x -= vel

    if keys[pygame.K_RIGHT] and rectangle_x < screen_x - vel - rectangle_width:  
        rectangle_x += vel
        
    if not(isJump): 
        if keys[pygame.K_UP] and rectangle_y > vel:
            rectangle_y -= vel

        if keys[pygame.K_DOWN] and rectangle_y < screen_y - rectangle_height - vel:
            rectangle_y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            rectangle_y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
            
    screen.fill(black)
    pygame.draw.rect(screen, red, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))
    

    pygame.display.update()

pygame.quit()
