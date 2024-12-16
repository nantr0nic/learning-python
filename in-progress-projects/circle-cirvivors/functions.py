import pygame

def check_events(player, bullets, win):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moving_x = -1
            elif event.key == pygame.K_RIGHT:
                player.moving_x = 1
            elif event.key == pygame.K_UP:
                player.moving_y = -1
            elif event.key == pygame.K_DOWN:
                player.moving_y = 1
            elif event.key == pygame.K_SPACE:
                pass
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving_x = 0
            elif event.key == pygame.K_RIGHT:
                player.moving_x = 0
            elif event.key == pygame.K_UP:
                player.moving_y = 0
            elif event.key == pygame.K_DOWN:
                player.moving_y = 0    