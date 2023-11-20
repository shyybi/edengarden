def start_game():
   
    import pygame

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    ammo_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player_speed = 1.00000 
    ammo_speed = 10

    while running:
        # Traitement des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("#467532")
        pygame.draw.circle(screen, "red", player_pos, 40)

        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[2]:
            mouse_pos = pygame.mouse.get_pos()

            direction = mouse_pos - player_pos
            direction.normalize()

            player_pos += direction * player_speed * dt
            
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            direction = mouse_pos - player_pos
            direction.normalize()
            ammo_pos += direction * ammo_speed * dt


        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()
