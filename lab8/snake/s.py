import pygame
import random

# Глобальные константы
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20  # Размер блока (размер одного сегмента змеи)

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Инициализация змеи
    snake = Snake()
    
    # Инициализация еды
    food = Food()
    food.randomize_position()  # Случайная позиция еды
    
    # Счетчик очков
    score = 0
    
    # Уровень сложности (начальная скорость змеи)
    level = 1
    speed = 5
    
    # Флаг окончания игры
    game_over = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            # Управление змеёй с клавиатуры
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.change_direction(RIGHT)
        
        # Движение змеи
        snake.move()
        
        # Проверка столкновения змеи с границами экрана
        if snake.check_collision(SCREEN_WIDTH, SCREEN_HEIGHT):
            game_over = True
        
        # Проверка столкновения змеи с едой
        if snake.head.position == food.position:
            snake.grow()  # Увеличение длины змеи
            food.randomize_position()  # Случайная позиция еды
            score += 1
            
            # Увеличение уровня сложности после съедения определенного количества еды
            if score % 3 == 0:
                level += 1
                speed += 1
                snake.increase_speed(speed)
        
        screen.fill(BLACK)
        
        

        # Отрисовка змеи и еды
        snake.draw(screen)
        food.draw(screen)
        
        # Отображение текущего счета
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score) + " Level: " + str(level), True, WHITE)
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        
        clock.tick(speed)  # Установка скорости обновления экрана (скорости змеи)

class Snake:
    def __init__(self):
        self.head = Segment(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Начальная позиция головы змеи
        self.body = [self.head]  # Список сегментов змеи
        self.direction = RIGHT  # Начальное направление движения
    
    def change_direction(self, direction):
        self.direction = direction
    
    def move(self):
        # Двигаем голову в заданном направлении
        new_head = Segment(self.head.position[0] + self.direction[0] * BLOCK_SIZE,
                          self.head.position[1] + self.direction[1] * BLOCK_SIZE)
        # Добавляем новую голову в начало тела
        self.body.insert(0, new_head)
        self.head = new_head
        # Удаляем последний сегмент тела (хвост), чтобы змея казалась двигающейся
        self.body.pop()
    
    def grow(self):
        # Добавление нового сегмента к змее
        tail = self.body[-1]
        new_segment = Segment(tail.position[0], tail.position[1])
        self.body.append(new_segment)
    
    def draw(self, screen):
        for segment in self.body:
            segment.draw(screen)
    
    def check_collision(self, screen_width, screen_height):
        # Проверка столкновения с границами экрана
        if (self.head.position[0] < 0 or self.head.position[0] >= screen_width
                or self.head.position[1] < 0 or self.head.position[1] >= screen_height):
            return True
        return False
    
    def increase_speed(self, speed):
        # Увеличение скорости змеи
        pass  # Здесь можно добавить логику увеличения скорости

class Segment:
    def __init__(self, x, y):
        self.position = (x, y)
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
    
    def randomize_position(self):
        # Генерация случайной позиции для еды
        x = random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE
        y = random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE
        self.position = (x, y)
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

main()
import pygame
import random

# Глобальные константы
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20  # Размер блока (размер одного сегмента змеи)

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Инициализация змеи
    snake = Snake()
    
    # Инициализация еды
    food = Food()
    food.randomize_position()  # Случайная позиция еды
    
    # Счетчик очков
    score = 0
    
    # Уровень сложности (начальная скорость змеи)
    level = 1
    speed = 5
    
    # Флаг окончания игры
    game_over = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            # Управление змеёй с клавиатуры
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.change_direction(RIGHT)
        
        # Движение змеи
        snake.move()
        
        # Проверка столкновения змеи с границами экрана
        if snake.check_collision(SCREEN_WIDTH, SCREEN_HEIGHT):
            game_over = True
        
        # Проверка столкновения змеи с едой
        if snake.head.position == food.position:
            snake.grow()  # Увеличение длины змеи
            food.randomize_position()  # Случайная позиция еды
            score += 1
            
            # Увеличение уровня сложности после съедения определенного количества еды
            if score % 3 == 0:
                level += 1
                speed += 1
                snake.increase_speed(speed)
        
        screen.fill(BLACK)
        
        

        # Отрисовка змеи и еды
        snake.draw(screen)
        food.draw(screen)
        
        # Отображение текущего счета
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score) + " Level: " + str(level), True, WHITE)
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        
        clock.tick(speed)  # Установка скорости обновления экрана (скорости змеи)

class Snake:
    def __init__(self):
        self.head = Segment(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Начальная позиция головы змеи
        self.body = [self.head]  # Список сегментов змеи
        self.direction = RIGHT  # Начальное направление движения
    
    def change_direction(self, direction):
        self.direction = direction
    
    def move(self):
        # Двигаем голову в заданном направлении
        new_head = Segment(self.head.position[0] + self.direction[0] * BLOCK_SIZE,
                          self.head.position[1] + self.direction[1] * BLOCK_SIZE)
        # Добавляем новую голову в начало тела
        self.body.insert(0, new_head)
        self.head = new_head
        # Удаляем последний сегмент тела (хвост), чтобы змея казалась двигающейся
        self.body.pop()
    
    def grow(self):
        # Добавление нового сегмента к змее
        tail = self.body[-1]
        new_segment = Segment(tail.position[0], tail.position[1])
        self.body.append(new_segment)
    
    def draw(self, screen):
        for segment in self.body:
            segment.draw(screen)
    
    def check_collision(self, screen_width, screen_height):
        # Проверка столкновения с границами экрана
        if (self.head.position[0] < 0 or self.head.position[0] >= screen_width
                or self.head.position[1] < 0 or self.head.position[1] >= screen_height):
            return True
        return False
    
    def increase_speed(self, speed):
        # Увеличение скорости змеи
        pass  # Здесь можно добавить логику увеличения скорости

class Segment:
    def __init__(self, x, y):
        self.position = (x, y)
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
    
    def randomize_position(self):
        # Генерация случайной позиции для еды
        x = random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE
        y = random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE
        self.position = (x, y)
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

main()
