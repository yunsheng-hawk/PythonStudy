'''
Created on 2013-2-22

@author: huysh1976
'''

'''
f = file("c:/ehcache1.xml")
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line,
print 'done.'
f.close()
'''

import cPickle as p
f = file("d:/temp.txt", "w")
items = ['s1', 2, 's2', 5.5,'s4']
p.dump(items, f, protocol=0)
f.close()

f = file ("d:/temp.txt")
loaded = p.load(f)

print "items:",items
print "loaded:", loaded