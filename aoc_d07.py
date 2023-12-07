import pandas as pd
import numpy as np
import re
import time
import os
import cProfile

os.chdir(r"C:\Users\dears002\Documents\adventofcode")
os.curdir

s = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

t0=time.time()
with open(r"C:\Users\dears002\Documents\adventofcode\input_d07.txt") as f:
    s = f.read()
f.close()

t0=time.time()
ls = s.splitlines()

ls = [s.split(' ') for s in ls]

df = pd.DataFrame(ls, columns=['HAND', 'BID'])

t0=time.time()
df['HAND_SORTED'] = df['HAND']
for i in range(len(df)):
    df['HAND_SORTED'][i] = ''.join(sorted(df['HAND'][i]))

df['BID'] = pd.to_numeric(df['BID'])

ranks = {'5K':7, '4K':6, 'FH':5, '3K':4, '2P':3, '1P':2, 'HC':1}

five_of_kind = re.compile(r'([AKQJT2-9])\1\1\1\1')
four_of_kind = re.compile(r'([AKQJT2-9])\1\1\1')
full_house = re.compile(r'^([AKQJT2-9])\1+([AKQJT2-9])\2+$')
three_of_kind = re.compile(r'([AKQJT2-9])\1\1')
two_pair = re.compile(r'([AKQJT2-9])\1.?([AKQJT2-9])\2')
one_pair = re.compile(r'([AKQJT2-9])\1')

def classify(col):
    if re.search(five_of_kind, col):
        return '5K'
    elif re.search(four_of_kind, col):
        return '4K'
    elif re.search(full_house, col):
        return 'FH'
    elif re.search(three_of_kind, col):
        return '3K'
    elif re.search(two_pair, col):
        return '2P'
    elif re.search(one_pair, col):
        return '1P'
    else:
        return 'HC'

def hand_to_num(hand):
    strength = '23456789TJQKA'
    num_str = ''
    for char in hand:
        rank = str(strength.index(char))
        if len(rank) == 1:
            rank = '0' + rank
        num_str += rank
    return num_str


df['TYPE'] = df['HAND_SORTED'].apply(classify)

df['TEMP_RANK'] = df['TYPE'].apply(lambda x: ranks.get(x))
df['NUM_HAND'] = df['HAND'].apply(hand_to_num)

df = df.sort_values(by=['TEMP_RANK', 'NUM_HAND'])

df['FINAL_RANK'] = range(1, len(df)+1)

df['WINNINGS'] = df['BID'] * df['FINAL_RANK']

df['WINNINGS'].sum()

# Part 2
def jokers(hand):
    if hand == 'JJJJJ':
        return hand
    else:
        cards = set.difference(set(hand), {'J'})
        high_hand=0
        high_rank = 0
        for card in cards:
            new_hand = hand.replace('J', card)
            new_hand_sorted = ''.join(sorted(new_hand))
            #print(new_hand_sorted)
            type = classify(new_hand_sorted)
            rank = ranks.get(type)
            if rank > high_rank:
                high_rank = rank
                high_hand = new_hand
        return high_hand

df['JOKER'] = df['HAND'].apply(lambda x: 'J' in x)

df['JOKER_HAND'] = df['HAND']
df['JOKER_HAND'][df['JOKER']==True] = df['HAND'].apply(jokers)


df['JOKER_HAND_SORTED'] = df['JOKER_HAND']
for i in range(len(df)):
    df['JOKER_HAND_SORTED'][i] = ''.join(sorted(df['JOKER_HAND'][i]))

df['JOKER_TYPE'] = df['JOKER_HAND_SORTED'].apply(classify)

df['JOKER_TEMP_RANK'] = df['JOKER_TYPE'].apply(lambda x: ranks.get(x))

def joker_hand_to_num(hand):
    strength = 'J23456789TQKA'
    num_str = ''
    for char in hand:
        rank = str(strength.index(char))
        if len(rank) == 1:
            rank = '0' + rank
        num_str += rank
    return num_str

df['JOKER_NUM_HAND'] = df['HAND'].apply(joker_hand_to_num)

df = df.sort_values(by=['JOKER_TEMP_RANK', 'JOKER_NUM_HAND'])

df['JOKER_FINAL_RANK'] = range(1, len(df)+1)

df['JOKER_WINNINGS'] = df['BID'] * df['JOKER_FINAL_RANK']

df['JOKER_WINNINGS'].sum()
t1=time.time()

total = t1-t0

df.to_csv(r'C:\Users\dears002\Documents\adventofcode\output_d07.csv')


