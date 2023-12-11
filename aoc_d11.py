import numpy as np

d = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''

with open(r"C:\Users\dears002\Documents\adventofcode\input_d11.txt") as f:
    d = f.read()
f.close()

u = d.split('\n')
u = u[:-1]

u = [list(r) for r in u]

u_arr = np.array(u)

empty_cols = []
for i in range(u_arr.shape[1]):
    if '#' not in u_arr[:,i]:
        empty_cols.append(i)
empty_cols

dots_column = np.full((u_arr.shape[0], 1), '.', dtype='<U1')
u_arr = np.insert(u_arr, empty_cols, dots_column, axis=1)

empty_rows = []
for i in range(u_arr.shape[0]):
    if '#' not in u_arr[i,:]:
        empty_rows.append(i)
empty_rows

dots_column = ['.' for i in range(u_arr.shape[1])]
u_arr = np.insert(u_arr, empty_rows, dots_column, axis=0)

indices = list(np.where(u_arr == '#'))
indices = [a.tolist() for a in indices]
indices = list(zip(indices[0], indices[1]))
indices

sum = 0
for i in range(len(indices)):
    current_i = indices[i]
    for j in range(i+1, len(indices)):
        d = abs(indices[j][1]-indices[i][1]) + abs(indices[j][0]-indices[i][0])
        print(str(i+1), ' to ', str(j+1), ': ', d)
        sum += d
sum