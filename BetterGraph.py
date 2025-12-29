### DEPRECATED

from day8.Node import Node, Edge
from day8.DisjointSets import DisjointSets

class BetterGraph:
    def __init__(self):
        self.nodes: set[Node] = set()
        self.edges: dict[Edge, int] = {}
        self.node_sets = DisjointSets()

        self.n_to_i: dict[Node, int] = {}
        self.i_to_n: dict[int, Node] = {}
    
    def parse_coords(coords):
        g = BetterGraph()
        for coord in coords:
            g.add_coord(coord)
        return g
    
    def add_coord(self, coord: list[int]):
        if len(coord) == 3:
            n = Node(coord[0], coord[1], coord[2])
        elif len(coord) == 2:
            n = Node(coord[0], coord[1], 0)
        else:
            raise ValueError("coords of length 2 or 3 only")
        self.add_node(n)

    def add_node(self, node: Node):
        # update self.nodes
        self.nodes.add(node)

        # update self.edges
        for other_node in self.nodes:
            e = Edge(node, other_node)
            self.edges[e] = e.distance
        
        # update self.node_sets
        self.node_sets.add_elem()

        # update maps
        index = len(self.nodes) - 1
        self.n_to_i[node] = index
        self.i_to_n[index] = node
    
    def smallest_edge(self):
        min_edge, min_distance = None, float('inf')
        for node1 in self.nodes:
            for node2 in self.nodes:
                e = Edge(node1, node2)
                if self.edges[e] > 0 and self.edges[e] < min_distance:
                    min_edge = e
                    min_distance = self.edges[e]
        return min_edge
    
    def connect_closest(self):
        # find closest
        e = self.smallest_edge()
        self.edges[e] = 0
        a, b = e.node_a, e.node_b
        print("closest", a, b)

        # distances from all nodes to these is minimum of both
        for node in self.nodes:
            edge_a = Edge(node, a)
            edge_b = Edge(node, b)
            # print("distances", self.edges[edge_a], self.edges[edge_b])
            min_dist = min(self.edges[edge_a], self.edges[edge_b])

            self.edges[edge_a] = min_dist
            self.edges[edge_b] = min_dist

        # update self.node_sets
        i1, i2 = self.n_to_i[a], self.n_to_i[b]
        self.node_sets.connect(i1, i2)
        print("connecting", i1, "to", i2)
    
    def three_largest_circuits(self):
        set_sizes = self.node_sets.sizes()
        set_sizes.sort(reverse=True)
        print(set_sizes)
        return set_sizes[0] * set_sizes[1] * set_sizes[2]
    
    def largest_edge(self):
        max_edge, max_distance = None, 0
        for node1 in self.nodes:
            for node2 in self.nodes:
                e = Edge(node1, node2)
                if self.edges[e] > max_distance:
                    max_edge = e
                    max_distance = self.edges[e]
        return max_edge