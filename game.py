def start_game():
    import pygame
    import time

    pygame.init()
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    current_sprite_index = 0

    anim_top = [
        pygame.image.load("character/top/top2.png"),
        pygame.image.load("character/top/top3.png")
    ]
    anim_bot = [
        pygame.image.load("character/bot/bot1.png"),
        pygame.image.load("character/bot/bot2.png")
    ]
    anim_right = [
        pygame.image.load("character/right/right1.png"),
        pygame.image.load("character/right/right2.png")
    ]
    anim_left = [
        pygame.image.load("character/left/left1.png"),
        pygame.image.load("character/left/left2.png")
        
    ]
    sprite_size = (150, 150)  
    player_sprite = pygame.transform.scale(anim_top[current_sprite_index], sprite_size)

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)  
    player_speed = 250
    last_sprite_change_position = player_pos.y
    last_sprite_change_time = time.time()

    last_sprite_change_position_x = player_pos.x
    last_sprite_change_time_x = time.time()



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("#467532")
        
        sprite_rect = player_sprite.get_rect(center=player_pos)
        screen.blit(player_sprite, sprite_rect)
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            player_pos.y -= player_speed * dt

            if abs(player_pos.y - last_sprite_change_position) >= 50:
                last_sprite_change_position = player_pos.y
                current_sprite_index = (current_sprite_index + 1) % len(anim_top)
                player_sprite = pygame.transform.scale(anim_top[current_sprite_index], sprite_size)

            if time.time() - last_sprite_change_time >= 1.0:
                last_sprite_change_time = time.time()
                current_sprite_index = (current_sprite_index + 1) % len(anim_top)
                player_sprite = pygame.transform.scale(anim_top[current_sprite_index], sprite_size)

        if keys[pygame.K_s]:
            player_pos.y += player_speed * dt

            if abs(player_pos.y - last_sprite_change_position) >= 50:
                last_sprite_change_position = player_pos.y
                current_sprite_index = (current_sprite_index + 1) % len(anim_bot)
                player_sprite = pygame.transform.scale(anim_bot[current_sprite_index], sprite_size)

            if time.time() - last_sprite_change_time >= 1.0:
                last_sprite_change_time = time.time()
                current_sprite_index = (current_sprite_index + 1) % len(anim_bot)
                player_sprite = pygame.transform.scale(anim_bot[current_sprite_index], sprite_size)

        if keys[pygame.K_q]:   
            player_pos.x -= player_speed * dt

            if abs(player_pos.x - last_sprite_change_position_x) >= 50:
                last_sprite_change_position_x = player_pos.x
                current_sprite_index = (current_sprite_index + 1) % len(anim_left)
                player_sprite = pygame.transform.scale(anim_left[current_sprite_index], sprite_size)

            if time.time() - last_sprite_change_time_x >= 1.0:
                last_sprite_change_time_x = time.time()
                current_sprite_index = (current_sprite_index + 1) % len(anim_left)
                player_sprite = pygame.transform.scale(anim_left[current_sprite_index], sprite_size)

        if keys[pygame.K_d]:
            player_pos.x += player_speed * dt

            if abs(player_pos.x - last_sprite_change_position_x) >= 50:
                last_sprite_change_position_x = player_pos.x
                current_sprite_index = (current_sprite_index + 1) % len(anim_right)
                player_sprite = pygame.transform.scale(anim_right[current_sprite_index], sprite_size)

            if time.time() - last_sprite_change_time_x >= 1.0:
                last_sprite_change_time_x = time.time()
                current_sprite_index = (current_sprite_index + 1) % len(anim_right)
                player_sprite = pygame.transform.scale(anim_right[current_sprite_index], sprite_size)



        camera_x = player_pos.x - screen_width // 2
        camera_y = player_pos.y - screen_width // 2
 


        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()