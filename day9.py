def day9_solution1(coords):
    g = BetterGraph.parse_coords(coords)
    e = g.largest_edge()
    a, b = e.node_a, e.node_b
    print("largest edge between", a, b)
    dx, dy = abs(a.x - b.x) + 1, abs(a.y - b.y) + 1
    return dx * dy


def day9_solution2(lines):
    pass

def parse_coords(filepath):
    with open(filepath, 'r') as f:
        str_coords = [line.strip().split(',') for line in f.readlines()]
        int_coords = [[int(num) for num in coord] for coord in str_coords]
    return int_coords

if __name__ == "__main__":
    from BetterGraph import BetterGraph

    # Puzzle 1 Baby
    baby_fp = "day9/baby.txt"
    baby_coords = parse_coords(baby_fp)
    print("Baby 1 Solution:", day9_solution1(baby_coords))

    # Puzzle 1
    main_fp = "day9/puzzle.txt"
    coords = parse_coords(main_fp)
    print("Puzzle 1 Solution:", day9_solution1(coords))

    # Puzzle 2 Baby
    # print("Baby 2 Solution:", day9_solution2(baby_coords))

    # Puzzle 2
    # print("Puzzle 2 Solution:", day9_solution2(coords))