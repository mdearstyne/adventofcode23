
# Part 1

# Load in data
with open("C:/Users/dears002/Documents/adventofcode/input_d08.txt") as f:
    d = f.read()
f.close()

# Clean it up
d = d.split('\n')
rl = d[0]
d = d[2:-1]

# Turn it into a dictionary with starting node as the value and destination nodes as the key
desert_map = {}

for i in range(len(d)):
    node, cord = d[i].split(' = ')
    cord = cord.replace('(', '')
    cord = cord.replace(')', '')
    cord = cord.split(', ')
    #cord = cord.split(', ')
    desert_map[node] = cord

# Define a count steps function to determine how many steps it will take to arrive at 'ZZZ'.
def count_steps(dmap, starting_node, rl):
    count = 0
    while starting_node != 'ZZZ':
        #print('Current node: ' + starting_node)
        for turn in rl:
            if turn == 'R':
                #print('Turn right')
                starting_node = dmap[starting_node][1]
                #print('Next node: ' + starting_node)
            elif turn == 'L':
                #print('Turn left')
                starting_node = dmap[starting_node][0]
                #print('Next node: ' + starting_node)
            count+=1
            #print('Current count: ' + str(count))
    return count

count_steps(desert_map, 'AAA', rl) # 20513

# Part 2

# Get the starting nodes that end in 'A'
starting_nodes = []
for key in desert_map.keys():
    if key[-1] == 'A':
        starting_nodes.append(key)

# Modify count steps to accept a list of nodes, and stop when arriving at a node that ends in 'Z'

def new_count_steps(dmap, starting_nodes, rl):
    node_counts = {}
    for starting_node in starting_nodes:
        #print(starting_node)
        count=0
        #print('Current node: ' + starting_node)
        while starting_node[-1] != 'Z':
            for turn in rl:
                    if turn == 'R':
                        #print('Turn right')
                        starting_node = dmap[starting_node][1]
                        #print('Next node: ' + starting_node)
                    elif turn == 'L':
                        #print('Turn left')
                        starting_node = dmap[starting_node][0]
                        #print('Next node: ' + starting_node)
                    count+=1
        #print('Next node: ' + starting_node)
        #print('Count: ' + str(count))
        node_counts[starting_node] = count
    return node_counts

m = new_count_steps(desert_map, starting_nodes, rl)

# It's not immediately obvious that it has to be this way, BUT it turns out that this list is cyclical!
# Look at how many steps it takes for just a single node to arrive at a node ending in Z, the first hundred times through the list.

def count_single_node(dmap, starting_node, rl):
    count=0
    counts = []
    while len(counts) < 100:
        for turn in rl:
            if turn == 'R':
                #print('Turn right')
                starting_node = dmap[starting_node][1]
                #print('Next node: ' + starting_node)
            elif turn == 'L':
                #print('Turn left')
                starting_node = dmap[starting_node][0]
                #print('Next node: ' + starting_node)
            count+=1
            if starting_node[-1] == 'Z':
                counts.append(count)
    return counts

count_single_node(desert_map, starting_nodes[0], rl)

# It takes the same count each time to arrive at a node ending in Z. That means that the solution to this is just to get the least common multiple of all the counts of each of the nodes!
# This saves us from having to run through the entire list for each node, which will take hours.

new_count_steps(desert_map, list(m.keys()), rl)
multiples = [v for v in m.values()]

import math
math.lcm(*multiples) # 15995167053923

    
