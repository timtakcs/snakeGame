import pygame
import time
import random

def draw_grid(width, height, block_size, screen):
    green = 0
    for i in range(0, width, block_size):
        for j in range(0, height, block_size):
            grid_rect_fill = pygame.Rect(i, j, block_size, block_size)
            pygame.draw.rect(screen, (0, green, 0), grid_rect_fill, 1)

def snake_mvmt(head, direction, block_size, length, screen): 
    for i in range(len(positionsx), len(positionsx) - length, -1):
        if len(positionsx) > length:
            body = pygame.Rect(positionsx[i - 1], positionsy[i - 1], block_size, block_size)
            pygame.draw.rect(screen, (0, 0, 255), body, 0)
            
    if direction == "up" and head.bottom - block_size > 0:
        head.top -= block_size
    if direction == "left" and head.right - block_size > 0:
        head.left -= block_size
    if direction == "down" and head.top + block_size < height:
        head.top += block_size
    if direction == "right" and head.left + block_size < width:
        head.left += block_size

def collision(head, apple):
    if head.colliderect(apple):
        return True

def collision_snake(length):
    for i in range(len(positionsx) - 2, len(positionsx) - length, -1):
        if positionsx[-1] == positionsx[i] and positionsy[-1] == positionsy[i]:
            return True

def game_over(screen, length):
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont('Pixeboy', 30)
    line1 = font.render("GAME OVER", True, (255, 255, 0))
    screen.blit(line1, (200, 250))
    line2 = font.render("Your Score Was: " + str(length), True, (255, 255, 0))
    screen.blit(line2, (200, 300))
    pygame.display.flip()

def main():
    pygame.init()
    
    clock = pygame.time.Clock()

    global height
    global width
    global positionsx
    global positionsy

    width = 600
    height = 600
    block_size = 60
    length = 1

    xpos = 2 * block_size
    ypos = 2 * block_size

    randomx = random.randint(1, width/block_size - 1)
    randomy = random.randint(1, height/block_size - 1)
    
    screen = pygame.display.set_mode((width, height))

    head = pygame.Rect(xpos, ypos, block_size, block_size)
    
    running = True
    gameover = False
    direction = "right"

    positionsx = []
    positionsy = []

    while running == True:
        if gameover == False:
            screen.fill((255, 255, 255))
            draw_grid(width, height, block_size, screen)
            pygame.draw.rect(screen, (0, 0, 255), head, 0)
            apple = pygame.Rect(randomx * block_size, randomy * block_size, block_size, block_size)
            pygame.draw.rect(screen, (255, 0, 0), apple, 0)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and direction != "down":
                        direction = "up"
                
                    if event.key == pygame.K_a and direction != "right":
                        direction = "left"
                
                    if event.key == pygame.K_s and direction != "up":
                        direction = "down"
                
                    if event.key == pygame.K_d and direction != "left":
                        direction = "right"
                
                if event.type == pygame.QUIT:
                    running = False
            
            positionsx.append(head.left)
            positionsy.append(head.top)
            
            snake_mvmt(head, direction, block_size, length, screen)

            if collision_snake(length) == True:
                gameover = True

            if collision(head, apple) == True:
                    randomx = random.randint(1, width/block_size -1)
                    randomy = random.randint(1, height/block_size -1)
                    length += 1
        
            time.sleep(0.1) 
            pygame.display.update()
            clock.tick(60)

        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        length = 1

                        gameover = False

                if event.type == pygame.QUIT:
                    running = False
                    
            game_over(screen, length)
            

if __name__ == "__main__":
    main()

