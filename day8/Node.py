import math
class Node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def distance(self, o: object):
        assert type(o) is Node
        x, y, z = self.x, self.y, self.z
        xo, yo, zo = o.x, o.y, o.z
        return math.sqrt((x - xo)**2 + (y - yo)**2 + (z - zo)**2)

    def __eq__(self, o: object):
        assert type(o) is Node
        return (self.x == o.x) and (self.y == o.y) and (self.z == o.z)

    def __hash__(self):
        return hash(self.x) + hash(self.y) + hash(self.z)

class Edge:
    def __init__(self, a: Node, b: Node):
        self.node_a = a
        self.node_b = b
    
    def __eq__(self, o):
        assert type(o) == Edge
        node_oa, node_ob = o.node_a, o.node_b
        return (self.node_a == node_oa and self.node_b == node_ob) or (self.node_a == node_ob and self.node_b == node_oa)

    def __hash__(self):
        return hash(self.node_a) + hash(self.node_b)