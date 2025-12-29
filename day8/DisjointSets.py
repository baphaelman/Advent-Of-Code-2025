class DisjointSets:
    def __init__(self, d=None):
        if d:
            self.data = list(d.data)
            self.len = d.len
        else:
            self.data = []
            self.len = 0

    def add_elem(self):
        self.data.append(-1)
        self.len += 1
    
    def connect(self, n1: int, n2: int):
        assert (n1 >= 0 and n1 < self.len)
        assert (n2 >= 0 and n2 < self.len)

        # find tree size by climbing branches
        n1_parent, n2_parent = self.parent(n1), self.parent(n2)
        if n1_parent == n2_parent:
            return
        
        v1, v2 = abs(self.data[n1_parent]), abs(self.data[n2_parent])
        
        # connect smaller tree to larger one
        if v1 > v2:
            self.data[n2_parent] = n1
            self.data[n1_parent] -= v2 # adjust tree size by smaller tree's value
        else:
            self.data[n1_parent] = n2
            self.data[n2_parent] -= v1
    
    def parent(self, n: int):
        assert (n >= 0 and n < self.len)

        indeces_passed = [n]
        val, i = self.data[n], n
        while val > -1:
            i = val
            val = self.data[val]
            indeces_passed.append(i)
        
        # we don't want to change the root node
        indeces_passed.pop()

        for index in indeces_passed:
            self.data[index] = i
        return i
    
    def sizes(self):
        """Returns sizes of all sets"""
        sizes = []
        for i in range(self.len):
            if self.data[i] < 0:
                sizes.append(abs(self.data[i]))
        return sizes
    
    def __str__(self):
        return self.data.__str__()

