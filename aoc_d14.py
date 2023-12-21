# Day 14

# Part 1
import numpy as np

d = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''

with open(r'C:\Users\dears002\Documents\adventofcode\input_d14.txt') as f:
    d = f.read()
f.close()

d = d.split()
d = [[e for e in l] for l in d]
dish = np.array(d)

def roll_blocks(reflector):
    a = np.copy(reflector)
    changes = 0
    for i in range(len(a)-1):
        current_row = a[i]
        next_row = a[i+1]
        for j in range(len(current_row)):
            if current_row[j] == '.' and next_row[j] == 'O':
                current_row[j] = 'O'
                next_row[j] = '.'
                changes+=1
    if changes == 0:
        #print('No changes, returning...')
        return a
    else:
        #print('Starting recursion...')
        return roll_blocks(a)

b = roll_blocks(dish)

def calculate_load(a):
    total_load = 0
    for i in range(len(a)):
        current_row = a[i]
        stone_count = np.where(current_row == 'O')[0].size
        factor = len(a)-i
        total_load += stone_count * factor
    return total_load

calculate_load(b)

# Part 2

def spin_cycle(dish, n):
    prev_dishes = []
    a = np.copy(dish)
    #print('Input')
    #print(a)
    cycle = 0
    result_of_last_cycle = a.copy()
    while cycle < n:
        i = 0
        while i < 4:
            if i%4 == 0:
                a = roll_blocks(a)
            elif i%4 == 1:
                temp_a = np.rot90(a, k=1, axes=(1,0)).copy()
                temp_a = roll_blocks(temp_a)
                a = np.rot90(temp_a, k=1, axes=(0,1)).copy()
            elif i%4 == 2:
                temp_a = np.rot90(a, k=2, axes=(1,0)).copy()
                temp_a = roll_blocks(temp_a)
                a = np.rot90(temp_a, k=2, axes=(0,1)).copy()
            elif i%4 == 3:
                temp_a = np.rot90(a, k=3, axes=(1,0)).copy()
                temp_a = roll_blocks(temp_a)
                a = np.rot90(temp_a, k=3, axes=(0,1)).copy()
            #print('After', i+1, 'spins')
            #print(a)
            i+=1
        #print('After', cycle+1, 'cycle(s)')
        #print(a)
        cycle+=1

        for d in prev_dishes:
            if np.array_equal(d, a):
                print('Prev dish found at cycle', cycle)
                break
            else:
                prev_dishes.append(a)

        if cycle % 10000 == 0:
            print('On cycle', cycle)

        if np.array_equal(a, result_of_last_cycle):
            print('New array is equal to original after cycle', cycle)
            break
        else:
            #print(a)
            #print(result_of_last_cycle)
            #print(np.array_equal(a, result_of_last_cycle))
            result_of_last_cycle = a.copy()


    return a

b = spin_cycle(dish, 1000000000)

b = np.rot90(a, axes=(1,0))
b
c = np.rot90(b, axes=(1,0))
c
d = np.rot90(c, axes=(1,0))
d