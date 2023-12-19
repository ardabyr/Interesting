import pygame
import math
from ant import *
import numpy as np

# Инициализация пайгейма
pygame.init()

# Типы клеток
SPACE = 0
START = 1
END = 2
BARRIER = 3
PATH = 4

# Количество строк
ROWS = 20

# Раземеры окна
WIDTH = 800
HEIGHT = 600

# Размер ячейки
CELL_SIZE = WIDTH // ROWS

# Инициализация пайгейма
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Algorithm")

# Класс поля
class Grid:
    def __init__(self, row, col):
        self.obstacles = []
        self.grid = []
        self.init_grid()

    def init_grid(self):
        for i in range(ROWS):
            curr_row = []
            for j in range(ROWS):
                curr_row.append(Square(i, j, SPACE))
            self.grid.append(curr_row)

# Класс ячейки
class Square:
    def __init__(self, row, col, stype):
        self.row = row
        self.col = col
        self.stype = stype
        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE


# Проходит по всей матрице ячеек, ищет преграды и создает из их координат список
def get_obstacles(matrix):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 3):
                res.append((i, j))
    return res

# Рисует сетку
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, (26, 26, 26), (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, (26, 26, 26), (j * gap, 0), (j * gap, width))

# Рисует объекты (цветные квадраты) в зависимости от типа ячейки
def draw_objects(grid):
    for i in range(ROWS):
        for j in range(ROWS):
            curr = grid[i][j]
            if (curr.stype == BARRIER):
                pygame.draw.rect(win, (0, 0, 0), (curr.x, curr.y, CELL_SIZE, CELL_SIZE))
            elif (curr.stype == START):
                pygame.draw.rect(win, (0, 255, 0), (curr.x, curr.y, CELL_SIZE, CELL_SIZE))
            elif (curr.stype == END):
                pygame.draw.rect(win, (255, 0, 0), (curr.x, curr.y, CELL_SIZE, CELL_SIZE))
            elif (curr.stype == PATH):
                pygame.draw.rect(win, (0, 0, 255), (curr.x, curr.y, CELL_SIZE, CELL_SIZE))

# Рисует путь по переданным координатам ячеек
def draw_path(path):
    for elem in path:
        x = elem[1] * CELL_SIZE
        y = elem[0] * CELL_SIZE
        pygame.draw.rect(win, (0, 0, 255), (x, y, CELL_SIZE, CELL_SIZE))

# Создаем сетку
grid = Grid(ROWS, ROWS)

# Флаги для проверки того, нарисовали ли мы начало и конец
start_drawn = False
end_drawn = False

# Флаг для цикла
running = True

# Главный цикл рисования
while running:
    # Ловим пользовательские действия
    for event in pygame.event.get():
        # Нажатия на крестик справа вверху
        if event.type == pygame.QUIT:
            running = False
        # Нажатие на кнопку мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() # Поулчаем координаты курсора
            row, col = mouse_pos[1] // CELL_SIZE, mouse_pos[0] // CELL_SIZE # Считаем, в какую клетку мы ткнули
            if event.button == 1 and (row, col) not in grid.obstacles: # Если кнопка - левая и этой ячейки нет в списке препятствий
                grid.obstacles.append((row, col)) # Добавляем координаты препятствия в список препятствий
                grid.grid[row][col] = Square(row, col, BARRIER) # Добавляем ячейку в сетку
                #print(grid.obstacles)
            elif event.button == 3: # Если кнопка - правая
                if not start_drawn: # Если не нарисовали начало
                    start_point = Square(row, col, START) # Тут вроде ясно
                    grid.grid[row][col] = start_point
                    start_drawn = True
                elif not end_drawn: # Если не нарисовали конец
                    end_point = Square(row, col, END) # Same
                    grid.grid[row][col] = end_point
                    end_drawn = True
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Жмем не пробел
            # Создаем класс нашего алгоса и запихиваем в него кучу параметров
            aco_pdg = AntColony(ROWS, ROWS, grid.obstacles, 
                                ant_count=50, step_count=100, 
                                alpha=1.1, gamma=0.02, 
                                evaporation_rate=0.5, 
                                start=np.array([start_point.row, start_point.col]), 
                                end=np.array([end_point.row, end_point.col]), 
                                colony_iter=ROWS)
            # Запускаем муравьев
            o = aco_pdg.run_ant_colony(10)
            paths = []
            # Проходим по всем путям
            # elem = (длина пути1, [вершина1, вершина2, ...])
            for elem in o:
                # Убираю начальную и конечную точку
                elem[1].remove((start_point.row, start_point.col))
                elem[1].remove((end_point.row, end_point.col))
                # Добавляю путь в список путей
                paths.append(elem[1])
            # Отключаем главный цикл
            running = False

    # Каждый проход цикла
    win.fill((255, 255, 255)) # Заливаем экран белым
    draw_grid(win, ROWS, WIDTH) # Рисуем сетку
    draw_objects(grid.grid) # Рисуем объекты
    pygame.display.update() # Обновляем экран

# Флаг для цикла просмотра путей
viewing_paths = True

# Если путь есть, ставим в текущий путь первый из нашего списка
# Если путей нет, завершаем работу
if (len(paths) > 0):
    curr_path = paths[0] #make_path_grid(grid.grid, paths[0])
else:
    print("NO WAYS FOUNDED :(")
    viewing_paths = False

# Указатель на текущий путь в списке
pointer = 0
max_size = len(paths)

# Цикл просмотра путей
while viewing_paths:
    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            viewing_paths = False
        
        # Стрелка вправо
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            # Прибавляем указатель, берем остаток чтобы после конца списка мы уходили в начало
            pointer = pointer + 1
            pointer = pointer % max_size
            curr_path = paths[pointer] # Меняем текущий путь
            #print_info(curr_grid)
        # Стрелка влево
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            # Убавляем указатель, если ушли в минус переходим в конец списка
            pointer = pointer -1
            if pointer < 0:
                pointer = max_size - 1
            curr_path = paths[pointer]

    # Как и в прошлом
    win.fill((255, 255, 255))
    draw_grid(win, ROWS, WIDTH)
    draw_objects(grid.grid)
    draw_path(curr_path) # Рисуем путь, на который направлен указатель
    pygame.display.update()


    
    
