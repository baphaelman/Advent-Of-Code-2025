def day7_solution1(grid):
    # populate tree
    pos = grid.find("S")
    root = Tree(TreeNode(pos.x))
    leaves = [root]
    for r in range(1, grid.y):
        new_leaves = []
        # check if splitter at any new positions
        for leaf in leaves:
            c = leaf.val
            if grid.get(Point(c, r)) == '^':
                count += 1
                if c > 0:
                    leaf.left = TreeNode(c - 1)
                    new_leaves.append(leaf.left)
                if c < grid.x:
                    leaf.right = TreeNode(c + 1)
                    new_leaves.append(leaf.right)
            else:
                new_leaves.append(leaf)
        new_leaves = leaves
    
    return root.count_nodes()

def day7_solution1_better(grid):
    pass

def day7_solution2(grid):
    pass

if __name__ == "__main__":
    from Point import Point
    from TreeNode import TreeNode
    from Tree import Tree
    from BottomUpTree import BottomUpTree

    from parser import parse_grid

    # Puzzle 1 Baby
    baby_fp = "day7/baby.txt"
    baby_grid = parse_grid(baby_fp)
    print(baby_grid)
    print("Baby 1 Solution:", day7_solution1(baby_grid))

    # Puzzle 1
    main_fp = "day7/puzzle.txt"
    grid = parse_grid(main_fp)
    print("Puzzle 1 Solution:", day7_solution1(grid))

    # Puzzle 2 Baby
    # print("Baby 2 Solution:", day7_solution2(baby_grid))

    # Puzzle 2
    # print("Puzzle 2 Solution:", day7_solution2(grid))