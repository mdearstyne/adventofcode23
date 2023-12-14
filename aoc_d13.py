import numpy as np
from itertools import combinations

d = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''

with open(r"C:\Users\dears002\Documents\adventofcode\input_d13.txt") as f:
    d = f.read()
f.close()

d = d.replace('\n', '*')
d = d.split('*')

d = d.split('\n')
p1 = d[0:7]
p2 = d[7:]

patterns = []

temp_pattern = []
for e in d:
    if e != '':
        temp_pattern.append(e)
    else:
        patterns.append(temp_pattern)
        temp_pattern = []

patterns.append(temp_pattern)

def find_mirror(p):
    first_row = 1
    last_row = len(p)

    end_rows = []
    middle_rows = []

    # make a list of all matching rows
    # if more than 2 rows match, expand them to include all combinations
    matches = []
    for e in set(p):
        match = [i+1 for i, v in enumerate(p) if v == e]
        if len(match) > 2:
            expanded_matches = list(combinations(match, r=2))
            expanded_matches = [list(e) for e in expanded_matches]
            matches.extend(expanded_matches)
        elif len(match) == 2:
            matches.append(match)
    print('Matches: ', str(matches))

    # separate the matches into end rows and middle rows
    for match in matches:
        # the difference between the end row and the match must be odd
        if ((first_row in match) or (last_row in match)) and ((match[1]-match[0]) % 2 != 0):
            end_rows.append(tuple(match))
        elif (first_row not in match) and (last_row not in match):
            middle_rows.append(tuple(match))
        else:
            print('Rows discarded: ', str(match))
    
    if len(end_rows) >= 1:
        print('End rows: ', str(end_rows))
    if len(middle_rows) >= 1:
        print('Middle rows:', str(middle_rows))
    
    # if there are no end rows, return None
    if len(end_rows) == 0:
        print('Reflection does not extend to end of pattern')
        return None
    #elif len(end_rows) > 1:
        #print('WARNING: more than one possible end row')
    
    if len(middle_rows) == 0:
        middle_rows = end_rows
    
    row_differences = [match[1]-match[0] for match in middle_rows]

    if 1 not in row_differences:
        print('WARNING: No adjacent rows - mirror could be only matching pair')
        #return None
    
    #mirror_candidate = middle_rows[row_differences.index(1)]
    #if middle_rows == end_rows:
        #return end_rows[0][0]
    
    # Check if middle rows are contained by end_row
    for end_row in end_rows:
        print('Checking for all reflections between ' + str(end_row))
        start = end_row[0]
        stop = end_row[1]
        midpoint = int(((end_row[1]-end_row[0])/2)+end_row[0])
        going_up = tuple(range(start+1, midpoint+1))
        going_down = tuple(range(stop-1, midpoint, -1))
        up_and_down = tuple(zip(going_up, going_down))
        up_and_down = [tuple(sorted(e)) for e in up_and_down]

        if len(up_and_down) == 0:
            # mirror is on the end, return first element of end row
            print('Mirror is on the end')
            return end_row[0]

        elif set(up_and_down).issubset(middle_rows):
            print('Mirror is ' + str(midpoint) + ' rows/columns down')
            return midpoint
        else:
            print('Not all rows between end are contained')
            print('Middle rows should include:', str(up_and_down))
            next
    
    print('No mirror found')
    return None

def transpose_pattern(p):
    new_p = []
    for l in p:
        new_p.append([e for e in l])

    a = np.array(new_p)
    aT = a.T
    pT = aT.tolist()

    new_p = []
    for l in pT:
        new_p.append(''.join(l))
    
    return new_p

def reflection_sum(p):
    a = find_mirror(p)
    if a:
        return a*100
    else:
        print('Transposing, finding new mirror')
        b = find_mirror(transpose_pattern(p))
        if b:
            return b
        else:
            print('Still no mirror found')

totals = []
for i in range(100):
    print('Pattern ' + str(i))

    new_p = []
    for l in patterns[i]:
        new_p.append([e for e in l])
    print(np.array(new_p))

    totals.append(reflection_sum(patterns[i]))
sum(totals)

