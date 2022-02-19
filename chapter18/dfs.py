from graph import Vertex

#depth first search
def dfs_traverse(vertex, visited_vertices={}):
    # mark vertex as visited
    visited_vertices[vertex.value] = True
    print(vertex.value)
    # iterate through current vertexe's adjacent vertices
    for vertex in vertex.adjacent_vertices:
        if not vertex.value in visited_vertices:
            dfs_traverse(vertex, visited_vertices)


# initiate graph
alice = Vertex('alice')
bob = Vertex('bob')
cynthia = Vertex('cynthia')

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
bob.add_adjacent_vertex(cynthia)
cynthia.add_adjacent_vertex(bob)

# execute depth first search
dfs_traverse(alice)