import pygame
import random

# Defingerer farger som skal bli brukt i spillet
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class SnakeGame:
    def __init__(self, width, height, pixel_size):
        pygame.init()

        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake spill")

        self.clock = pygame.time.Clock()

        # Justering av hvor slangen spawner etter hvor stort vinduet er
        self.snake = [
            (width // 2, height // 2),
            (width // 2 - pixel_size, height // 2),
            (width // 2 - 2 * pixel_size, height // 2),
        ]

        # Velger startsretning til høyre
        self.direction = "RIGHT"

        self.food = self.create_food()

        self.score = 0

    # Funksjon som lager mat og setter den inn i spillet
    def create_food(self):
        while True:
            food_pos = (
                random.randrange(1, self.width // self.pixel_size) * self.pixel_size,
                random.randrange(1, self.height // self.pixel_size) * self.pixel_size,
            )
            # Sjekker om maten vil være innenfor slangens kropp
            if food_pos not in self.snake:
                return food_pos

    # Game over skjerm som viser score osv.
    def game_over(self):
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"Game Over! Score: {self.score}", True, RED)
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        quit()

    def run(self, speed):
        # Løkke for at slangen skal kunne bevege seg og ikke la den gå to omvendte retninger samtidig
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != "DOWN":
                        self.direction = "UP"
                    elif event.key == pygame.K_DOWN and self.direction != "UP":
                        self.direction = "DOWN"
                    elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                        self.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                        self.direction = "RIGHT"

            self.move_snake()

            self.screen.fill((0, 0, 0))

            # Laster inn slangens kropp i spillet
            for pos in self.snake:
                pygame.draw.rect(
                    self.screen,
                    GREEN,
                    (pos[0], pos[1], self.pixel_size, self.pixel_size),
                )

            # Tegner "maten" i spillet
            pygame.draw.rect(
                self.screen,
                RED,
                (self.food[0], self.food[1], self.pixel_size, self.pixel_size),
            )

            pygame.display.update()
            self.clock.tick(speed)

    # Funksjon for bevegelse av slangen, hvor ny blokk skal legges til og ulike døds-scenarier
    def move_snake(self):
        head = self.snake[0]
        if self.direction == "UP":
            new_head = (head[0], head[1] - self.pixel_size)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + self.pixel_size)
        elif self.direction == "LEFT":
            new_head = (head[0] - self.pixel_size, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + self.pixel_size, head[1])

        # slange død scenarier
        if (
            new_head[0] < 0
            or new_head[0] >= self.width
            or new_head[1] < 0
            or new_head[1] >= self.height
        ):
            self.game_over()

        if new_head in self.snake:
            self.game_over()

        self.snake.insert(0, new_head)

        if self.snake[0] == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()


def main():
    # GUI slik at brukereren kan velge vanskelighetsgrad
    print("Select game mode:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    mode = input("Enter mode (1/2/3): ")

    if mode == "1":
        speed = 5
        width = 360
        height = 240
        pixel_size = 20
    elif mode == "2":
        speed = 7.5
        width = 540
        height = 360
        pixel_size = 30

    elif mode == "3":
        speed = 10
        width = 720
        height = 540
        pixel_size = 30

    else:
        print("Invalid mode selected. Defaulting to medium.")
        speed = 7.5
        width = 540
        height = 360
        pixel_size = 30

    game = SnakeGame(width, height, pixel_size)
    game.run(speed)


if __name__ == "__main__":
    main()
