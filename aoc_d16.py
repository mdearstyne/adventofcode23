import numpy as np

import time

d = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''

t0=time.time()
with open(r"C:\Users\dears002\Documents\adventofcode\input_d16.txt") as f:
    d = f.read()
f.close()

d = d.split()
           
d = [[e for e in l] for l in d]
a = np.array(d)
a

class SplitException(Exception):
        pass

class Beam():
    
    def __init__(self, start=None, direction='R'):
        if start ==None:
            start = (0, 0)
        self.current_position = start
        self.previous_position = start
        self.crow = self.current_position[0]
        self.ccol = self.current_position[1] 
        self.direction = direction
    
    def info(self):
        #print(self.current_position, self.direction)
        return self.current_position
    
    def update_position(self):
        self.current_position = [self.crow, self.ccol]
        if -1 in self.current_position:
            raise IndexError
    
    def move_up(self):
        self.crow -= 1
        self.direction = 'U'
        self.update_position()
    
    def move_down(self):
        self.crow += 1
        self.direction = 'D'
        self.update_position()
    
    def move_left(self):
        self.ccol -= 1
        self.direction = 'L'
        self.update_position()
    
    def move_right(self):
        self.ccol += 1
        self.direction = 'R'
        self.update_position()

    
    def move_beam(self, symbol):
        if self.direction == 'R':
            if symbol in ['-', '.']:
                self.move_right()
            elif symbol == '\\':
                self.move_down()
            elif symbol == '/':
                self.move_up()
            elif symbol == '|':
                self.move_down()
                raise SplitException
        elif self.direction == 'L':
            if symbol in ['-', '.']:
                self.move_left()
            elif symbol == '\\':
                self.move_up()
            elif symbol == '/':
                self.move_down()
            elif symbol == '|':
                self.move_down()
                raise SplitException
        elif self.direction == 'U':
            if symbol == '-':
                self.move_right()
                raise SplitException
            elif symbol == '\\':
                self.move_left()
            elif symbol == '/':
                self.move_right()
            elif symbol in ['|','.']:
                self.move_up()
        elif self.direction == 'D':
            if symbol == '-':
                self.move_right()
                raise SplitException
            elif symbol == '\\':
                self.move_right()
            elif symbol == '/':
                self.move_left()
            elif symbol in ['|','.']:
                self.move_down()

def traverse_contraption(contraption = np.empty([0,0]), beam=Beam()):
    
    contraption = contraption.copy()

    col = beam.ccol
    row = beam.crow

    path = [(col, row)]
    
    current_symbol = contraption[row, col]

    beam_collection = []
    energized = set()
    energized.add((row, col))

    splits = set()

    while(True):
        #print('Starting at: [', row, ',', col, ']: Going', beam.direction)
        #print('Current symbol: ', current_symbol)
        try:
            beam.move_beam(current_symbol)
        except SplitException:
            #print('Beam has split, added to collection')
            #print(row, col)
            if beam.direction in ['L', 'R']:
                split_direction = 'L'
            else:
                split_direction = 'U'
            if (row, col) not in splits:
                split_beam = Beam(start=(row, col), direction = split_direction)
                beam_collection.append(split_beam)
                splits.add((row, col))
            else:
                break
        except IndexError:
            #print('At wall')
            #contraption[row, col] = '#'
            #print(contraption)
            energized.add((row, col))
            break

        # Change previous element
        #contraption[row, col] = '#'

        # Add to set
        energized.add((row, col))
        col, row = beam.ccol, beam.crow
        try:
            current_symbol = contraption[row, col]
            #print('Beam now at', beam.current_position, 'New symbol: ', current_symbol)
            #print(contraption)
        except IndexError:
            #print('At wall')
            #print(contraption)
            break
        
        path.append((row, col))
        if path.count((row, col)) >=3:
            break
        
    #print(contraption)
    #print(len(energized), energized)
    #print(len(beam_collection), "beams remaining")
    return energized, beam_collection 

#def combine_beams(a, first_beam=Beam()):
    
def collapse_beams(energized=set(), beam_collection=[Beam()]):
    
    if not isinstance(beam_collection, list):
        beam_collection = [beam_collection]

    splits = set()

    while len(beam_collection) > 0:
        beam = beam_collection.pop(0)
        if beam.info() in splits:
            #print(len(beam_collection))
            continue
        else:
            splits.add(beam.info())
            temp_energized, temp_collection = traverse_contraption(a, beam)
            energized.update(temp_energized)
            beam_collection.extend(temp_collection)
            #print(len(energized))
            #print(len(beam_collection))
    
    return len(energized)

#t0 = time.time()
collapse_beams()
#t1 = time.time()
#t1-t0
# Part 2
#t0 = time.time()
top = [(0, i) for i in range(len(a))]
left = [(i, 0) for i in range(len(a))]
bottom = [(len(a)-1, i) for i in range(len(a))]
right = [(i, len(a)-1) for i in range(len(a))]

sides = [top, left, bottom, right]

max_energized = 0

for side in sides:
    for start in side:
        num_energized = collapse_beams()
        if num_energized > max_energized:
            max_energized = num_energized

max_energized
t1 = time.time()
t1-t0

