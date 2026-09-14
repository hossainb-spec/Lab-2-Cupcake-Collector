import pygame
import asyncio

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cupcake Collector by Barack Hossain")
clock = pygame.time.Clock()

player_x = 50
player_y = 300

player_dy = 0
gravity = 0.5
jump_speed = -10
on_ground = True

platforms = [
    pygame.Rect(0, 350, 600, 50),
    pygame.Rect(100, 270, 150, 20),
    pygame.Rect(350, 220, 150, 20)
]

cupcakes = [
    pygame.Rect(150, 230, 30, 30),
    pygame.Rect(400, 180, 30, 30),
    pygame.Rect(520, 310, 30, 30),
    pygame.Rect(250, 240, 30, 30),
    pygame.Rect(450, 190, 30, 30),
    pygame.Rect(80, 310, 30, 30)
]

score = 0

font = pygame.font.Font(None, 36)


async def main():

    global player_x
    global player_y
    global player_dy
    global on_ground
    global score

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player_x -= 3

        if keys[pygame.K_d]:
            player_x += 3

        if keys[pygame.K_w] and on_ground:
            player_dy = jump_speed
            on_ground = False

        player_dy += gravity
        player_y += player_dy

        player_rect = pygame.Rect(
            player_x,
            player_y,
            50,
            50
        )

        on_ground = False

        for platform in platforms:
            if player_rect.colliderect(platform) and player_dy >= 0:
                player_y = platform.top - 50
                player_dy = 0
                on_ground = True

        player_rect = pygame.Rect(
            player_x,
            player_y,
            50,
            50
        )

        for cupcake in cupcakes[:]:
            if player_rect.colliderect(cupcake):
                cupcakes.remove(cupcake)
                score += 1

        screen.fill((20, 24, 40))

        for platform in platforms:
            pygame.draw.rect(
                screen,
                (100, 180, 100),
                platform
            )

        for cupcake in cupcakes:
            pygame.draw.circle(
                screen,
                (255, 150, 200),
                cupcake.center,
                10
            )

        pygame.draw.rect(
            screen,
            (100, 150, 255),
            player_rect
        )

        score_text = font.render(
            "Score: " + str(score),
            True,
            (255, 255, 255)
        )

        screen.blit(
            score_text,
            (10, 10)
        )

        pygame.display.flip()

        clock.tick(60)

        await asyncio.sleep(0)


asyncio.run(main())
pygame.quit()