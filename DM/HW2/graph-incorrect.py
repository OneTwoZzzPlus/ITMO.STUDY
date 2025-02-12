class InvalideGraph(Exception):
    pass

    
class Graph:
    def __init__(self, table: list[list[int|float]], debug=False):
        """ Проверка корректности таблицы смежности """
        if not isinstance(table, list):
            raise InvalideGraph(f'TABLE must be list, not {type(table)}')
        if len(table) == 0:
            raise InvalideGraph('EMPTY GRAPH')
        for i, row in enumerate(table):
            if not isinstance(row, list):
                raise InvalideGraph(f'Row must be list, ROW {i} has the type {type(row)}')
            if len(row) != len(table):
                raise InvalideGraph(f'The sizes of ROW {i} and TABLE are not equal')
            for j, x in enumerate(row):
                if not isinstance(x, int|float):
                    raise InvalideGraph(f'The weights must be int or float, but the element ({i}, {j}) is of type {type(x)}')
        # Сохранение        
        self.graph = table.copy()
        self.size = len(self.graph)   
        # DEBUG рисуем граф
        self.DEBUG = debug
        if self.DEBUG:
            print('Изначальный граф')
            self.draw()
    
    def draw(self):
        """ Рисует граф """
        try:
            import networkx as nx
            import matplotlib.pyplot as plt
            import numpy as np
            G = nx.from_numpy_array(np.array(self.graph), parallel_edges=False, create_using=nx.DiGraph())
            
            pos=nx.drawing.shell_layout(G)

            nx.draw(G, pos, 
                with_labels=True, 
                node_color='lightblue', 
                node_size=500, 
                font_size=12
            )
            edge_labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

            labels = {node: str(node) for node in G.nodes()}
            nx.draw_networkx_labels(G, pos, labels, font_size=10)

            plt.axis('off')
            plt.tight_layout()
            plt.show()
        except ModuleNotFoundError:
            print('Для рисования графа необходимы сторонние библиотеки, установка:')
            print('pip install numpy matplotlib networkx')

    def _BFS(self, start, finish, parent):
        """ 
            ЧАСТЬ ОСНОВНОГО АЛГОРИТМА
            Поиск в глубину BFS БЕЗ проверки узлов
            Сохраняет для каждой вершины откуда можно в него добраться в список parent
            Получается только 1 путь (остальные избыточны)
            return: существует ли путь
        """
        # Посещённые вершины
        visited = [False]*self.size
        # Очередь
        queue = []
        
        # Добавляем первый элемент в очередь и посещённые
        visited[start] = True
        queue.append(start)
        # Пока очередь не пуста
        while queue:
            # Берём вершину
            current = queue.pop(0)
            # Проходим по всем не посещённым соседям
            for node, weight in enumerate(self.graph[current]):
                if not visited[node] and weight > 0:
                    # Добавляем соседа в очередь и посещённые
                    queue.append(node)
                    visited[node] = True
                    # Сохраняем путь
                    parent[node] = current
                    # Если нашли хотя бы один путь
                    if node == finish:
                        return True
        return False
    
    def _FordFulkerson(self, start, finish):
        """ 
            ОСНОВНОЙ АЛГОРИТМ
            Поиск максимального потока
            ГРАФ ИЗМЕНЯЕТСЯ за время работы!
            Сохранение изначального графа не нужно для рассчётов на скорость
        """
        # Сохраняем путь (вершины из которых можно добраться)
        parent = [-1]*self.size
        # Максимальный поток
        max_flow = 0
        # Пока существует путь
        while self._BFS(start, finish, parent):
            # Берём самый маленькое по весу ребро на пути
            path_flow = float("Inf")
            s = finish
            while(s !=  start):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            # Добавляем поток
            max_flow += path_flow
            # Вычитаем величину потока из пути
            v = finish
            while(v != start):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            # DEBUG рисуем ход решения 
            if self.DEBUG:
                print('Вычитаемый поток:', path_flow)
                self.draw()
                
        return max_flow

    def FordFulkerson(self, start, finish):
        """ Поиск максимального потока """
        graph = self.graph.copy()
        res = self._FordFulkerson(start, finish)
        self.graph = graph.copy()
        return res


if __name__ == "__main__":
    # Таблица смежности графа
    table = [
        [0, 18, 13, 0,  7, 0],
        [0, 0,  10, 12, 0, 0],
        [0, 0,  0,  0,  19, 0],
        [0, 4,  9,  0,  0, 20],
        [0, 0,  8,  7,  0, 4],
        [0, 0,  0,  0,  0, 0]
    ]
    # Создаём граф (debug=True - рисование графа)
    graph = Graph(table, False)
    # Алгоритм Форда-Фалкерсона
    print(graph.FordFulkerson(0, 5))
