class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = [] # adjacency list
    
    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)