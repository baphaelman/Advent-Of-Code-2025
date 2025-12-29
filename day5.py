def day5_solution1(lines):
    # split into ranges and ingredients
    starts = []
    ends = []
    ingredients = set()
    count = 0
    for line in lines:
        if '-' in line:
            start_str, end_str = line.split('-')
            start = int(start_str)
            end = int(end_str)

            starts.append(start)
            ends.append(end)
        elif not line:
            continue
        else:
            ingredients.add(int(line))
    
    for ingredient in ingredients:
        # check if in any range
        for i, start in enumerate(starts):
            if start <= ingredient <= ends[i]:
                count += 1
                break

    return count

def day5_solution2(lines):
    # make ranges
    starts = []
    ends = []
    count = 0
    for line in lines:
        if '-' in line:
            start_str, end_str = line.split('-')
            start = int(start_str)
            end = int(end_str)

            starts.append(start)
            ends.append(end)
        elif not line:
            break
        else:
            break

    zipped = zip(starts, ends)
    sorted_by_start = sorted(zipped, key=lambda x: x[0])
    print(sorted_by_start)

    print(sorted_by_start)
    for range_i in range(len(sorted_by_start)):
        # choose range
        start, end = sorted_by_start[range_i][0], sorted_by_start[range_i][1]
        print("incrementing for", range_i, "from", start, end)
        count += 1
    
    # alter starts and ends to avoid double counting
    for range_j in range(range_i + 1, len(sorted_by_start)):
        print(range_j)
        start2, end2 = sorted_by_start[range_j][0], sorted_by_start[range_j][1]
        if start2 > end:
            print("skipped", start2, end2)
            break
        elif end2 <= end:
            sorted_by_start[range_j][1] = sorted_by_start[range_j][0] # neutralize skipped ranges
            print("neutralized", start2, end2)
        else:
            start2_original = sorted_by_start[range_j][0]
            sorted_by_start[range_j][0] = end
            print("shifted", start2_original, "->", start2, end2)

    return count

def master_debator(lines):
    # make ranges
    starts = []
    ends = []
    for line in lines:
        if '-' in line:
            start_str, end_str = line.split('-')
            start = int(start_str)
            end = int(end_str)

            starts.append(start)
            ends.append(end)
        elif not line:
            break
        else:
            break

    zipped = zip(starts, ends)
    sorted_by_start = sorted(zipped, key=lambda x: x[0])
    print(sorted_by_start)

    count = 0
    # ranges
    # values in ranges
    # add all values in a range
    # check subsequent ranges and adjust each until there is no overlap
    list_rs = [[r[0], r[1]] for r in sorted_by_start]
    neutralized = set()
    rs_len = len(list_rs)
    for i in range(rs_len): # for each range
        if i in neutralized: # skip skipped ranges
            continue
        r = list_rs[i]
        # print("r", r)
        start, end = r[0], r[1]
        count += end - start + 1 # add all values
        # print("current count", count)

        for j in range(i + 1, rs_len): # fix next ranges appropriately
            r2 = list_rs[j]
            print("r2", r2)
            start2, end2 = r2[0], r2[1]
            
            if start2 > end:
                # print("skipped", start2, end2, "from", start, end)
                break
            elif end2 <= end:
                neutralized.add(j)
                # print("neutralized", start2, end2)
            else:
                start2_original = r2[0]
                r2[0] = end + 1
                print("shifted", start2_original, "->", start2, end2)
    return count


        




if __name__ == "__main__":
    from parser import parse_lines

    main_fp = "day5/puzzle.txt"
    lines = parse_lines(main_fp)


    # Puzzle 1 Baby
    baby_fp = "day5/baby.txt"
    baby_lines = parse_lines(baby_fp)

    print("Baby 1 Solution:", day5_solution1(baby_lines))

    # Puzzle 1
    print("Puzzle 1 Solution:", day5_solution1(lines))

    # Puzzle 2 Baby
    # print("Baby 2 Solution:", day5_solution2(baby_lines))
    print("baby master debating", master_debator(baby_lines))

    # Puzzle 2
    print("Puzzle 2 Solution:", master_debator(lines))