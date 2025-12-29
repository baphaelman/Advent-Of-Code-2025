def dayn_solution1(lines):
    pass

def dayn_solution2(lines):
    pass

if __name__ == "__main__":
    from parser import parse_lines

    # Puzzle 1 Baby
    baby_fp = "dayn/baby.txt"
    baby_lines = parse_lines(baby_fp)
    print("Baby 1 Solution:", dayn_solution1(baby_lines))

    # Puzzle 1
    main_fp = "dayn/puzzle.txt"
    lines = parse_lines(main_fp)
    # print("Puzzle 1 Solution:", dayn_solution1(lines))

    # Puzzle 2 Baby
    # print("Baby 2 Solution:", dayn_solution2(baby_lines))

    # Puzzle 2
    # print("Puzzle 2 Solution:", dayn_solution2(lines))