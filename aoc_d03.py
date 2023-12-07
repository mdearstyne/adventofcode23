import re

test_data = '''467..114..
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

test_data = test_data.split('\n')

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
#sums = []
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
    locs = {}
    dups = {}
    for m in iter:
        if m.group() not in locs:
            locs[m.group()] = m.span()
        else:
            dups[m.group()] = m.span()
            #raise Exception('DUPLICATE KEY')
    #print(locs)
    #line_dict[i] = locs
    #i += 1
    for k, v in locs.items():
        print('Current iteration: ' + k,v)
        if v[0] == 0:
            prev_index = v[0]
        else:
            prev_index = v[0]-1
        #if v[1] == 139:
            #next_index = v[1]
        #else:
        #if v[1] == 140:
        #    next_index = v[1]
        #else:
        next_index = v[1]+1
        prev_line_substr = prev_line[prev_index:next_index]
        cur_line_substr = line[prev_index:next_index]
        next_line_substr = next_line[prev_index:next_index]
        print(prev_line_substr)
        print(cur_line_substr)
        print(next_line_substr)
        block = set(prev_line_substr + cur_line_substr + next_line_substr)
        if set.intersection(block, symbols):
            print(k + ' is adjacent to ' + ''.join(set.intersection(block, symbols)))
            total_sum += int(k)
            #linesum += int(k)
            print('Total sum is ' + str(total_sum))
            #print('Total sum is ' + str(linesum))
        else:
            print(k + ' is not symbol adjacent - not added')
            print('Total sum is ' + str(total_sum))
            #print('Total sum is ' + str(linesum))
    for k, v in dups.items():
        print('Current iteration: ' + k,v)
        if v[0] == 0:
            prev_index = v[0]
        else:
            prev_index = v[0]-1
        #if v[1] == 139:
            #next_index = v[1]
        #else:
        #if v[1] == 140:
        #    next_index = v[1]
        #else:
        next_index = v[1]+1
        prev_line_substr = prev_line[prev_index:next_index]
        cur_line_substr = line[prev_index:next_index]
        next_line_substr = next_line[prev_index:next_index]
        print(prev_line_substr)
        print(cur_line_substr)
        print(next_line_substr)
        block = set(prev_line_substr + cur_line_substr + next_line_substr)
        if set.intersection(block, symbols):
            print(k + ' is adjacent to ' + ''.join(set.intersection(block, symbols)))
            total_sum += int(k)
            #linesum += int(k)
            print('Total sum is ' + str(total_sum))
            #print('Total sum is ' + str(linesum))
        else:
            print(k + ' is not symbol adjacent - not added')
            print('Total sum is ' + str(total_sum))
            #print('Total sum is ' + str(linesum))
    #sums.append(linesum)

# Part 2
total_sum = 0
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
        locs.append([m.group(), m.span()])
    
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

        print(prev_line_substr)
        print(cur_line_substr)
        print(next_line_substr)

        block = [prev_line_substr, cur_line_substr, next_line_substr]

        for j in range(len(block)):
            if '*' in block[j]:
                print('Found * in line ' + str(i-1+j))


        if set.intersection(block, symbols):
            print(k + ' is adjacent to ' + ''.join(set.intersection(block, symbols)))
            total_sum += int(k)
            #linesum += int(k)
            print('Total sum is ' + str(total_sum))
            #print('Total sum is ' + str(linesum))
        else:
            print(k + ' is not symbol adjacent - not added')
            print('Total sum is ' + str(total_sum))
            #print('Total sum is ' + str(linesum))
