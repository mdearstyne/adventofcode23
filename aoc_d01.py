import re

with open("C:/Users/dears002/Documents/adventofcode/input_d01.txt") as file:
    d = file.readlines()
file.close()

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
nums_dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

file_sum = 0

for line in d:

    ids = {}

    for num in nums:
        start = 0
        stop = len(line)
        id_list = []
        id = line.find(num)
        if id == -1:
            continue
        else:
            while id != -1:
                if len(num) == 1:
                    ids[id] = num
                else:
                    ids[id] = nums_dict[num]
                start = id
                id = line.find(num, start+1, stop)

    high = max(ids.keys())
    low = min(ids.keys())
    added = int(ids[low] + ids[high])
    file_sum += added

file_sum

    
for num in nums.values():
    start = 0
    stop = len(line)
    id_list = []
    id = line.find(num)
    if id == -1:
        continue
    else:
        while id != -1:
            id_list.append(id)
            start = id
            id = line.find(num, start+1, stop)
    ids[num] = id_list

low = float('int')
high = 0
minmax = {}

for key in ids.keys():
    if min(ids[key]) < low:
        low = min(ids[key])
    if max(ids[key]) > high:
        high = max(ids[key])
    minmax[key] = {'max': high, 'min': low}
    
    


