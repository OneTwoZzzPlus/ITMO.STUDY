class InvalidGraph(Exception):
    pass

    
class Graph:
    def __init__(self, table: list[list[int|float]], debug=False):
        """ Проверка корректности таблицы смежности """
        if not isinstance(table, list):
            raise InvalidGraph(f'TABLE must be list, not {type(table)}')
        if len(table) == 0:
            raise InvalidGraph('EMPTY GRAPH')
        for i, row in enumerate(table):
            if not isinstance(row, list):
                raise InvalidGraph(f'Row must be list, ROW {i} has the type {type(row)}')
            if len(row) != len(table):
                raise InvalidGraph(f'The sizes of ROW {i} and TABLE are not equal')
            for j, x in enumerate(row):
                if not isinstance(x, int|float):
                    raise InvalidGraph(f'The weights must be int or float, but the element ({i}, {j}) is of type {type(x)}')
        # Сохранение        
        self.graph = table.copy()
        self.size = len(self.graph)   
        # DEBUG (рисуем граф во время решения) 
        self.DEBUG = debug
    
    def draw(self):
        """ Рисует граф, если установлены библиотеки """
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

    def DFS(self, start, finish, parent):
        """ 
            Поиск в глубину DFS
            Часть алгоритма Форда-Фалкерсона
            
            start: начальная вершина
            finish: искомая вершина
                        
            return: существует ли путь
            parent: сохраняет путь в список 
        """
        # Посещённые вершины
        visited = [False]*self.size
        # Очередь
        stack = []
        
        # Добавляем первый элемент в очередь и посещённые
        visited[start] = True
        stack.append(start)
        # Пока очередь не пуста
        while stack:
            # Берём вершину
            current = stack.pop()
            # Проходим по всем не посещённым соседям
            for node, weight in enumerate(self.graph[current]):
                if not visited[node] and weight > 0:
                    # Добавляем соседа в очередь и посещённые
                    stack.append(node)
                    visited[node] = True
                    # Сохраняем путь
                    parent[node] = current
                    # Если нашли хотя бы один путь
                    if node == finish:
                        return True
        return False

    def BFS(self, start, finish, parent):
        """ 
            Поиск в глубину BFS
            Часть алгоритма Эдмондса–Карпа
            
            start: начальная вершина
            finish: искомая вершина
                        
            return: существует ли путь
            parent: сохраняет путь в список 
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
    
    def MaxFlow(self, start, finish, path_exist):
        """ 
            Алгоритм Форда-Фалкерсона
            Может использовать любой способ поиска пути
            
            start: исток, начальная вершина
            finish: сток, конечная вершина
            path_exist: алгоритм поиска пути
            
            return: максимальный поток
        """
        # В процессе работы граф меняется, сохраняем изначальный
        saved_graph = __import__("copy").deepcopy(self.graph)
        # В parent cохраняем путь (вершины из которых можно добраться в каждую вершину)
        parent = [-1]*self.size
        # Максимальный поток
        max_flow = 0
        # Пока существует путь
        while path_exist(start, finish, parent):
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
        
        # Восстанавливаем граф
        self.graph = saved_graph
        return max_flow

    def FordFulkerson(self, start, finish):
        return self.MaxFlow(start, finish, self.DFS)
    
    def EdmondsKarp(self, start, finish):
        return self.MaxFlow(start, finish, self.BFS)


if __name__ == "__main__":
    # Таблица смежности графа
    table = [
        [0, 18, 13, 0,  7, 0],
        [0, 0,  10, 12, 0, 0],
        [0, 0,  0,  0,  19, 0],
        [0, 4,  9,  0,  0, 20],
        [0, 0,  8,  7,  0, 4],
        [0, 0,  -999,  0,  0, 0]
    ]
    # Создаём граф (debug=True - рисование графа)
    graph = Graph(table, False)
    
    print("Алгоритм Форда-Фалкерсона")
    print("Максимальный поток:", graph.FordFulkerson(0, 5))
    print("Алгоритм Эдмондса–Карпа")
    print("Максимальный поток :", graph.EdmondsKarp(0, 5))
