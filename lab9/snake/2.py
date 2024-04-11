import pygame
import random
import time

# Global constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Main function
# Inside the main function
def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Initialize the snake
    snake = Snake()
    
    # Initialize the food
    foods = [Food() for _ in range(3)]  # Create multiple food instances
    for food in foods:
        food.randomize_position()
    
    # Initialize game variables
    score = 0
    level = 1
    speed = 5
    game_over = False
    
    # Main game loop
    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.change_direction(RIGHT)
        
        # Snake movement and collision detection
        snake.move()
        if snake.check_collision(SCREEN_WIDTH, SCREEN_HEIGHT):
            game_over = True
        
        # Food interaction
        for food in foods:
            if snake.head.position == food.position:
                snake.grow()
                score += 1
                food.randomize_position()
                food.reset_timer()
            elif food.is_expired():
                food.randomize_position()
                food.reset_timer()
                
        if score >= level * 3:  # Increase level every multiple of 3
            level += 1
            speed += 1  # Increase speed by 1
        
        # Update screen
        screen.fill(BLACK)
        snake.draw(screen)
        for food in foods:
            food.draw(screen)
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score) + " Level: " + str(level), True, WHITE)
        screen.blit(text, (10, 10))
        pygame.display.flip()
        clock.tick(speed)
# Snake class
class Snake:
    def __init__(self):
        self.head = Segment(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body = [self.head]
        self.direction = RIGHT
    
    def change_direction(self, direction):
        self.direction = direction
    
    def move(self):
        new_head = Segment(self.head.position[0] + self.direction[0] * BLOCK_SIZE,
                          self.head.position[1] + self.direction[1] * BLOCK_SIZE)
        self.body.insert(0, new_head)
        self.head = new_head
        self.body.pop()
    
    def grow(self):
        tail = self.body[-1]
        new_segment = Segment(tail.position[0], tail.position[1])
        self.body.append(new_segment)
    
    def draw(self, screen):
        for segment in self.body:
            segment.draw(screen)
    
    def check_collision(self, screen_width, screen_height):
        if (self.head.position[0] < 0 or self.head.position[0] >= screen_width
                or self.head.position[1] < 0 or self.head.position[1] >= screen_height):
            return True
        return False

# Segment class
class Segment:
    def __init__(self, x, y):
        self.position = (x, y)
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.creation_time = 0
        self.expiration_time = 5  # Food expires after 5 seconds
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                         random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
        self.creation_time = time.time()
    
    def is_expired(self):
        return time.time() - self.creation_time >= self.expiration_time

    def reset_timer(self):
       self.creation_time = time.time()

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

# Run the main function
if __name__ == "__main__":
    main()

