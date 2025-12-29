def process_light(light):
    assert type(light) == str and light[0] == '[' and light[-1] == ']'
    result = []
    for char in light[1:-1]:
        if char == '.':
            result.append(False)
        elif char == '#':
            result.append(True)
        else:
            raise TypeError
    return result

def process_button(button):
    assert type(button) == str and button[0] == '(' and button[-1] == ')'
    button_set = set()
    for x in button[1:-1].split(','):
        button_set.add(int(x))
    return button_set

def fewest_presses(mask, buttons):
    # iteratively apply each button to each new map until we reach mask
    starting_map = [False] * len(mask)
    maps = []
    maps.append(starting_map)
    rounds = 0
    while not mask in maps:
        rounds += 1
        new_maps = []
        for reached_map in maps: # for each map,
            for button in buttons: # apply each button
                new_map = list(reached_map)
                for num in button:
                    new_map[num] = not new_map[num]

                # add to pile of maps, if new
                if new_map not in maps:
                    new_maps.append(new_map) 
        for new_map in new_maps:
            if new_map not in maps:
                maps.append(new_map)

    return rounds

def day10_solution1(lines):
    lights, buttons_str, joltages = [], [], []
    for line in lines:
        words = line.strip().split(' ')
        lights.append(words[0])
        buttons_str.append(words[1:-1])
        joltages.append(words[-1])

    masks = [process_light(light) for light in lights]
    buttons = [[process_button(button) for button in problem_str] for problem_str in buttons_str]
    
    total = 0
    for mask, button in zip(masks, buttons):
        n = fewest_presses(mask, button)
        total += n
    return total

def process_joltage(joltage):
    assert type(joltage) == str and joltage[0] == '{' and joltage[-1] == '}'
    vals = joltage.strip()[1:-1].split(',')
    return np.array([int(x) for x in vals])

def process_button_vector(button, dim):
    new_button = np.zeros(dim)
    for num in button:
        new_button[int(num)] = 1
    return new_button

def remove_index(arr, i):
    """Wayyyy too complicated but works lol"""
    assert type(arr) is np.ndarray
    assert 0 <= i < len(arr)

    new_arr = np.zeros(len(arr) - 1)
    new_idx = 0
    for old_idx, elem in enumerate(arr):
        if old_idx == i:
            continue
        new_arr[new_idx] = elem
        new_idx += 1
    return new_arr

def valid_combinations_helper(buttons, presses, joltage):
    combs = set()
    # base case
    if presses == 1:
        for button in buttons:
            combs.add(button)
        return combs
    
    for button in buttons:
        combs.add()

def valid_combinations(buttons, presses, joltage):
    """yield all combinations of button presses recursively"""
    combs = set()
    
    for _ in range(presses):
        # choose a button


    
def fewest_presses_joltage(joltage, buttons):
    # base case, joltage is one number
    if len(joltage) == 1:
        assert np.array([1]) in buttons
        return joltage[0]
    
    # find smallest element and its index in joltage
    min_i = min(range(len(joltage)), key=joltage.__getitem__) # from https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
    min_joltage = joltage[min_i]
    print(joltage)
    print("smallest", min_joltage, "at", min_i)
    
    # process new joltage to not include min_i index
    new_joltage = remove_index(joltage, min_i)
    print("new joltage", new_joltage, "from", joltage)

    # find all buttons that increment joltage at min_i; also process buttons and relevant_buttons
    new_buttons = []
    new_relevant_buttons = []
    for button in buttons:
        new_button = remove_index(button, min_i)
        if button[min_i]: # if relevant to our coordinate
            new_relevant_buttons.append(new_button)
        else:
            new_buttons.append(new_button)


    # compute all valid n-wise combinations of relevant (new) buttons
    combs = valid_combinations(new_relevant_buttons, min_joltage, new_joltage)

    # recurse on new joltage and buttons
    recurse_val = float('inf')
    for comb in combs:
        adjusted_new_joltage = new_joltage - comb
        recurse_val = min(recurse_val, fewest_presses_joltage(adjusted_new_joltage, new_buttons))
    return min_joltage + recurse_val


def day10_solution2(lines):
    lights, buttons_str, joltages = [], [], []
    for line in lines:
        words = line.strip().split(' ')
        lights.append(words[0])
        buttons_str.append(words[1:-1])
        joltages.append(words[-1])

    joltages = [process_joltage(joltage) for joltage in joltages]
    buttons = [[process_button(button) for button in problem] for problem in buttons_str]

    button_vectors = []
    for i, joltage in enumerate(joltages):
        dim = len(joltage)
        button_vectors.append([process_button_vector(button, dim) for button in buttons[i]])
    
    total = 0
    for joltage, button in zip(joltages, button_vectors):
        n = fewest_presses_joltage(joltage, button)
        # print("adding", n)
        total += n
    return total

if __name__ == "__main__":
    import numpy as np # vectors
    from parser import parse_lines

    # Puzzle 1 Baby
    baby_fp = "day10/baby.txt"
    baby_lines = parse_lines(baby_fp)
    print("Baby 1 Solution:", day10_solution1(baby_lines))

    # Puzzle 1
    main_fp = "day10/puzzle.txt"
    lines = parse_lines(main_fp)
    print("Puzzle 1 Solution:", day10_solution1(lines))

    # Puzzle 2 Baby
    print("Baby 2 Solution:", day10_solution2(baby_lines))

    # Puzzle 2
    # print("Puzzle 2 Solution:", day10_solution2(lines))