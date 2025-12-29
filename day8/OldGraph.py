from Node import Node, Edge
from DisjointSets import DisjointSets
import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        # for DisjointSets
        self.size = 0
        self.i_to_node: dict[int, Node] = {} # pair maps from 
        self.node_to_i: dict[Node, int] = {} 
        self.node_sets = DisjointSets() 

        # TAKE 3
        self.edges: dict[Node, set[Node]] = defaultdict(set) # node to its set of existing edge complements
        self.distances: set[float] = set() # all (unexhausted) edge distances
        self.edges_of_dist: dict[float, set[Edge]] = defaultdict(int) # from distance to all edges of that distance
    
    def parse_coords(coords):
        g = Graph()
        for coord in coords:
            g.add_coord(coord)
        return g
    
    def connect_closest(self):
        smallest = self.smallest_edge()
        self.add_edge(smallest[0], smallest[1])
        return smallest
    
    def add_coord(self, coord):
        n = Node(coord[0], coord[1], coord[2])
        self.add_node(n)
    
    def add_node(self, n: Node):
        """Assuming completely new node"""

        # update edges stuff
        for node in self.node_to_i:
            d = n.distance(node)
            self.distances.add(d)
            e = Edge(n, node)
            self.edges_of_dist[d].add(e)
            
        # update DisjointSets stuff
        i = self.size
        self.i_to_node[i] = n
        self.node_to_i[n] = i
        self.node_sets.add_elem()
        self.size += 1
    
    def add_edge(self, n1: Node, n2: Node):
        i1, i2 = self.node_to_i[n1], self.node_to_i[n2]
        self.node_sets.connect(i1, i2)

        # update edges
        self.edges[n1].add(n2)
        self.edges[n2].add(n1)
    
    def copy(self):
        g2 = Graph()
        g2.size = self.size

        g2.i_to_node = dict(self.i_to_node)
        g2.node_to_i = dict(self.node_to_i)

        g2.edges = defaultdict(set, {
            node: set(neighbors)
            for node, neighbors in self.edges.items()
        })

        g2.distances = set(self.distances)

        g2.edges_of_dist = defaultdict(set, {
            d: set(edges)
            for d, edges in self.edges_of_dist.items()
        })

        g2.node_sets = DisjointSets(self.node_sets)
        return g2
    
    def connect_n_smallest(self, n):
        """
        Roughly n
        Technically I add all edges of the final distance for convenience
        """
        count = 0
        while count < n:
            d = min(self.distances)
            count += 
        pass
    
    def final_connection(self):
        step = 1000
        while True:
            self.connect_n_smallest(step)
        pass
    
    ### DEPRECATED
    """
    def smallest_edge(self):
        # Taking into account existing edges
        curr_distance = float('inf')
        curr_closest = []
        for i in range(self.size):
            n1 = self.i_to_node[i]
            for j in range(i + 1, self.size):
                n2 = self.i_to_node[j]
                if n2 in self.edges[n1]: # ignore edges already made
                    continue
                dist = n1.distance(n2)
                if dist < curr_distance:
                    curr_distance = dist
                    curr_closest = [n1, n2]
        return curr_closest

    def largest_circuits(self):
        set_sizes = self.node_sets.sizes()
        set_sizes.sort(reverse=True)
        return set_sizes
    
    def n_smallest_edges(self, n):
        # Yes taking into account existing edges
        heap = []
        for i in range(self.size):
            n1 = self.i_to_node[i]
            for j in range(i + 1, self.size):
                n2 = self.i_to_node[j]
                if (n1, n2) in self.edges: # ignore edges already made
                    continue
                dist = n1.distance(n2)
                e = Edge(n1, n2)
                if len(heap) < n: # if in top n by default
                    heapq.heappush(heap, (-dist, e))
                else:
                    if dist < -heap[0][0]:
                        heapq.heapreplace(heap, (-dist, e))

        return [e for _, e in heap]
    
    def connect_n_smallest(self, n):
        edges = self.n_smallest_edges(n)
        for edge in edges:
            self.add_edge(edge.node_a, edge.node_b)
    
    def final_connection(self):
        # connects closest edges one by one
        # returns final edge

        while True:
            e = self.connect_closest()
            if len(self.largest_circuits()) == 1:
                break
        return e
    """