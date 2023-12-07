import pandas as pd

d = pd.read_table('C:/Users/dears002/Documents/adventofcode/input_d04.txt', sep='|', names=None)

with open('C:/Users/dears002/Documents/adventofcode/input_d04.txt') as f:
    d = f.readlines()
    d = [s.strip() for s in d]
f.close()

cards = {}

for i in range(len(d)):
    cards[d[i].split(':')[0]] = str(d[i].split(':')[1])

for k, v in cards.items():
    print(k, v)
    cards[k] = {'winners':v.split('|')[0].strip(), 'numbers':v.split('|')[1].strip()}

for v in cards.values():
    v['winners'] = v['winners'].replace('  ', ' ')
    v['winners'] = v['winners'].split(' ')
    v['winners'] = set([int(s) for s in v['winners']])
    v['numbers'] = v['numbers'].replace('  ', ' ')
    v['numbers'] = v['numbers'].split(' ')
    v['numbers'] = set([int(s) for s in v['numbers']])

for v in cards.values():
    v['intersection'] = set.intersection(v['winners'], v['numbers'])
    v['length'] = len(v['intersection'])

sum = 0

for v in cards.values():
    print(v['length'])
    if v['length'] == 0:
        sum +=0
    else:
        points = 2**(v['length']-1)
        print(points)
        sum += points
    print(sum)