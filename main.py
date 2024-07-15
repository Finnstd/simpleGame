import pygame
from sys import exit

pygame.init()


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time = int(current_time / 100)
    font = pygame.font.Font(None, 60)
    text_score = font.render(f"Score: {current_time}", True, (120, 100, 90))
    text_score_rect = text_score.get_rect(topleft=(360, 10))
    screen.blit(text_score, text_score_rect)


display_size = width, height = (900, 360)
screen = pygame.display.set_mode(display_size)
title = pygame.display.set_caption("Roblex")
clock = pygame.time.Clock()
Game_active = True
start_time = 0
#SURFACE
surface_game = pygame.image.load("bg.png").convert()

#CHARACTER
character = pygame.image.load("acc.png").convert_alpha()
char_x_pos, char_y_pos = 30, 190
character_rect = character.get_rect(topleft=(char_x_pos, char_y_pos))
character_gravity = 0

#SNAIL
snail = pygame.image.load("snail.png").convert_alpha()
snail_x_pos, snail_y_pos = 705, 227
snail_rect = snail.get_rect(topleft=(snail_x_pos, snail_y_pos))
#
# TEXT GAME
font = pygame.font.Font(None, 60)
text = font.render("ROBLOX", True, "#0CA3A0")
text_rect = text.get_rect(topleft=(360, 10))

#TIME


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if Game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if character_rect.y == 190:
                        character_gravity = -18

            if event.type == pygame.MOUSEBUTTONDOWN:
                if character_rect.collidepoint(event.pos):
                    character_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                Game_active = True
                snail_rect.x = 705
                start_time = pygame.time.get_ticks()

    if Game_active:
        # SCREEN
        screen.blit(surface_game, (0, 0))
        screen.blit(character, character_rect)
        pygame.draw.rect(screen, "pink", text_rect, 20, 10)
        pygame.draw.rect(screen, "pink", text_rect)
        display_score()

        # screen.blit(text, text_rect)

        # Character
        character_gravity += 1
        character_rect.y += character_gravity
        if character_rect.y >= 190: character_rect.y = 190
        snail_rect.left -= 4
        if snail_rect.left <= -100:
            snail_rect.left = 1000
        screen.blit(snail, snail_rect)

        # collision
        if character_rect.colliderect(snail_rect):
            Game_active = False
    else:
        screen.fill("red")

    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()
