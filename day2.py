def get_factors(n):
    """
    Generates a list of all factors for a given integer n.
    """
    factors = []
    # Iterate from 1 to n (inclusive)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def is_double(s):
    l = len(s)
    first, last = s[:l // 2], s[l // 2:]
    return first == last

def invalid_doubles(nums_range):
    invalids = []

    start, end = map(int, nums_range.split('-'))
    for id in range(start, end + 1):
        str_id = str(id)
        if is_double(str_id):
            invalids.append(id)
    return invalids

def day2_solution1(ranges):
    total = 0
    for range in ranges:
        invalids = invalid_doubles(range)
        total += sum(invalids)
    return total

def is_repeating_window(s):
    l = len(s)
    window_sizes = get_factors(l)
    for n in window_sizes:
        windows = [s[i:i+n] for i in range(0, len(s), n)]
        if len(set(windows)) == 1:
            return True
    return False

def factor_invalics(id_range):
    invalids = []

    start, end = map(int, id_range.split('-'))
    for id in range(start, end + 1):
        str_id = str(id)
        if is_repeating_window(str_id):
            invalids.append(id)
    return invalids

def day2_solution2(id_ranges):
    total = 0
    for id_range in id_ranges:
        invalids = factor_invalics(id_range)
        total += sum(invalids)
    return total

if __name__ == "__main__":
    from parser import parse_comma_line
    main_fp = "day2/puzzle.txt"
    ranges = parse_comma_line(main_fp)

    # Baby 1
    baby_fp = "day2/2baby1.txt"
    baby_ranges = parse_comma_line(baby_fp)

    print("Baby 1 Solution:", day2_solution1(baby_ranges))

    
    # Puzzle 1
    print("Puzzle 1 Solution:", day2_solution1(ranges))

    # Puzzle 2 Baby
    print("Baby 2 Solution:", day2_solution2(baby_ranges))

    # Puzzle 2
    print("Puzzle 2 Solution:", day2_solution2(ranges))