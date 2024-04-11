# Импорт библиотек
import pygame
import math

# Инициализация Pygame
pygame.init()

# Установка параметров игры
fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_figure = 0
active_color = 'white'
figure_size = 20  # Размер фигур по умолчанию

# Создание окна
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []

# Функция для рисования квадрата
def draw_square(pos, size, color):
    pygame.draw.rect(screen, color, [pos[0] - size, pos[1] - size, size * 2, size * 2], 2)

# Функция для рисования прямоугольного треугольника
def draw_right_triangle(pos, size, color):
    pygame.draw.polygon(screen, color, [(pos[0], pos[1] - size), (pos[0] + size, pos[1] + size), (pos[0] - size, pos[1] + size)], 2)

# Функция для рисования равностороннего треугольника
def draw_equilateral_triangle(pos, size, color):
    height = size * math.sqrt(3) / 2
    pygame.draw.polygon(screen, color, [(pos[0], pos[1] - height), (pos[0] + size, pos[1] + height / 2), (pos[0] - size, pos[1] + height / 2)], 2)

# Функция для рисования ромба
def draw_rhombus(pos, size, color):
    pygame.draw.polygon(screen, color, [(pos[0], pos[1] - size), (pos[0] + size, pos[1]), (pos[0], pos[1] + size), (pos[0] - size, pos[1])], 2)

# Функция для отрисовки меню
def draw_menu(color):
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    pygame.draw.circle(screen, 'black', (35, 35), 18)
    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)

    brush_list = [circle_brush, rect_brush]

    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    # Загрузка изображения ластика и его отрисовка
    eraser = pygame.Surface((25, 25))
    eraser.fill((255, 255, 255))
    pygame.draw.rect(eraser, 'black', [0, 0, 25, 25], 3)
    screen.blit(eraser, [WIDTH - 150, 7, 25, 25])

    # Отрисовка кнопок выбора цвета и ластика
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    plus_button = pygame.draw.rect(screen, 'black', [10, 90, 20, 20])  # Кнопка "Плюс"
    minus_button = pygame.draw.rect(screen, 'black', [40, 90, 20, 20])  # Кнопка "Минус"

    square_button = pygame.draw.rect(screen, 'black', [70, 90, 20, 20])  # Кнопка "Квадрат"
    right_triangle_button = pygame.draw.rect(screen, 'black', [100, 90, 20, 20])  # Кнопка "Прямоугольный треугольник"
    equilateral_triangle_button = pygame.draw.rect(screen, 'black', [130, 90, 20, 20])  # Кнопка "Равносторонний треугольник"
    rhombus_button = pygame.draw.rect(screen, 'black', [160, 90, 20, 20])  # Кнопка "Ромб"

    # Список цветов и их RGB значений
    color_rect = [blue, red, green, yellow, teal, purple, black, eraser.get_rect(topleft=(WIDTH - 150, 7))]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return brush_list, color_rect, rgb_list, plus_button, minus_button, square_button, right_triangle_button, equilateral_triangle_button, rhombus_button

# Функция для отрисовки созданных пользователем фигур
def draw_painting(paints):   
    for color, pos, figure, size in paints:
        if color == (255, 255, 255):
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20])
        elif figure == 0:
            pygame.draw.circle(screen, color, pos, size, 2)
        elif figure == 1:
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)
        elif figure == 2:  # Квадрат
            draw_square(pos, size, color)
        elif figure == 3:  # Прямоугольный треугольник
            draw_right_triangle(pos, size, color)
        elif figure == 4:  # Равносторонний треугольник
            draw_equilateral_triangle(pos, size, color)
        elif figure == 5:  # Ромб
            draw_rhombus(pos, size, color)

# Основной цикл игры
run = True
while run:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    # Отрисовка меню и получение информации о выбранных опциях
    brushes, colors, rgbs, plus_button, minus_button, square_button, right_triangle_button, equilateral_triangle_button, rhombus_button = draw_menu(active_color)

    # Рисование фигур при клике левой кнопкой мыши
    if left_click and mouse[1] > 85:
        painting.append((active_color, mouse, active_figure, figure_size))
    draw_painting(painting)

    # Отрисовка активного курсора мыши
    if mouse[1] > 85:
        if active_color == (255, 255, 255):
            pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20])
        elif active_figure == 0:
            pygame.draw.circle(screen, active_color, mouse, figure_size, 2)
        elif active_figure == 1:
            pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)
        elif active_figure == 2:  # Квадрат
            draw_square(mouse, figure_size, active_color)
        elif active_figure == 3:  # Прямоугольный треугольник
            draw_right_triangle(mouse, figure_size, active_color)
        elif active_figure == 4:  # Равносторонний треугольник
            draw_equilateral_triangle(mouse, figure_size, active_color)
        elif active_figure == 5:  # Ромб
            draw_rhombus(mouse, figure_size, active_color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            for i in brushes:
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]

            # Обработка событий при нажатии на кнопки
            if plus_button.collidepoint(event.pos):  # Кнопка "Плюс"
                figure_size += 5
            elif minus_button.collidepoint(event.pos):  # Кнопка "Минус"
                figure_size = max(5, figure_size - 5)
            elif square_button.collidepoint(event.pos):  # Кнопка "Квадрат"
                active_figure = 2
            elif right_triangle_button.collidepoint(event.pos):  # Кнопка "Прямоугольный треугольник"
                active_figure = 3
            elif equilateral_triangle_button.collidepoint(event.pos):  # Кнопка "Равносторонний треугольник"
                active_figure = 4
            elif rhombus_button.collidepoint(event.pos):  # Кнопка "Ромб"
                active_figure = 5

    pygame.display.flip()

pygame.quit()  # Завершение работы Pygame
