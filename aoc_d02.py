with open("C:/Users/dears002/Documents/adventofcode/input_d02.txt") as file:
    d = file.readlines()
file.close()

max = {'red':12, 'green':13, 'blue':14}

games = {}

g = 1
for line in d:
    games[g] = line.split(':')[1].strip().split(';')
    g+=1

for k, v in games.items():
    sets = {}
    for i in range(len(v)):
        sets[i+1] = v[i]
    games[k] = sets

for game in games.values():
    for k, v in game.items():
        game[k] = v.split(',')

for game in games.values():
    for k, v in game.items():
        colors = {}
        for i in range(len(v)):
            a, b = v[i].strip().split(' ')
            colors[b] = a
        game[k] = colors

id_sum = 0

for k, v in games.items():
    count = True
    for set in v.values():
        for color, value in set.items():
            if int(value) > max[color]:
                count = False
    if count is True:
        id_sum += k

# Part 2
for k, v in games.items():
    color_min = {'red':0, 'blue':0, 'green':0}
    for set in v.values():
        for a, b in set.items():
            if color_min[a] < int(b):
                color_min[a] = int(b)
    v['power'] = color_min['red'] * color_min['blue'] * color_min['green']
        
power_sum = 0

for game in games.values():
    power_sum += game['power']
    

    

        

