import re, os, functools, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *
from math import gcd
from functools import *

#file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
file = open(os.path.dirname(os.path.realpath(__file__)) + '/test')

lines = file.readlines()

