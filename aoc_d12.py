
import re
from itertools import product

""" d = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1''' """

# prepare data
with open(r"C:\Users\dears002\Documents\adventofcode\input_d12.txt") as f:
    d = f.read()
f.close()


d = d.split('\n')
d = d[:-1]
d = [s.split(' ') for s in d]

# write function to get possible springs
def get_springs(r):

    # set element in row
    e = r[0]

    # create regex pattern for matching later
    e_pattern = e.replace('.', '\.')
    e_pattern = e_pattern.replace('?', '[#.]')
 
    # get the lengths of consecutive damaged springs
    l = r[1].split(',')
    l = [int(n) for n in l]
    
    # get the total number of damanged springs, and the number of consecutive groups
    total_springs = sum(l)
    groups_of_springs = len(l)

    # get the cartesion product of the two symbols, with length of all the springs, for iterating
    possibilities = list(product('.#', repeat=len(e)))

    new_possibilities = []
    for p in possibilities:
        p = ''.join(p)

        # if the number of springs in the current possibility matches the total number of damaged springs
        # and if the number of groups of consecutive springs matches the pattern, continue
        if p.count('#') == total_springs and len(re.findall('\#+', p)) == groups_of_springs:
            # check if the current possibility matches the pattern
            if re.fullmatch(e_pattern, p):
                # check if the length of each of the groups matches the expected lengths, append the possibiltiy to the new list
                if [len(m) for m in re.findall('#+', p)] == l:
                    #print('Current possibility: ' + p)
                    #print('Number of # in possibility matches total possible: ',  str(total_springs))
                    #print('Current possibility matches pattern: ', e_pattern)
                    #print('Grouping of possibility matches pattern: ', str(l))
                    #print('---')
                    new_possibilities.append(p)
    #print('Percent reduction: ' + str(round((len(possibilities)-len(new_possibilities))/len(possibilities)*100)) + '%')    
    #print(new_possibilities)
    return len(new_possibilities)

num_poss = []
for r in d:
    num_poss.append(get_springs(r))
sum(num_poss)

# Part 2

# expand the lists
new_d = []
for i in range(len(d)):
    r = d[i]
    e = r[0]
    l = r[1]
    new_e = ((e+'?')*5)[:-1]
    new_l = ((l+',')*5)[:-1]
    new_d.append([new_e, new_l])


new_d # not happening



