
d = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

d = d.split('\n')

with open('C:/Users/dears002/Documents/adventofcode/input_d04.txt') as f:
    d = f.readlines()
    d = [s.strip() for s in d]
f.close()

cards = {}

for i in range(len(d)):
    cards[i+1] = str(d[i].split(':')[1])

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

total_points = 0

for v in cards.values():
    print(v['length'])
    if v['length'] == 0:
        total_points +=0
    else:
        points = 2**(v['length']-1)
        print(points)
        total_points += points
    print(total_points)

# Part 2
for k, v in cards.items():
    v['copies'] = 1

for k, v in cards.items():
    for copy in range(v['copies']):
        num_winners = v['length']
        for i in range(k+1, k+num_winners+1):
            cards[i]['copies'] += 1

num_of_cards = 0
for k, v in cards.items():
    num_of_cards += v['copies']
num_of_cards