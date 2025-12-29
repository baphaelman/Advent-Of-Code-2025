def day8_solution1(coords, connections):
    g = Graph.parse_coords(coords)
    for i in range(connections):
        print("finding next closest edge:", i)
        g.connect_closest()
    circuits = g.largest_circuits()
    return circuits[0] * circuits[1] * circuits[2]

def day8_solution1_better(coords, connections):
    g = BetterGraph.parse_coords(coords)
    for i in range(connections):
        print("finding next closest edge:", i)
        g.connect_closest()
    return g.three_largest_circuits()

def day8_solution1_betterer(coords, connections):
    g = Graph.parse_coords(coords)
    g.connect_n_smallest(connections)
    nums = g.largest_circuits()
    return nums[0] * nums[1] * nums[2]

def day8_solution2(coords):
    step = 1000
    g = Graph.parse_coords(coords)
    g_copy = g.copy()
    while len(g.largest_circuits()) > 1:
        g.connect_n_smallest(step)
        print("connected", step)
        print(g.largest_circuits())
        if len(g.largest_circuits()) == 1:
            # converges in the last batch
            print("convergence passed")
            break
        g_copy = g.copy()

    # rollback to before convergence
    g = g_copy
    e = g.final_connection()
    return e[0].x * e[1].x

def parse_coords(filepath):
    with open(filepath, 'r') as f:
        str_coords = [line.strip().split(',') for line in f.readlines()]
        int_coords = [[int(num) for num in coord] for coord in str_coords]
    return int_coords

if __name__ == "__main__":
    from BetterGraph import BetterGraph
    from day8.OldGraph import Graph
    
    # Puzzle 1 Baby
    baby_fp = "baby.txt"
    baby_coords = parse_coords(baby_fp)
    print("Baby 1 Solution:", day8_solution1(baby_coords, 10))
    print("Baby 1 Solution:", day8_solution1_betterer(baby_coords, 10))

    # Puzzle 1
    main_fp = "puzzle.txt"
    coords = parse_coords(main_fp)
    # print("Puzzle 1 Solution:", day8_solution1(coords, 1000))
    print("Puzzle 1 Solution:", day8_solution1_betterer(coords, 1000))

    # Puzzle 2 Baby
    print("Baby 2 Solution:", day8_solution2(baby_coords))

    # Puzzle 2
    print("Puzzle 2 Solution:", day8_solution2(coords))