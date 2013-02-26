'''
Created on 2013-2-22

@author: huysh1976
'''
from compiler.ast import TryExcept
class ShortInputException(Exception):
    def __init__(self, length, min):
        self.length = length
        self.min = min

try:
    input = raw_input("Input some content:")
    if len(input) < 5:
        raise ShortInputException(len(input), 5)
    print "input:", input
except ShortInputException, se:
    print 'input content is too short to display, the current length is %s and the min is %s' % (se.length, se.min)
except:
    print 'Exception occurred.'
    
    