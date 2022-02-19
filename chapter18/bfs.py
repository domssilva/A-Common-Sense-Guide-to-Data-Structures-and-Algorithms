from graph import Vertex
from queue import Queue

# breadth first search
def bfs_traverse(vertex):
    queue = Queue(maxsize=0)
    visited_vertices = {}
    # set vertex as visited
    visited_vertices[vertex.value] = True
    # enqueue vertex
    queue.put(vertex)
    # perform bfs
    while not queue.empty():
        # dequeue current vertex
        vertex = queue.get()
        print(vertex.value)
        # iterate over current vertex's adjacent vertices
        for adjacent_vertex in vertex.adjacent_vertices:
            if not adjacent_vertex.value in visited_vertices:
                # set adjacent vertex as visited
                visited_vertices[adjacent_vertex.value] = True
                # enqueue vertex
                queue.put(adjacent_vertex)


# initiate graph
alice = Vertex('Alice')
bob = Vertex('Bob')
fred = Vertex('Fred')
helen = Vertex('Helen')
candy = Vertex('Candy')
derek = Vertex('Derek')
elaine = Vertex('Elaine')
gina = Vertex('Gina')
irena = Vertex('Irena')

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)

bob.add_adjacent_vertex(fred)
bob.add_adjacent_vertex(helen)

derek.add_adjacent_vertex(gina)
derek.add_adjacent_vertex(irena)

# execute breadth first search
bfs_traverse(alice)
