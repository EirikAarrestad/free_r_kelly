import pygame
import random

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class SnakeGame:
    def __init__(self, width, height):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        # Adjusting initial snake position based on the game area size
        self.snake = [
            (width // 2, height // 2),
            (width // 2 - 10, height // 2),
            (width // 2 - 20, height // 2),
        ]
        self.direction = "RIGHT"

        # Adjusting initial food position based on the game area size
        self.food = self.create_food()

        self.score = 0

    def create_food(self):
        return (
            random.randrange(1, self.width // 10) * 10,
            random.randrange(1, self.height // 10) * 10,
        )

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

            for pos in self.snake:
                pygame.draw.rect(self.screen, GREEN, (pos[0], pos[1], 10, 10))

            pygame.draw.rect(self.screen, RED, (self.food[0], self.food[1], 10, 10))

            pygame.display.update()
            self.clock.tick(speed)

    def move_snake(self):
        head = self.snake[0]
        if self.direction == "UP":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + 10)
        elif self.direction == "LEFT":
            new_head = (head[0] - 10, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + 10, head[1])

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
    # UI for selecting game mode
    print("Select game mode:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    mode = input("Enter mode (1/2/3): ")

    if mode == "1":
        speed = 10
        width = 360
        height = 240
    elif mode == "2":
        speed = 10
        width = 720
        height = 480
    elif mode == "3":
        speed = 15
        width = 1080
        height = 720
    else:
        print("Invalid mode selected. Defaulting to medium.")
        speed = 10
        width = 720
        height = 480

    game = SnakeGame(width, height)
    game.run(speed)


if __name__ == "__main__":
    main()
