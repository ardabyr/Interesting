import numpy as np

# Класс алгоритма Ant Colony Optimization
class AntColony():
    def __init__(self, width, height, obstacles, ant_count, step_count, alpha, gamma, evaporation_rate, start, end, colony_iter):
        self.width = width
        self.height = height
        self.obstacles = obstacles
        self.ant_count = ant_count
        self.step_count = step_count
        self.alpha = alpha
        self.gamma = gamma
        self.evaporation_rate = evaporation_rate
        self.start = start
        self.end = end
        self.colony_iter = colony_iter
        self.pheromone_grid = np.ones(shape=(self.width, self.height))
        self.ants_movements = []
    
    # Испарение феромона
    def pheromone_diffusion(self, phi, r, xi):
        return self.gamma * phi * (r - xi) / r

    # Возвращает список пригодных для движения ячеек
    def can_go_grid_list(self, position, previous):
        x = position[0]
        y = position[1]
        x_p = previous[0]
        y_p = previous[1]
        # Результрующий список
        res = []
        # Цикл идет по 8 клеткам вокруг текущей ячейки
        for i in range(max(x - 1, 0), min(x + 2, self.height)):
            for j in range(max(y - 1, 0), min(y + 2, self.width)):
                # Условия пригодности клетки:
                # - Не текущая клетка
                # - Не предыдущая
                # - Не препятствие
                # Если выполнены - добавляем в результирующий список
                if (not (i, j) == (x_p, y_p)) and (not (i, j) == (x, y)) and (not (i, j) in self.obstacles):
                    res.append((i, j))
        return res
    
    # Функция продвижения муравьев
    def move_ant(self):
        position = self.start # Текущая позиция
        visited_grids = [(position[0], position[1])] # Посещенные точки. Сразу добавляем текущую позицию
        # Делаем step_count шагов
        for i in range(self.step_count):
            # Список пригодных для перехода ячеек
            can_go_list = self.can_go_grid_list(visited_grids[i], visited_grids[i-1])
            # Список вероятностей
            p = [] 
            # Проходим по возможным ячейкам и добавляем вероятность перехода в точку
            for can_go in can_go_list:
                p.append(self.pheromone_grid[can_go[0], can_go[1]] ** self.alpha)            
            # Решаем, в какую точку идет муравей  
            p = np.array(p)
            p /= np.sum(p)
            p = np.cumsum(p)
            r = np.random.random()
            for j in range(len(p)):
                if p[j] >= r:
                    break
            # Добавляем точку в список пройденных
            visited_grids.append(can_go_list[j])
            if can_go_list[j][0] == self.end[0] and can_go_list[j][1] == self.end[1]:
                break
        return visited_grids
    
    # Вычисление длины пути
    def get_path_len(self, path):
        length = 0
        # Проходим по всем точкам и считаем обычное расстояние из линала
        for i in range(1, len(path)):
            length += np.linalg.norm(np.array(path[i]) - np.array(path[i-1]))
        return length
    
    # Функция сглаживания пути
    def optimize_path(self, path):
        # Создание нового пути
        new_path = [path[0]]
        i = 1
        while i < len(path) - 1:
            grid = path[i]
            new_path.append(grid)
            # Список смежных ячеек (не препятствий)
            tmp_grids = []
            # Добавляем смежные ячейки
            for j in range(max(grid[0] - 1, 0), min(grid[0] + 2, 20)):
                for k in range(max(grid[1] - 1, 0), min(grid[1] + 2, 20)):
                    if not (j, k) in self.obstacles:
                        tmp_grids.append((j, k))

            # Удаляем текущую и предыдущую ячейку
            tmp_grids.remove(grid)
            tmp_grids.remove(path[i-1])
            
            # Смотрим, есть ли повторяющиеся точки в оставшейся части пути
            # Если есть, обновляем индекс i для продолжентя поиска
            for tmp_grid in tmp_grids:
                if tmp_grid in path[i:]:
                    for j in range(path[i:].count(tmp_grid)):
                        i = path[i:].index(tmp_grid) + i
                        
        # Добавляем новый путь
        new_path.append(path[-1])
        return new_path
    
    # Функция, запускающая поиск пути  
    def run_ant_colony(self, Q):
        complete_paths = []
        for t in range(self.colony_iter):
            complete_paths = []
            # Создаем матрицу с феромонами каждый проход колонии
            d_pheromone = np.zeros(shape=(self.width, self.height))
            for i in range(self.ant_count):
                # Получаем какой-то путь муравьев
                ant_path = self.move_ant()
                # Проверяем, дошли ли они до конца
                if ant_path[-1] == (self.end[0], self.end[1]):
                    # Сглаживаем путь и добавляем его в результирующие пути
                    ant_path = self.optimize_path(ant_path)
                    complete_paths.append((self.get_path_len(ant_path), ant_path))
                    # Обновление матрицы феромонов
                    for grid in ant_path:
                        d_pheromone[grid[0], grid[1]] += Q / self.get_path_len(complete_paths[-1][1])
                        for j in range(max(grid[0] - 1, 0), min(grid[0] + 2, self.height)):
                            for k in range(max(grid[1] - 1, 0), min(grid[1] + 2, self.width)):
                                if not (j, k) in self.obstacles:
                                    d_pheromone[j, k] += self.pheromone_diffusion(self.pheromone_grid[j, k] + d_pheromone[grid[0], grid[1]], 2, np.linalg.norm(np.array(grid) - np.array((j, k))))
            self.pheromone_grid = (1 - self.evaporation_rate) * \
                self.pheromone_grid + d_pheromone
        # Сортировка путей по длине
        complete_paths = sorted(complete_paths, key=lambda x: x[0])
        return complete_paths