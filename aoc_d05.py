d = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

with open(r"C:\Users\dears002\Documents\adventofcode\input_d05.txt") as f:
    d = f.read()
f.close()

d = d.split('\n')
d = d[:-1]

seeds = d[0].split(': ')[1].split(' ')
seeds = [int(n) for n in seeds]
seeds

maps = {}
for i in range(1, len(d)):
    splits = d[i].split(' ')
    if len(splits)==2:
        mkey = splits[0]
        maps[mkey] = {'destination_start': [], 'source_start': [], 'range_length': []}
    elif len(splits)==3:
        a, b, c = splits
        maps[mkey]['destination_start'].append(int(a))
        maps[mkey]['source_start'].append(int(b))
        maps[mkey]['range_length'].append(int(c))

def seed_to_location(seed):
    for map in maps:
        #print('In seed: ', str(seed))
        m = maps[map]
        start = m['source_start']
        end = [x + y for x, y in zip(start, m['range_length'])]
        diffs = [x - y for x, y in zip(start, m['destination_start'])]
        l = range(len(m['source_start']))
        for i in l:
            #print(seed)
            #print(start[i])
            #print(end[i])
            if seed in range(start[i], end[i]):
                seed = seed - diffs[i]
                break
            else:
                seed = seed
        #print('Out seed: ', str(seed))
    return seed

seed_locations = []
for seed in seeds:
    seed_locations.append(seed_to_location(seed))
seed_locations

min(seed_locations)

# Part 2
def seed_generator(seeds):

    for i in range(len(seeds)):
        if i % 2 == 0:
            start = seeds[i]
        else:
            yield range(start, start+seeds[i])
            #yield range(start, start+seeds[i])

min_loc = float('inf') 
for seed in seed_generator(seeds):
    for s in seed:
        loc = seed_to_location(s)
        if loc < min_loc:
            min_loc = loc
        #seed_locations.append(seed_to_location(s))
min_loc
        

