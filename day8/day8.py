def day8_solution1(coords, connections):
    g = Graph.parse_coords(coords)
    for _ in range(connections):
        # print("finding next closest edge:", i)
        g.connect_closest()
    circuits = g.circuit_sizes()
    circuits.sort(reverse=True)
    return circuits[0] * circuits[1] * circuits[2]

def day8_solution2(coords):
    g: Graph = Graph.parse_coords(coords)
    e = g.last_connection()
    n1, n2 = e.node_a, e.node_b
    return n1.x * n2.x

def parse_coords(filepath):
    with open(filepath, 'r') as f:
        str_coords = [line.strip().split(',') for line in f.readlines()]
        int_coords = [[int(num) for num in coord] for coord in str_coords]
    return int_coords

if __name__ == "__main__":
    from Graph import Graph
    
    # Puzzle 1 Baby
    baby_fp = "baby.txt"
    baby_coords = parse_coords(baby_fp)
    print("Baby 1 Solution:", day8_solution1(baby_coords, 10))

    # Puzzle 1
    main_fp = "puzzle.txt"
    coords = parse_coords(main_fp)
    print("Puzzle 1 Solution:", day8_solution1(coords, 1000))

    # Puzzle 2 Baby
    print("Baby 2 Solution:", day8_solution2(baby_coords))

    # Puzzle 2
    print("Puzzle 2 Solution:", day8_solution2(coords))