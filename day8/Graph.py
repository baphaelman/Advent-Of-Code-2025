from Node import Node, Edge
from DisjointSets import DisjointSets
from typing import Tuple
import heapq

class Graph:
    def __init__(self):
        self.size = 0
        self.node_to_i: dict[Node, int] = {}
        self.i_to_node: dict[int, Node] = {}
        self.circuits: DisjointSets = DisjointSets()

        self.heap: heapq[Tuple[int, Edge]] = []

    def circuit_sizes(self):
        return self.circuits.sizes()
    
    ### POPULATING GRAPH ###
    def add_node(self, n: Node):
        # update heap stuff
        for node in self.node_to_i:
            d = n.distance(node)
            e = Edge(n, node)
            heapq.heappush(self.heap, (d, e))
            self.heap

        # update circuit stuff
        i = self.size
        self.node_to_i[n] = i
        self.i_to_node[i] = n
        self.circuits.add_elem()

        self.size += 1

    def connect_closest(self):
        """
        Connects closest currently unconnected breaker boxes
        Returns added edge
        """
        # pops smallest edge from heap
        _, e = heapq.heappop(self.heap)

        # connects circuit accordingly
        n1, n2 = e.node_a, e.node_b
        i1, i2 = self.node_to_i[n1], self.node_to_i[n2]
        self.circuits.connect(i1, i2)
        return e
    
    ### CONVENIENCE STUFF ###
    def add_coord(self, coord: list[int]):
        n = Node(coord[0], coord[1], coord[2])
        self.add_node(n)
    
    def parse_coords(coords: list[list[int]]):
        g = Graph()
        for coord in coords:
            g.add_coord(coord)
        return g
    
    def is_converged(self):
        return len(self.circuits.sizes()) == 1
    
    ### HEAVY LIFTING ###
    def last_connection(self):
        """
        Add all edges of increasing distance until convergence
        """
        while not self.is_converged():
            e = self.connect_closest()
        return e