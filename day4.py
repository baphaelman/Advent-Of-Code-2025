def print_map(str_map, window):
    x, y = window.x, window.y
    for j in range(y):
        row = ""
        for i in range(x):
            point = Point(i, j)
            row += str_map.get(point, ' ')
        print(row)

def can_pick_up(str_map, point):
    count = 0
    unit_vectors = [Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1),
                    Point(1, 1), Point(1, -1), Point(-1, 1), Point(-1, -1)]
    for u in unit_vectors:
        neighbor = point + u
        if str_map.get(neighbor) == '@':
            count += 1
    return count < 4


def day4_solution1(str_map, window):
    adjusted_map = str_map.copy()
    x, y = window.x, window.y
    count = 0
    for j in range(y):
        for i in range(x):
            point = Point(i, j)
            if str_map[point] == '@' and can_pick_up(str_map, point):
                # print(f"Can pick up at {point.x}, {point.y}")
                adjusted_map[point] = 'x'
                count += 1
    # print_map(adjusted_map, window)
    return count

def find_rolls(str_map, window):
    # returns rolls_removed (list of Points)
    rolls_removed = []
    x, y = window.x, window.y
    for j in range(y):
        for i in range(x):
            point = Point(i, j)
            if str_map[point] == '@' and can_pick_up(str_map, point):
                rolls_removed.append(point)
    return rolls_removed



def day4_solution2(str_map, window):
    has_changed = True
    count = 0
    while has_changed:
        removed_rolls = find_rolls(str_map, window)
        if len(removed_rolls) == 0:
            break
        count += len(removed_rolls)
        for point in removed_rolls:
            str_map[point] = ' '
    return count


if __name__ == "__main__":
    from parser import Point, parse_grid

    main_fp = "day4/puzzle.txt"
    real_map, real_window = parse_grid(main_fp)

    # Puzzle 1 Baby
    baby_fp = "day4/baby.txt"
    baby_map, baby_window = parse_grid(baby_fp)

    # print_map(baby_map, baby_window)
    print(baby_window.x, baby_window.y)
    print("Baby 1 Solution:", day4_solution1(baby_map, baby_window))

    # Puzzle 1
    print("Puzzle 1 Solution:", day4_solution1(real_map, real_window))

    # Puzzle 2 Baby
    print("Baby 2 Solution:", day4_solution2(baby_map, baby_window))

    # Puzzle 2
    print("Puzzle 2 Solution:", day4_solution2(real_map, real_window))