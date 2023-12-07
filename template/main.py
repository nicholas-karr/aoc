import re, os, functools, sys

sys.path.insert(0, '..')


from util import *

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

print(lines)