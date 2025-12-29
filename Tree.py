from TreeNode import TreeNode
class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def count_nodes(self):
        count = 1
        count += self.left.count_nodes()
        return count + self.right.count_nodes()