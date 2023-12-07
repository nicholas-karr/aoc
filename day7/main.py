import re, os, functools, sys
from collections import defaultdict
    
def extractNums(string):
    nums = []

    match = re.findall(r'(\d+)', string)
    for i in match:
        nums.append(int(i))

    return nums

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
#file = open(os.path.dirname(os.path.realpath(__file__)) + '/test')
lines = file.readlines()

def parseHand(line):
    hand = line.split(' ')[0]
    bid = int(line.split(' ')[1])

    return (hand, bid)

#cardScore = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]
cardTypes = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J' ]
cardScore = { j: chr(ord('0') + i) for i, j in enumerate(reversed(cardTypes)) }

def sames(hand: str):
    m = 0
    counts = {}
    for i in hand:
        cnt = hand.count(i)
        if cnt > m:
            m = cnt
        if cnt in counts:
            counts[cnt].append(i)
        else:
            counts[cnt] = [i]

    return counts

def rawTypeOf(hand: str):
    s = sames(hand)

    if 5 in s:
        return 6
    elif 4 in s and 1 in s:
        return 5
    elif 3 in s and 2 in s:
        return 4
    elif 3 in s and 2 not in s:
        return 3
    elif 2 in s and len(s[2]) == 2 * 2:
        return 2
    elif 2 in s and len(s[2]) == 2:
        return 1
    elif 1 in s and len(s[1]) == 5:
        return 0
    
    print(hand)

def typeOf(hand:str):
    highest = 0

    if 5 in sames(hand) and hand[0] == 'J':
        print(' ')
    
    for newJoker in cardTypes:
        

        v = rawTypeOf(hand.replace('J', newJoker))

        if v > highest:
            highest = v

    return highest

def cmp(lhs, rhs):
    lt = typeOf(lhs[0])
    rt = typeOf(rhs[0])

    if lt == rt:
        lexigLhs = list(map(lambda i: cardScore[i], lhs[0]))
        lexigRhs = list(map(lambda i: cardScore[i], rhs[0]))
        res = ''.join(lexigLhs) > ''.join(lexigRhs)
    else:
        res = lt > rt

    if res:
        return 1
    elif not res:
        return -1
    else:
        print()

hands = [parseHand(i) for i in lines]
hands.sort(key=functools.cmp_to_key(cmp))

scores = []

print([(i, typeOf(i[0])) for i in hands])

for i, hand in reversed(list(enumerate(hands))):
    #score = typeOf(hand[0]) #* hand[1]
    #score = (hand[1], (i + 1))
    score = hand[1] * (i + 1)
    scores.append(score)

print(scores)
print(sum(scores))

#hands = [scoreOf(i) for i in lines]
#total = sum(hands)