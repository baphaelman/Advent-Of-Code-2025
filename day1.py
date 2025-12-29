from parser import parse_lines

def day1_solution1(input):
    count = 0
    current = 50
    for i, rotation in enumerate(input):
        direction, distance = rotation[0], rotation[1:]
        # print(rotation, direction, distance)
        if direction == 'R':
            current += int(distance)
        elif direction == 'L':
            current -= int(distance)
        else:
            raise ValueError(f"Invalid direction '{direction}' in rotation '{rotation}' at line {i+1}")
        current %= 100
        # print(current)
        if current == 0:
            count += 1
    return count

def day1_solution2(input):
    count = 0
    current = 50
    for rotation in input:
        direction, distance = rotation[0], rotation[1:]

        # calculate displacement
        if direction == 'R':
            step = 1
        elif direction == 'L':
            step = -1
        else:
            raise ValueError(f"Invalid direction '{direction}' in rotation '{rotation}'")

        for _ in range(abs(int(distance))):
            current = (current + step) % 100
            if current == 0:
                count += 1
        # print(current)
    return count

if __name__ == "__main__":
    main_fp = "day1/1puzzle1.txt"
    rotations = parse_lines(main_fp)

    # Baby 1main_fp
    baby_fp = "day1/1baby1.txt"
    baby_rotations = parse_lines(baby_fp)
    print("Baby 1 Solution:", day1_solution1(baby_rotations))

    # Puzzle 1
    print("Puzzle 1 Solution:", day1_solution1(rotations))

    # Puzzle 2 Baby
    print("Baby 2 Solution:", day1_solution2(baby_rotations))

    # Puzzle 2
    print("Puzzle 2 Solution:", day1_solution2(rotations))