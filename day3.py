def n_max_voltage(banks, n):
    if len(banks) == n:
        return banks
    # find max within window
    max, max_i = '0', 0

    end = len(banks) - (n - 1)
    for i, char in enumerate(banks[:end]):
        if char > max:
            max = char
            max_i = i

    # technically recursive, but conveges very quickly
    if n == 1:
        return max
    identified_subset = banks[max_i + 1:]
    return max + n_max_voltage(identified_subset, n - 1)
    

def max_voltage(bank):
    current_max = '0'
    second_digit = '0'
    for char in bank[:-1]:
        second_digit = max(second_digit, char)
        if char > current_max:
            current_max = char
            second_digit = '0'
    second_digit = max(second_digit, bank[-1])
    return 10 * int(current_max) + int(second_digit)

def day3_solution1(banks):
    total = 0
    for bank in banks:
        total += max_voltage(bank)
    return total

def day3_solution2(banks):
    total = 0
    for bank in banks:
        voltage = n_max_voltage(bank, 12)
        # print(f"Bank: {bank}, Voltage: {voltage}")
        total += int(voltage)
    return total

if __name__ == "__main__":
    from parser import parse_lines

    main_fp = "day3/puzzle.txt"
    banks = parse_lines(main_fp)

    # Puzzle 1 Baby
    baby_fp = "day3/baby.txt"
    baby_banks = parse_lines(baby_fp)
    print("Baby 1 Solution:", day3_solution1(baby_banks))

    # Puzzle 1
    print("Puzzle 1 Solution:", day3_solution1(banks))

    # Puzzle 2 Baby
    print("Baby 2 Solution:", day3_solution2(baby_banks))

    # Puzzle 2
    print("Puzzle 2 Solution:", day3_solution2(banks))