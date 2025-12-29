from Grid import Grid
from Point import Point

class BottomUpTree:
    def __init__(self):
        self.original_leaves: dict[int, BottomUpNode] = {}
        self.active_nodes: dict[int, BottomUpNode] = {}
        self.grid = None # to be filled in by parse_grid()
        self.root = None # to be filled in by parse_grid()

        """
        # populate data structures
        for i in range(self.grid.x):
            n = BottomUpNode
            self.original_leaves[i] = n
        """
    
    def parse_grid(grid: Grid):
        """Takes in grid from a 'filled-in' part 1"""
        print(grid)
        t = BottomUpTree()
        grid.tachyon_fill()
        t.grid = grid

        matrix = t.clean_grid(t.grid)
        
        # parse first row manually to populate data structures
        first_row = matrix[0]
        for i, elem in enumerate(first_row):
            assert elem in [0, 2]
            n = BottomUpNode(0, leaf=True)
            if elem == 2:
                t.original_leaves[i] = n
            t.active_nodes[i] = n

        # parse remaining rows iteratively
        x = t.grid.x
        for row_idx, row in enumerate(matrix[1:-1]):
            print(row)
            for i, elem in enumerate(row):
                if elem == 1:
                    # replace current active node with new
                    new_n = BottomUpNode(row_idx + 1)
                    t.active_nodes[i] = new_n

                    # update parents appropriately
                    if i > 0:
                        t.active_nodes[i - 1].parents.append(new_n)
                    if i < x - 1:
                        t.active_nodes[i + 1].parents.append(new_n)
        
        # one final tratment for the beam emittor
        i = t.grid.find('S').x
        t.root = BottomUpNode(len(matrix))
        t.active_nodes[i] = t.root

        # update parents appropriately
        if i > 0:
            t.active_nodes[i - 1].parents.append(t.root)
        if i < x - 1:
            t.active_nodes[i + 1].parents.append(t.root)
        return t
    
    def count_paths(self):
        children = set(self.original_leaves.values())
        all_parents = set()
        for child in children:
            all_parents.update(child.parents)

        generation = 0
        while len(all_parents) > 1:
        # for _ in range(10):
            print(len(all_parents))
            print(all_parents)
            print("generation", generation)
            # transfer values
            while children:
                child = children.pop()
                v = child.val
                for parent in child.parents:
                    parent.val += v
            
            # update children and all_parents for next generation
            generation += 1
            remove = set()
            for parent in all_parents:
                if parent.generation == generation:
                    remove.add(parent)
                    children.add(parent)

            for r in remove:
                all_parents.remove(r)
                
        # we expect len(children) == 1
        print("length of all_parents", len(all_parents))
        return 0
    
    """
    def count_paths(self):
        # Counting all paths from root to leaves
        # set up children and parents to enter loop
        children = self.original_leaves.values()
        parents = set()
        for child in children:
            # print(child.parents)
            parents.update(child.parents)
        
        generation = 1
        while len(parents) > 1:
            for parent in parents:
                if parent.generation != generation:
                    continue
                print("processing parent:", parent)



            children = parents
            parents = set()
            for child in children:
                parents.update(child.parents)
            # print("new parents:", parents)
        return parents.pop().val
        
        """

    def clean_grid(self, grid: Grid):
        """
        Returns nice bottom-up matrix from Grid
        0: empty, 1: splitter, 2: beam
        """
        matrix = []
        prev_row = None
        y = grid.y
        for i in range(y - 1, -1, -1):
            row = grid.get_row(i)
            nums = list(map(self.tachyon_converter, row))
            if (prev_row and prev_row == row): # or ((1 not in nums) and i != y - 1): # skip directly repeating rows
                continue
            print(f"{y - 1 - i}:", row, nums)
            matrix.append(nums)

            prev_row = row
        return matrix
        
    def tachyon_converter(self, c):
        if c == '.':
            return 0
        elif c == '^':
            return 1
        elif c == '|':
            return 2
        elif c == 'S':
            return 3
        raise TypeError("only chars supported are ., ^, |, and S")


class BottomUpNode:
        def __init__(self, generation: int, leaf=False):
            self.parents: list["BottomUpNode"] = []
            self.generation: int = generation
            if leaf:
                self.val: int = 1
            else:
                self.val: int = 0
        
        def __repr__(self):
            return f"Node(val={self.val}, gen={self.generation})"

if __name__ == "__main__":
    from parser import parse_grid

    baby_fp = 'day7/baby.txt'
    baby_grid = parse_grid(baby_fp)
    t = BottomUpTree.parse_grid(baby_grid)
    print(t.grid)
    a = t.count_paths()
    print("Answer:", a)