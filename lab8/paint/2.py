import pygame

# Инициализация Pygame
pygame.init()

# Установка частоты кадров
fps = 60

# Создание таймера для управления частотой кадров
timer = pygame.time.Clock()

# Установка ширины и высоты окна
WIDTH = 800
HEIGHT = 600

# Текущая активная фигура для рисования (0 - круг, 1 - прямоугольник)
active_figure = 0

# Текущий активный цвет
active_color = 'white'

# Создание окна с заданными шириной и высотой
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Установка заголовка окна
pygame.display.set_caption("Paint")

# Список для хранения элементов рисунка
painting = []

# Функция для отрисовки меню
def draw_menu(color):
    # Отрисовка фона меню
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    # Отрисовка разделительной линии
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    
    # Отрисовка кнопок кистей
    circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    pygame.draw.circle(screen, 'black', (35, 35), 18)
    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)
    
    # Формирование списка кистей
    brush_list = [circle_brush, rect_brush]
    
    # Отрисовка выбранного цвета
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)
    
    # Загрузка и отрисовка изображения ластика
    eraser = pygame.image.load("lab2/lab8/paint/eraser-square-svgrepo-com.svg")
    eraser_rect = eraser.get_rect(topleft=(WIDTH - 150, 7))
    eraser_rect.width = eraser_rect.height = 25
    screen.blit(eraser, [WIDTH - 150, 7, 25, 25])
    
    # Отрисовка цветовой палитры
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    
    # Формирование списка кнопок цветов
    color_rect = [blue, red, green, yellow, teal, purple, black, eraser_rect]
    
    # Задание списка RGB-значений цветов
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]
    
    # Возврат списков кистей, цветов и их значений RGB
    return brush_list, color_rect, rgb_list

# Функция для отрисовки элементов рисунка на холсте
def draw_painting(paints):
    for color, pos, figure in paints:
        if color == (255, 255, 255):
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20])
        else:
            if figure == 0:
                pygame.draw.circle(screen, color, pos, 20, 2)
            elif figure == 1:
                pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)

# Основной игровой цикл
run = True
while run:
    # Установка частоты кадров
    timer.tick(fps)
    
    # Заливка экрана белым цветом
    screen.fill("white")
    
    # Получение текущей позиции мыши и состояния левой кнопки мыши
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    
    # Отрисовка меню и получение списков кистей, цветов и их значений RGB
    brushes, colors, rgbs = draw_menu(active_color)
    
    # Добавление элементов рисунка по щелчку левой кнопки мыши
    if left_click and mouse[1] > 85:
        painting.append((active_color, mouse, active_figure))
    
    # Отрисовка элементов рисунка
    draw_painting(painting)
    
    # Отрисовка текущего инструмента рисования (кисти или ластика)
    if mouse[1] > 85:
        if active_color == (255, 255, 255):
            pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20])
        else:
            if active_figure == 0:
                pygame.draw.circle(screen, active_color, mouse, 20, 2)
            elif active_figure == 1:
                pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Обработка нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Обновление активного цвета при выборе цвета из палитры
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            # Обновление активного инструмента при выборе кисти
            for i in brushes:
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame после выхода из игрового цикла
pygame.quit()
