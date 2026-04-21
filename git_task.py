import random
import pygame

# Inițializare pygame
pygame.init()

# Constante pentru fereastră și grid
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_SIZE = 10
CELL_SIZE = 50
REGENERATE_INTERVAL = 5000  # 5000 ms = 5 secunde


def generate_color_grid():
    """
    Generează o matrice 10x10 cu culori random.
    Fiecare celulă conține un tuplu RGB.
    """
    return [
        [
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]


def draw_grid(screen, color_grid):
    """
    Desenează grid-ul de culori pe ecran.
    """
    screen.fill((0, 0, 0))

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(
                screen,
                color_grid[row][col],
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    pygame.display.flip()


def main():
    """
    Rulează aplicația principală.
    Grid-ul se regenerează automat la fiecare 5 secunde.
    """
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Procedural Color Grid")

    color_grid = generate_color_grid()
    running = True

    last_update_time = pygame.time.get_ticks()

    while running:
        current_time = pygame.time.get_ticks()

        # Regenerează grid-ul o dată la 5 secunde
        if current_time - last_update_time >= REGENERATE_INTERVAL:
            color_grid = generate_color_grid()
            last_update_time = current_time

        draw_grid(screen, color_grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()