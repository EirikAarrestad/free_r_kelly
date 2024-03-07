import pygame
import random

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class SnakeGame:
    def __init__(self, width=720, height=480):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.snake = [(100, 50), (90, 50), (80, 50)]
        self.direction = "RIGHT"

        self.food = self.create_food()

        self.score = 0

    def create_food(self):
        return (
            random.randrange(1, self.width // 10) * 10,
            random.randrange(1, self.height // 10) * 10,
        )

    def run(self):
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
            self.clock.tick(15)

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

        self.snake.insert(0, new_head)

        if self.snake[0] == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
