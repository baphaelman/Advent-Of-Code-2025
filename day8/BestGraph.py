### DEPRECATED

from Node import Node, Edge
from DisjointSets import DisjointSets
from collections import defaultdict

class BetterGraph:
    def __init__(self, g=None):
        if g:
            self = g.copy()
        else:
            self.size = 0
            self.node_to_i: dict[Node, int] = {}
            self.i_to_node: dict[int, Node] = {}
            self.circuits: DisjointSets = DisjointSets()

            self.edges: dict[Node, set[Node]] = defaultdict(set)
            self.distances: set[float] = set()
            self.distance_to_edges: dict[float, set[Edge]] = defaultdict(set)
    
    def copy(self):
        g2 = BetterGraph()

        g2.size = self.size
        g2.i_to_node = dict(self.i_to_node)
        g2.node_to_i = dict(self.node_to_i)
        g2.circuits = DisjointSets(self.circuits)

        g2.edges = defaultdict(set, {
            node: set(neighbors)
            for node, neighbors in self.edges.items()
        })
        g2.distances = set(self.distances)
        g2.distance_to_edges = defaultdict(set, {
            d: set(edges)
            for d, edges in self.distance_to_edges.items()
        })
        return g2
    
    ### POPULATING GRAPH ###
    def add_node(self, n: Node):
        # update edge stuff
        for node in self.node_to_i:
            d = n.distance(node)
            self.distances.add(d)

            e = Edge(n, node)
            self.distance_to_edges[d].add(e)

        # update circuit stuff
        i = self.size
        self.node_to_i[n] = i
        self.i_to_node[i] = n
        self.circuits.add_elem()

        self.size += 1

    def add_edge(self, e: Edge):
        """
        Just adds edge to data structure,
        doesn't account for change in distances for example
        """
        # circuit stuff
        n1, n2 = e.node_a, e.node_b
        i1, i2 = self.node_to_i[n1], self.node_to_i[n2]
        self.circuits.connect(i1, i2)

        # edges stuff
        self.edges[n1].add(n2)
        self.edges[n2].add(n1)
    
    ### CONVENIENCE STUFF ###
    def add_coord(self, coord: list[int]):
        n = Node(coord[0], coord[1], coord[2])
        self.add_node(n)
    
    def parse_coords(coords: list[list[int]]):
        g = BetterGraph()
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
        sorted_distances = list(self.distances, sorted=True)
        print(sorted_distances)
        for distance in self.distances:
            self.connect_all_distance(distance)
            self.distances.remove(distance)

    """
    self.size = 
        self.node_to_i = 
        self.i_to_node = 
        self.circuits = 

        self.edges = 
        self.distances = 
        self.distance_to_edges = 
        """

if __name__ == "__main__":
    def parse_coords(filepath):
        with open(filepath, 'r') as f:
            str_coords = [line.strip().split(',') for line in f.readlines()]
            int_coords = [[int(num) for num in coord] for coord in str_coords]
        return int_coords

    baby_fp = "baby.txt"
    baby_coords = parse_coords(baby_fp)
    g = BetterGraph.parse_coords(baby_coords)