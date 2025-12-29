def func_from_sig(s):
    if s == '+':
        return operator.add
    elif s == '*':
        return operator.mul
    
def do_problem(func, nums):
    curr = nums[0]
    for num in nums[1:]:
        # print(curr, func, num)
        curr = func(curr, num)
    return curr

def day6_solution1(lines):
    first_line = [x for x in lines[0].split(' ') if x]
    num_problems = len(first_line)
    # initiate map
    problems = {}
    for n in range(num_problems):
        problems[n] = []
    
    # populate maps
    functions = {}
    for i in range(len(lines)):
        nums = [x for x in lines[i].split(' ') if x != '']
        
        for j, num in enumerate(nums):
            if num in sigs: # for function handles
                func = func_from_sig(num)
                functions[j] = func
            else:
                problems[j].append(int(num))
    # print(len(functions))
    # print(len(problems))

    # do problems
    total = 0
    for i in range(len(problems)):
        total += do_problem(functions[i], problems[i])
    return total

def arr_to_int(arr_num: str):
    if not arr_num:
        return 0
    curr = int(arr_num[0])
    for s in arr_num[1:]:
        curr = curr * 10 + int(s)
    return curr


def day6_solution2(lines):
    # iterate through all lines at once, building each problem as we go
    handles = lines[-1]
    num_lines = lines[:-1]
    #print(num_lines)

    problems = {} # indexed by
    functions = {} # same pointer vv
    i = 0
    problems[i] = []
    for char_i in range(len(num_lines[0]) - 1, -1, -1):
        raw_num = [line[char_i] for line in num_lines]
        arr_num = [x for x in raw_num if x != ' ']
        num = arr_to_int(arr_num)
        #print(raw_num, arr_num, num)
        if not num: # end of word
            functions[i] = func_from_sig(handles[char_i + 1])
            #print("adding", functions[i], "at", i)
            i += 1
            problems[i] = []
        else:
            problems[i].append(num)
    functions[i] = func_from_sig(handles[0])

    #print(problems)
    #print(functions)

    # do math lol
    total = 0
    for j in range(i + 1):
        plus = do_problem(functions[j], problems[j])
        # print("adding", plus)
        total += plus
    return total
            


if __name__ == "__main__":
    import operator
    from parser import parse_lines

    global sigs
    sigs = ['+', '*']

    # Puzzle 1 Baby
    baby_fp = "day6/baby.txt"
    baby_lines = parse_lines(baby_fp, raw=True)
    print("Baby 1 Solution:", day6_solution1(baby_lines))

    # Puzzle 1
    main_fp = "day6/puzzle.txt"
    lines = parse_lines(main_fp, raw=True)
    print("Puzzle 1 Solution:", day6_solution1(lines))

    # Puzzle 2 Baby
    print("Baby 2 Solution:", day6_solution2(baby_lines))

    # Puzzle 2
    print("Puzzle 2 Solution:", day6_solution2(lines))