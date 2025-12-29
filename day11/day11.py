def day11_solution1(d):
    g = Day11Graph.parse_dict(d)
    i, j = g.name_to_i["you"], g.name_to_i["out"]
    return g.count_paths(i ,j)

def day11_solution2(d):
    g = Day11Graph.parse_dict(d)
    i, j = g.name_to_i["svr"], g.name_to_i["out"]
    a, b = g.name_to_i["dac"], g.name_to_i["fft"]
    return g.count_paths_with_visits(i, j, [a, b])
def parse_dict(fp):
    dict = {}
    with open(fp, 'r') as file:
        lines = [line.strip().split(' ') for line in file.readlines()]
        for line in lines:
            print(line)
            root = line[0][:-1]
            dict[root] = []
            for address in line[1:]:
                dict[root].append(address)
    return dict


if __name__ == "__main__":
    from Day11Graph import Day11Graph, Day11Node
    # from parser import parse_lines

    # Puzzle 1 Baby
    baby_fp = "baby.txt"
    baby_dict = parse_dict(baby_fp)
    print("Baby 1 Solution:", day11_solution1(baby_dict))

    # Puzzle 1
    main_fp = "puzzle.txt"
    main_dict = parse_dict(main_fp)
    print("Puzzle 1 Solution:", day11_solution1(main_dict))

    # Puzzle 2 Baby
    # print("Baby 2 Solution:", day11_solution2(baby_lines))

    # Puzzle 2
    # print("Puzzle 2 Solution:", day11_solution2(lines))