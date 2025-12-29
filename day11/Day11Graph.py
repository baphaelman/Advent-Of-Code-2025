class Day11Node:
    def __init__(self, i):
        self.num: int = i
        self.connected: set[int] = set()
    
    def connect_nodes(self, nodes):
        for node in nodes:
            self.connect(node)
    
    def connect(self, i):
        self.connected.add(i)

class Day11Graph:
    def __init__(self):
        from collections import defaultdict

        self.dp: dict[int, set[int]] = defaultdict(set)
        self.name_to_i: dict[str, int] = {}
        # self.i_to_name: dict[int, str] = {}
        self.len: int = 0
        self.cache1: dict[int, int] = defaultdict(int)
        self.cache2: dict[int, int] = defaultdict(int)
    
    def add_node(self, name):
        if name in self.name_to_i:
            return
        self.name_to_i[name] = self.len
        # self.i_to_name[self.len] = name
        self.len += 1
    
    def connect(self, i, j):
        self.dp[i].add(j)

    """Counts paths from i to j"""
    def count_paths(self, i, j):
        # base case
        if i == j:
            return 1
        if i in self.cache1:
            # print("seeking cache:", i)
            return self.cache1[i]
        
        total = 0
        for next in self.dp[i]:
            # print("next", next)
            total += self.count_paths(next, j)
        self.cache1[i] = total
        return total

    """Counts paths from i to j that visit nodes in l"""
    def count_paths_with_visits(self, i, j, l):
        # base case
        if i == j:
            return 1
        if i in self.cache2:
            # print("seeking cache:", i)
            return self.cache[i]
        
        total = 0
        for next in self.dp[i]:
            # print("next", next)
            total += self.count_paths(next, j)
        self.cache[i] = total
        return total
    
    def parse_dict(d):
        g = Day11Graph()
        # first round,, adding all names
        for name in d:
            g.add_node(name)
            for connection in d[name]:
                g.add_node(connection)

        
        # second round, all connections
        for name in d:
            i = g.name_to_i[name]
            connections = d[name]
            for connection in connections:
                j = g.name_to_i[connection]
                g.connect(i, j)
        return g