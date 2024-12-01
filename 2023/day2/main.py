import re, os, functools

file = open('day2/input')
lines = file.readlines()

games = {}

colors = ['blue', 'green', 'red']

bag = {'red':12, 'green':13, 'blue':14}

def isGamePossible(game):
    for pull in game:
        for color in colors:
            if int(pull.get(color, 999)) < bag[color]:
                return False
            
    return True

def findMins(game):
    mins = {'red':0, 'green':0, 'blue':0}

    for pull in game:
        for color in colors:
            if mins[color] < int(pull.get(color, 0)):
                mins[color] = int(pull[color])

    mins = { k:v for (k,v) in mins.items() if v != 0 }
    
    return functools.reduce(lambda a, b : a * b, mins.values())

def readGame(string):
    match = re.search(r'Game (\d+): ', string)
    num = match[1]
    string = re.sub(r'Game (\d+): ', '', string)

    pulls = []

    strs = string.split(';')

    for sIndex, s in enumerate(string.split(';')):
        pull = {}

        for color in colors:
            if s.find(color) == -1:
                continue
            pullCount = re.search('(\d+) ' + color, s)[1]
            pull[color] = pullCount
        
        pulls.append(pull)
            
    games[num] = pulls

for i in lines:
    readGame(i) 

#games = { k:v for (k,v) in games.items() if isGamePossible(v) }

s = [ findMins(v) for (k,v) in games.items() ]

print(s)

s = sum(s)

print(s)