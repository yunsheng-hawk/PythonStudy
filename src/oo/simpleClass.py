'''
Created on 2013-2-21

@author: huysh1976
'''
from sqlalchemy.orm.collections import __del
class Person:
    count = 0
    def __del__(self):
        Person.count -= 1    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    def sayHi(self):
        print 'hi,', self.name
    def printCount(self):
        print 'total:', Person.count
        
class Police(Person):
    def __init__(self, name, rank):
        Person.__init__(self, name)
        self.rank = rank
    def sayHi(self):
        print 'hi,', self.name, self.rank
        
p1 = Person("zhangs")
p1.sayHi()
p1.printCount()
p2 = Person("lisi")
p2.sayHi()
p2.printCount()
del p2
p1.printCount()
p3 = Police("wangw", 5)
p3.sayHi()
p3.printCount()
p4 = Person("zhaol")
p4.sayHi()
p4.printCount()

