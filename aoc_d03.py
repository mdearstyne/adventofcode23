import re

d = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
2........1'''

d = d.split('\n')

with open(r'C:\Users\dears002\Documents\adventofcode\input_d03.txt') as f:
    d = f.readlines()
f.close()

for i in range(len(d)):
    d[i] = d[i].strip()

symbols = set()
for line in d:
    for char in line:
        if not char.isdigit() and char != '.' and char != '\n':
            symbols.add(char)

total_sum = 0

parts = []

for i in range(len(d)):
    print('Line ' + str(i))
    line = d[i]
    if i == 0:
        prev_line = '.'*len(line)
    else:
        prev_line = d[i-1]
    if i == len(d)-1:
        next_line = '.'*len(line)
    else:
        next_line = d[i+1]

    iter = re.finditer('[0-9]+', line)
    locs = []

    for m in iter:
        print(m.group())
        locs.append((m.group(), m.span()))

    for k, v in locs:
        print('Current iteration: ' + k,v)
        if v[0] == 0:
            prev_index = v[0]
        else:
            prev_index = v[0]-1
        
        next_index = v[1]+1
        prev_line_substr = prev_line[prev_index:next_index]
        cur_line_substr = line[prev_index:next_index]
        next_line_substr = next_line[prev_index:next_index]

        print(prev_line_substr + '\n' + cur_line_substr + '\n' + next_line_substr)
        block = set(prev_line_substr + cur_line_substr + next_line_substr)

        if set.intersection(block, symbols):
            print(k + ' is adjacent to ' + ''.join(set.intersection(block, symbols)))
            parts.append((i, k, v))
            total_sum += int(k)
            print('Total sum is ' + str(total_sum))
        else:
            print(k + ' is not symbol adjacent - not added')
            print('Total sum is ' + str(total_sum))

# Part 2
parts
gears = []

for i in range(len(d)):
    line = d[i]
    iter = re.finditer(r'\*', line)
    for m in iter:
        gears.append((i, m.span()))

double_gears = []
gear_ratios = []
for g in gears:
    vals = []
    part_count = 0
    gear_line = g[0]
    gear_index = g[1][0]
    prev_line = gear_line-1
    next_line = gear_line+1
    temp_parts = [e for e in parts if prev_line <= e[0] <= next_line]
    for p in temp_parts:
        parts_index = range(p[2][0]-1, p[2][1]+1)
        if gear_index in parts_index:
            print('Found gear')
            part_count +=1
            vals.append(p[1])
    if part_count == 2:
        print('Found double gear')
        double_gears.append(g)
        gear_ratio = int(vals[0]) * int(vals[1])
        gear_ratios.append(gear_ratio)

double_gears
gear_ratios
sum(gear_ratios)


