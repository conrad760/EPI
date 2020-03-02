class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.discovery = 0
        self.finish = 0
        self.distance = 999
        self.color = 'black'

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph_distance(self):
        print('Graph Distance')
        for key in sorted(list(self.vertices.keys())):
            print(key, str(self.vertices[key].neighbors), str(
                self.vertices[key].distance))

    def print_graph_discovery(self):
        print('Graph Discovery')
        for key in sorted(list(self.vertices.keys())):
            print(key, str(self.vertices[key].neighbors), str(
                self.vertices[key].discovery))

    def _dfs(self, vert):
        global time
        vert.distance = 0
        vert.color = 'red'
        vert.discovery = time
        for v in vert.neighbors:
          if self.vertices[v].color == 'black':
            self._dfs(self.vertices[v])
        vert.color = 'blue'
        vert.finish = time
        time += 1

    def dfs(self, vert):
      global time
      time = 1
      self._dfs(vert)
     
    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1


if __name__ == '__main__':
    g = Graph()
    a = Vertex('A')
    g.add_vertex(a)
    for i in range(ord('A'), ord('N')):
        g.add_vertex(Vertex(chr(i)))

    default_edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HI']
    edges = [str(chr(x)+chr(x+1)) for x in range(ord('A'), ord('K'))]
    for edge in default_edges:
        g.add_edge(edge[:1], edge[1:])
    print(edges)
    # g.bfs(a)
    g.print_graph_distance()
    g.DFS(a)
    g.print_graph_discovery()
