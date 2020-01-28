from collections import defaultdict, deque


class Graph:

    UNDIRECTED = 0
    DIRECTED = 1

    def __init__(self, type_=UNDIRECTED):
        self.type_ = type_
        self._graph = defaultdict(set)

    def __str__(self):
        return "\n".join(
            f'{vertex} -> {self._graph[vertex]}'
            for vertex in self._graph
        )

    def add_edge(self, src, dst):
        self._graph[src].add(dst)
        if self.type_ == Graph.UNDIRECTED:
            self._graph[dst].add(src)

    def get_adjacent(self, vertex):
        return self._graph[vertex]

    def is_empty(self):
        return len(self._graph) == 0


class BFS1:
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex

    def __iter__(self):
        visited = set()
        visit_queue = deque()  # Queue
        visit_queue.append(self.start_vertex)

        while visit_queue:
            vertex = visit_queue.popleft()
            if vertex not in visited:
                yield vertex
                visited.add(vertex)
                visit_queue.extend(self.graph.get_adjacent(vertex))


class BFS2:
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex

    def __iter__(self):
        visit_queue = deque()  # Queue
        visit_queue.append(self.start_vertex)
        visited = {self.start_vertex}

        while visit_queue:
            vertex = visit_queue.popleft()
            yield vertex
            for vertex in self.graph.get_adjacent(vertex):
                if vertex not in visited:
                    visited.add(vertex)
                    visit_queue.append(vertex)


class DFS:
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex

    def __iter__(self):
        visited = set()
        visit_stack = deque()  # Stack
        visit_stack.append(self.start_vertex)

        while visit_stack:
            vertex = visit_stack.pop()
            if vertex not in visited:
                yield vertex
                visited.add(vertex)
                visit_stack.extend(sorted(
                    self.graph.get_adjacent(vertex), reverse=True
                ))


