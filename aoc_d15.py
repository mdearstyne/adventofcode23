# Day 15

# test input

d = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
d = d.split(',')

'''Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256.'''

def HASH_algorithm(s):
    #print(s)
    current_code = 0
    for char in s:
        #print(char)
        current_code += ord(char)
        current_code *= 17
        current_code %= 256
        #print(char, current_code)
    return current_code

total = 0
for s in d:
    total += HASH_algorithm(s)
total

with open(r'C:\Users\dears002\Documents\adventofcode\input_d15.txt') as f:
    d = f.read()
f.close()

d = d.replace('\n', '')
d = d.split(',')

total = 0
for s in d:
    total += HASH_algorithm(s)
total

# Part 2
def parse_string(s):
    if '-' in s:
        label = s[:-1]
        op = '-'
        focal_length = 0
    else:
        label, focal_length = s.split('=')
        op = '='
    return label, op, focal_length

def get_boxes(d):
    boxes = {}
    i = 1
    for s in d:
        print('****')
        print(i)
        l, o, f = parse_string(s)
        #print(l, o, f)

        box = HASH_algorithm(l)
        print('Label: ', l, ' Box: ', box, ' Op: ' , o, ' Focal Length: ', f)

        if box not in boxes:
            print('Box not in boxes: adding...')
            boxes[box] = [list(), list()]
            print(boxes)
        
        current_box = boxes[box]
        labels_in_box = current_box[0]
        focal_lengths_in_box = current_box[1]
        print('Current box: ', current_box, 'Labels in box: ', labels_in_box, 'Focal lengths in box: ', focal_lengths_in_box)
        
        if o == '=':
            #print(labels)
            #print(focal_lengths)
            if l not in labels_in_box:
                print('Label not in box, adding...')
                labels_in_box.append(l)
                focal_lengths_in_box.append(f)
                print('Labels in box: ', labels_in_box, 'Focal lengths in box: ', focal_lengths_in_box)
            else:
                label_position = labels_in_box.index(l)
                print('Label exists at position ', label_position, '. Updating...')
                print('Old box: ', current_box)
                labels_in_box[label_position] = l
                focal_lengths_in_box[label_position] = f
                print('Updated box: ', current_box)
                print('All boxes: ', boxes)
        
        elif o == '-':
            if l not in labels_in_box:
                print('Label not in box, nothing to do')
                pass
            else:
                print('Removing label and focal length')
                print('Old labels in box: ', labels_in_box)
                print('Old focal lenghts in box: ', focal_lengths_in_box)
                label_position = labels_in_box.index(l)
                labels_in_box.remove(l)
                old_f = focal_lengths_in_box[label_position]
                del focal_lengths_in_box[label_position]
                print('New labels in box: ', labels_in_box)
                print('New focal lenghts in box: ', focal_lengths_in_box)
        print('Done with ', s)
        print('****')
        i+=1
    return boxes

def get_focusing_powers(b):

    focusing_powers = []

    for box in b:
        if b[box] == [[],[]]:
            next
        else:
            current_box = b[box]
            print(current_box)
            focal_lengths = current_box[1]
            #print(focal_lengths)
            for i in range(len(focal_lengths)):
                print(box+1, i+1, focal_lengths[i])
                fp = (box+1) * (i+1) * int(focal_lengths[i])
                print(focal_lengths[i], fp)
                focusing_powers.append(fp)

    print(focusing_powers)
    
    return sum(focusing_powers)

boxes = get_boxes(d)
get_focusing_powers(boxes)